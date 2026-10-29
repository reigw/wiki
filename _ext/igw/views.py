"""Generate portable Docutils content from the collected entity registry."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from itertools import groupby

from docutils import nodes
from sphinx import addnodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.docutils import SphinxDirective


class PendingView(nodes.General, nodes.Element):
    """Persist a query in the doctree, never a copy of its result."""


def parse_type(value):
    from .domain import entity_type

    return entity_type(value)


def parse_id(value):
    from .domain import identifier

    return identifier(value)


def parse_columns(value):
    from .domain import comma_list, identifier

    columns = tuple(identifier(column) for column in comma_list(value))
    if len(set(columns)) != len(columns):
        raise ValueError("statistics columns must be unique")
    return columns


class ViewDirective(SphinxDirective):
    """Parse presentation queries separately from entity definitions."""

    optional_arguments = 1
    # Parsers defer domain imports to avoid a cycle during domain registration.
    option_spec = {
        "type": parse_type, "faction": parse_id, "columns": parse_columns,
        "sort-by": parse_id,
    }

    def run(self):
        view = self.name.partition(":")[2]
        allowed = {"type", "faction", "columns", "sort-by"} if view == "statistics" else (
            {"type", "faction"} if view == "entity-list" else set()
        )
        if unsupported := self.options.keys() - allowed:
            raise self.error(f"unsupported options for igw:{view}: {', '.join(sorted(unsupported))}")
        if view in ("infobox", "backlinks"):
            if not self.arguments:
                raise self.error(f"igw:{view} requires an entity target")
        elif self.arguments:
            raise self.error(f"igw:{view} accepts filters as options, not an argument")
        node = PendingView(
            view=view, target=self.arguments[0] if self.arguments else "",
            docname=self.env.docname, **self.options,
        )
        self.set_source_info(node)
        return [node]


def entity_link(entity, docname):
    """Use Sphinx's resolver for every builder, including single-document ones."""
    node = addnodes.pending_xref(
        "", refdomain="igw", reftype="entity", reftarget=entity.key,
        refdoc=docname, refexplicit=True, refwarn=True,
    )
    node += nodes.inline("", entity.name)
    return node


def field(label, content):
    if isinstance(content, str):
        content = nodes.Text(content)
    return nodes.field("", nodes.field_name("", label), nodes.field_body("", nodes.paragraph("", "", content)))


def display_label(identifier):
    return identifier.replace("-", " ").capitalize()


def statistic_sort_key(entity, column):
    """Sort numeric values numerically, then text, with missing values last."""
    value = entity.stats.get(column)
    if value is None:
        return (2, "")
    try:
        number = Decimal(value)
    except InvalidOperation:
        pass
    else:
        # Nonfinite values cannot provide a consistent numeric ordering.
        if number.is_finite():
            return (0, number)
    return (1, value.casefold())


def infobox_statistics(entity):
    """Format infobox statistics without changing their stored definitions."""
    difficulties = ("easy", "medium", "hard", "brute", "god")
    setting_keys = {f"{difficulty}-setting" for difficulty in difficulties}
    settings_rendered = False
    for key, value in entity.stats.items():
        # The source uses this placeholder when a cvar has no recorded flags.
        if entity.kind == "cvar" and key == "flags" and value == "None listed":
            continue
        if entity.kind != "cvar" or key not in setting_keys:
            yield display_label(key), value
            continue
        if settings_rendered:
            continue
        settings_rendered = True
        # Missing settings break ranges; compare the authored values literally.
        for setting, group in groupby(
            difficulties, key=lambda difficulty: entity.stats.get(f"{difficulty}-setting"),
        ):
            names = list(group)
            if setting is None:
                continue
            label = names[0].capitalize()
            if len(names) > 1:
                label += f"-{names[-1].capitalize()}"
            yield f"{label} setting", setting


class RenderViews(SphinxPostTransform):
    """Expand queries after collection and before normal reference resolution."""

    default_priority = 5

    def run(self, **kwargs):
        domain = self.env.get_domain("igw")
        for node in list(self.document.findall(PendingView)):
            renderer = getattr(self, f"render_{node['view'].replace('-', '_')}")
            node.replace_self(renderer(domain, node))

    def render_infobox(self, domain, node):
        entity = domain.find(node["target"])
        if entity is None:
            return nodes.paragraph("", f"Unknown entity: {node['target']}")
        box = nodes.container("", classes=["igw-infobox"])
        fields = nodes.field_list()
        if not node.get("hide_name", False):
            fields += field("Name", entity_link(entity, node["docname"]))
        fields += field("Type", entity.kind)
        if entity.summary:
            fields += field("Summary", entity.summary)
        for label, value in infobox_statistics(entity):
            fields += field(label, value)
        for relation in ("faction", "upgrade", "related"):
            targets = [target for kind, target in entity.relations if kind == relation]
            if not targets:
                continue
            links = nodes.inline()
            for index, target in enumerate(targets):
                if index:
                    links += nodes.Text(", ")
                related = domain.find(target)
                links += entity_link(related, node["docname"]) if related else nodes.Text(target)
            fields += field({"faction": "Faction", "upgrade": "Upgrades", "related": "Related"}[relation], links)
        box += fields
        return box

    def selected(self, domain, node):
        """Apply filters to current definitions, including newly added entities."""
        entities = domain.data["registry"].values()
        if "type" in node:
            entities = [entity for entity in entities if entity.kind == node["type"]]
        if "faction" in node:
            relation = ("faction", f"faction:{node['faction']}")
            entities = [entity for entity in entities if relation in entity.relations]
        return sorted(entities, key=lambda entity: (entity.name.casefold(), entity.key))

    def render_entity_list(self, domain, node):
        entities = self.selected(domain, node)
        if not entities:
            return nodes.paragraph("", "No matching entities.")
        result = nodes.bullet_list()
        for entity in entities:
            result += nodes.list_item("", nodes.paragraph("", "", entity_link(entity, node["docname"])))
        return result

    def render_statistics(self, domain, node):
        entities = self.selected(domain, node)
        if not entities:
            return nodes.paragraph("", "No matching entities.")
        if "sort-by" in node:
            # Stable sorting retains the default name/ID ordering for ties.
            entities.sort(key=lambda entity: statistic_sort_key(entity, node["sort-by"]))
        columns = node.get("columns", sorted({key for entity in entities for key in entity.stats}))
        table = nodes.table(classes=["igw-statistics"])
        group = nodes.tgroup(cols=len(columns) + 1)
        table += group
        for column in range(len(columns) + 1):
            group += nodes.colspec(colwidth=1)
        head = nodes.thead()
        row = nodes.row()
        for label in ("Name", *(display_label(column) for column in columns)):
            row += nodes.entry("", nodes.paragraph("", label))
        head += row
        group += head
        body = nodes.tbody()
        for entity in entities:
            row = nodes.row()
            row += nodes.entry("", nodes.paragraph("", "", entity_link(entity, node["docname"])))
            for column in columns:
                row += nodes.entry("", nodes.paragraph("", entity.stats.get(column, "Unknown")))
            body += row
        group += body
        return table

    def render_backlinks(self, domain, node):
        entity = domain.find(node["target"])
        if entity is None:
            return nodes.paragraph("", f"Unknown entity: {node['target']}")
        # Presentation queries do not count as authored semantic relationships.
        documents = domain.data["backlinks"].get(entity.key, set()) - {node["docname"]}
        if not documents:
            return nodes.paragraph("", "No related articles.")
        result = nodes.bullet_list()
        for docname in sorted(documents):
            title = self.env.titles.get(docname)
            link = addnodes.pending_xref(
                "", refdomain="std", reftype="doc", reftarget=f"/{docname}",
                refdoc=node["docname"], refexplicit=True, refwarn=True,
            )
            link += nodes.inline("", title.astext() if title is not None else docname)
            result += nodes.list_item("", nodes.paragraph("", "", link))
        return result

"""Typed definitions and document-owned data, independent of their rendering."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import re

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.domains import Domain, ObjType
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_refnode

from .views import PendingView, ViewDirective


LOGGER = logging.getLogger(__name__)
KINDS = ("weapon", "upgrade", "file-extension", "enemy", "level", "faction", "building", "cvar", "entity")
IDENTIFIER = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def identifier(value):
    """Keep stable IDs independent of display names and document locations."""
    value = value.strip()
    if not IDENTIFIER.fullmatch(value):
        raise ValueError("expected a lowercase ID containing letters, digits, and single hyphens")
    return value


def entity_type(value):
    value = value.strip()
    if value not in KINDS:
        raise ValueError(f"expected an entity type: {', '.join(KINDS)}")
    return value


def nonempty(value):
    value = value.strip()
    if not value:
        raise ValueError("expected a nonempty value")
    return value


def comma_list(value):
    """Reject empty items instead of silently dropping malformed references."""
    return tuple(nonempty(item) for item in value.split(","))


def statistics(value):
    """Parse literal statistics without inferring game-specific types or ranges."""
    result = {}
    for line in value.splitlines():
        if not line.strip():
            continue
        key, separator, text = line.partition(":")
        if not separator:
            raise ValueError("expected one 'statistic-id: value' per line")
        key = identifier(key)
        if key in result:
            raise ValueError(f"duplicate statistic {key!r}")
        result[key] = nonempty(text)
    if not result:
        raise ValueError("expected at least one statistic")
    return result


@dataclass(frozen=True)
class Entity:
    """The sole stored definition of an entity, including its source location."""

    kind: str
    identifier: str
    name: str
    summary: str
    stats: dict[str, str]
    relations: tuple[tuple[str, str], ...]
    docname: str
    line: int

    @property
    def key(self):
        return f"{self.kind}:{self.identifier}"

    @property
    def anchor(self):
        return f"igw-{self.kind}-{self.identifier}"


class EntityDirective(SphinxDirective):
    """Collect data once; leave infobox rendering to the post-read phase."""

    required_arguments = 1
    has_content = True
    option_spec = {
        "name": nonempty,
        "summary": nonempty,
        "stats": statistics,
        "faction": identifier,
        "upgrades": comma_list,
        "related": comma_list,
        "no-infobox": directives.flag,
    }

    def run(self):
        kind = self.name.partition(":")[2]
        try:
            entity_id = identifier(self.arguments[0])
            relations = []
            if "faction" in self.options:
                relations.append(("faction", f"faction:{self.options['faction']}"))
            for target in self.options.get("upgrades", ()):
                relations.append(("upgrade", f"upgrade:{identifier(target)}"))
            for target in self.options.get("related", ()):
                target_kind, separator, target_id = target.partition(":")
                if not separator:
                    raise ValueError("related targets must use 'type:id'")
                relations.append(("related", f"{entity_type(target_kind)}:{identifier(target_id)}"))
        except ValueError as error:
            raise self.error(str(error))

        entity = Entity(
            kind, entity_id, self.options.get("name", entity_id),
            self.options.get("summary", ""), self.options.get("stats", {}),
            tuple(relations), self.env.docname, self.lineno,
        )
        domain = self.env.get_domain("igw")
        domain.document(self.env.docname)["entities"].append(entity)

        container = nodes.container("", ids=[entity.anchor], classes=["igw-entity", f"igw-{kind}"])
        self.set_source_info(container)
        self.state.document.note_explicit_target(container)
        container += nodes.rubric("", entity.name)
        if "no-infobox" not in self.options:
            view = PendingView(view="infobox", target=entity.key, docname=self.env.docname)
            self.set_source_info(view)
            container += view
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        return [container]


class IGWDomain(Domain):
    """Registry, semantic roles, and lifecycle management for wiki entities."""

    name = "igw"
    label = "Iron Grip: Warlord"
    data_version = 1
    object_types = {
        kind: ObjType(kind.replace("-", " "), kind, *(() if kind == "entity" else ("entity",)))
        for kind in KINDS
    }
    directives = {
        **dict.fromkeys(KINDS, EntityDirective),
        **dict.fromkeys(("infobox", "statistics", "entity-list", "backlinks"), ViewDirective),
    }
    roles = {kind: XRefRole(warn_dangling=True, innernodeclass=nodes.inline) for kind in KINDS}
    initial_data = {"documents": {}, "registry": {}, "backlinks": {}, "fingerprint": ""}

    def document(self, docname):
        """Own every parsed record by its source document for purge and merge."""
        return self.data["documents"].setdefault(
            docname, {"entities": [], "references": [], "views": [], "title": ""},
        )

    def clear_doc(self, docname):
        self.data["documents"].pop(docname, None)

    def merge_domaindata(self, docnames, otherdata):
        # Workers inherit old data; only their explicitly reread documents count.
        for docname in docnames:
            self.clear_doc(docname)
            if docname in otherdata["documents"]:
                self.data["documents"][docname] = otherdata["documents"][docname]

    def process_doc(self, env, docname, document):
        """Capture semantic links before Sphinx replaces pending references."""
        references = []
        for node in document.findall(addnodes.pending_xref):
            if node.get("refdomain") == "igw":
                references.append((node["reftype"], node["reftarget"], node.line))
            elif not node.get("refdomain") and node.get("reftype") == "any":
                references.append(("any", node["reftarget"], node.line))
        views = [(node.attributes.copy(), node.line) for node in document.findall(PendingView)]
        if references or views:
            data = self.document(docname)
            data["references"] = references
            data["views"] = views
        if docname in self.data["documents"]:
            # A referring article's title is displayed by other pages' backlinks.
            title = next(document.findall(nodes.title), None)
            self.document(docname)["title"] = title.astext() if title is not None else docname

    def find(self, target, kind="entity"):
        """Unqualified generic references must identify exactly one entity."""
        registry = self.data["registry"]
        if ":" in target:
            entity = registry.get(target)
            return entity if entity and (kind in ("entity", "any") or entity.kind == kind) else None
        if kind not in ("entity", "any"):
            return registry.get(f"{kind}:{target}")
        matches = [entity for entity in registry.values() if entity.identifier == target]
        return matches[0] if len(matches) == 1 else None

    def prepare(self):
        """Recompute derived lookups after all serial or parallel reads finish."""
        registry = {}
        documents = self.data["documents"]
        for docname, data in sorted(documents.items()):
            for entity in data["entities"]:
                if entity.key in registry:
                    previous = registry[entity.key]
                    LOGGER.warning(
                        "duplicate igw entity %r; first defined in %s:%s",
                        entity.key, previous.docname, previous.line,
                        location=(docname, entity.line), type="igw", subtype="duplicate",
                    )
                else:
                    registry[entity.key] = entity
        self.data["registry"] = registry

        backlinks = {}
        for docname, data in sorted(documents.items()):
            references = list(data["references"])
            for entity in data["entities"]:
                for relation, target in entity.relations:
                    if not self.find(target):
                        self.warn_target(target, (docname, entity.line))
                    references.append(("entity", target, entity.line))
            for kind, target, line in references:
                entity = self.find(target, kind)
                if entity:
                    backlinks.setdefault(entity.key, set()).add(docname)
            for view, line in data["views"]:
                if view["view"] in ("infobox", "backlinks") and not self.find(view["target"]):
                    self.warn_target(view["target"], (docname, line))
                if "faction" in view and not self.find(view["faction"], "faction"):
                    self.warn_target(f"faction:{view['faction']}", (docname, line))
        self.data["backlinks"] = backlinks

    @staticmethod
    def warn_target(target, location):
        LOGGER.warning(
            "unknown or ambiguous igw target %r; use 'type:id' for generic targets",
            target, location=location, type="igw", subtype="reference",
        )

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        entity = self.find(target, typ)
        if entity is None:
            return None
        if not node.get("refexplicit"):
            contnode = nodes.inline("", entity.name, classes=contnode.get("classes", []))
        return make_refnode(builder, fromdocname, entity.docname, entity.anchor, contnode, entity.name)

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        # Give Sphinx every candidate so it can diagnose ambiguity across domains.
        matches = [entity for entity in self.data["registry"].values()
                   if target in (entity.key, entity.identifier)]
        return [(f"igw:{entity.kind}", make_refnode(
            builder, fromdocname, entity.docname, entity.anchor,
            contnode.deepcopy(), entity.name,
        )) for entity in matches]

    def get_objects(self):
        for key, entity in sorted(self.data["registry"].items()):
            yield key, entity.name, entity.kind, entity.docname, entity.anchor, 1


def update_database(app, env):
    """Invalidate consumers when definitions, relationships, or links change."""
    domain = env.get_domain("igw")
    domain.prepare()
    documents = domain.data["documents"]
    fingerprint = sha256(repr(sorted(documents.items())).encode()).hexdigest()
    if fingerprint == domain.data["fingerprint"]:
        return []
    domain.data["fingerprint"] = fingerprint
    # Rewriting is enough: stored doctrees retain unresolved views and references.
    # All consumers must update even when a new entity matches an old list filter.
    return sorted(set(documents) & env.found_docs)

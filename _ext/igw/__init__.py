"""Build-time entity database and presentation for the Iron Grip wiki."""

from .domain import IGWDomain, update_database
from .views import PendingView, RenderViews


def setup(app):
    """Register the domain and resolve views before Sphinx resolves links."""
    app.add_domain(IGWDomain)
    app.add_node(PendingView)
    app.add_post_transform(RenderViews)
    app.connect("env-updated", update_database)
    return {
        "version": "0.1",
        "env_version": 2,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

"""Facebook Business MCP Servers - Three-Layer Architecture."""

# Keep for backward compatibility
from .marketing_api.insights import insights_server

__all__ = [
    "insights_server",
]

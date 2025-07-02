"""AdsQuickViews MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adsquickviews import AdsQuickViews
from fastmcp import FastMCP

from src.generated.models.adsquickviews import AdsQuickViewsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsQuickViews"
instructions = """
AdsQuickViews MCP Server for Facebook Business API.

Provides typed access to all AdsQuickViews operations.
"""

adsquickviews_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsquickviews_server.tool
@wrapped_fn_tool
def get_adsquickviews(
    adsquickviews_id: str,
    fields: list[AdsQuickViewsField] = [],
) -> str:
    """Get a AdsQuickViews object by ID.

    Args:
        adsquickviews_id: The ID of the AdsQuickViews.
        fields: Fields to retrieve. Available fields: See AdsQuickViewsField type.
    """
    obj = AdsQuickViews(adsquickviews_id)
    return obj.api_get(fields=fields)

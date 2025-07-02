"""AdCreative MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adcreative import AdCreative
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdCreative"
instructions = """
AdCreative MCP Server for Facebook Business API.

Provides typed access to all AdCreative operations.
"""

adcreative_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adcreative_server.tool
@wrapped_fn_tool
def get_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
) -> str:
    """Get a AdCreative object by ID.

    Args:
        adcreative_id: The ID of the AdCreative.
        fields: Fields to retrieve. Available fields: See {server_info.object_name}Field type.
    """
    obj = AdCreative(adcreative_id)
    return obj.api_get(fields=fields)


@adcreative_server.tool
@wrapped_fn_tool
def update_adcreative(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict = {},
) -> str:
    """Update a AdCreative object.

    Args:
        adcreative_id: The ID of the AdCreative.
        fields: Fields to return after update. Available fields: See {server_info.object_name}Field type.
        params: Parameters to update. Available params: See AdCreativeUpdateParams type.
    """
    return AdCreative(adcreative_id).api_update(fields=fields, params=params)


@adcreative_server.tool
@wrapped_fn_tool
def delete_adcreative(
    adcreative_id: str,
) -> str:
    """Delete a AdCreative object.

    Args:
        adcreative_id: The ID of the AdCreative.
    """
    return AdCreative(adcreative_id).api_delete()


# ---- Edge Methods (2) ----
@adcreative_server.tool
@wrapped_fn_tool
def create_ad_label(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Ad Label for this AdCreative.

    Args:
        adcreative_id: The ID of the AdCreative.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdCreativeCreateAdLabelParams type.
    """
    return AdCreative(adcreative_id).create_ad_label(fields=fields, params=params)


@adcreative_server.tool
@wrapped_fn_tool
def get_previews(
    adcreative_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Previews for this AdCreative.

    Args:
        adcreative_id: The ID of the AdCreative.
        fields: Fields to retrieve. Available fields: See AdPreviewField type.
        params: Query parameters. Available params: See AdCreativeGetPreviewsParams type.
    """
    return AdCreative(adcreative_id).get_previews(fields=fields, params=params)

"""Streamlined Ad MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.generated.models.ad import AdField, AdUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAd"
instructions = """
Ad MCP Server for Facebook Business API.

Provides typed access to all Ad operations.
"""

ad_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_ad(
    ad_id: str,
    fields: list[AdField] = [],
) -> str:
    """Get a Ad object by ID.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
    """
    obj = Ad(ad_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_ad(
    ad_id: str,
    fields: list[AdField] = [],
    params: AdUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a Ad object.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return Ad(ad_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad(
    ad_id: str,
) -> str:
    """Delete a Ad object.

    Args:
        ad_id: The ID of the Ad.
    """
    return Ad(ad_id).api_delete()


# ---- Edge Methods (7) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.ad_wrappers import (
    create_ad_label,
    create_copy,
    get_ad_rules_governed,
    get_copies,
    get_insights,
    get_insights_async,
    get_previews,
)

# ---- Register tools ----
# Register CRUD operations
ad_server.tool(get_ad)
ad_server.tool(update_ad)
ad_server.tool(delete_ad)

# Register edge methods from wrappers
ad_server.tool(create_ad_label)
ad_server.tool(get_ad_rules_governed)
ad_server.tool(get_copies)
ad_server.tool(create_copy)
ad_server.tool(get_insights)
ad_server.tool(get_insights_async)
ad_server.tool(get_previews)

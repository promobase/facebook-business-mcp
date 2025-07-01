"""Streamlined AdCreative MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.adcreative import AdCreative
from fastmcp import FastMCP

from src.generated.models.adcreative import AdCreativeField, AdCreativeUpdateParams
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
@wrapped_fn_tool
def get_adcreative(
    adcreative_id: str,
    fields: list[AdCreativeField] = [],
) -> str:
    """Get a AdCreative object by ID.

    Args:
        adcreative_id: The ID of the AdCreative.
        fields: Fields to retrieve.
    """
    obj = AdCreative(adcreative_id)
    return obj.api_get(fields=fields)


@wrapped_fn_tool
def update_adcreative(
    adcreative_id: str,
    fields: list[AdCreativeField] = [],
    params: AdCreativeUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdCreative object.

    Args:
        adcreative_id: The ID of the AdCreative.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdCreative(adcreative_id).api_update(fields=fields, params=params)


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
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.adcreative_wrappers import create_ad_label, get_previews

# ---- Register tools ----
# Register CRUD operations
adcreative_server.tool(get_adcreative)
adcreative_server.tool(update_adcreative)
adcreative_server.tool(delete_adcreative)

# Register edge methods from wrappers
adcreative_server.tool(create_ad_label)
adcreative_server.tool(get_previews)

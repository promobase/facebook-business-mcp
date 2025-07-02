"""HomeListing MCP Server."""

from typing import Any

from facebook_business.adobjects.homelisting import HomeListing
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookHomeListing"
instructions = """
HomeListing MCP Server for Facebook Business API.

Provides typed access to all HomeListing operations.
"""

homelisting_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@homelisting_server.tool
@wrapped_fn_tool
def get_homelisting(
    homelisting_id: str,
    fields: list[str] = [],
) -> str:
    obj = HomeListing(homelisting_id)
    return obj.api_get(fields=fields)


@homelisting_server.tool
@wrapped_fn_tool
def update_homelisting(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return HomeListing(homelisting_id).api_update(fields=fields, params=params)


@homelisting_server.tool
@wrapped_fn_tool
def delete_homelisting(
    homelisting_id: str,
) -> str:
    return HomeListing(homelisting_id).api_delete()


# ---- Edge Methods (3) ----
@homelisting_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return HomeListing(homelisting_id).get_channels_to_integrity_status(
        fields=fields, params=params
    )


@homelisting_server.tool
@wrapped_fn_tool
def get_override_details(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return HomeListing(homelisting_id).get_override_details(fields=fields, params=params)


@homelisting_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    homelisting_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return HomeListing(homelisting_id).get_videos_metadata(fields=fields, params=params)

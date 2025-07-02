"""IGMedia MCP Server."""

from typing import Any

from facebook_business.adobjects.igmedia import IGMedia
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGMedia"
instructions = """
IGMedia MCP Server for Facebook Business API.

Provides typed access to all IGMedia operations.
"""

igmedia_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@igmedia_server.tool
@wrapped_fn_tool
def get_igmedia(
    igmedia_id: str,
    fields: list[str] = [],
) -> str:
    obj = IGMedia(igmedia_id)
    return obj.api_get(fields=fields)


@igmedia_server.tool
@wrapped_fn_tool
def update_igmedia(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return IGMedia(igmedia_id).api_update(fields=fields, params=params)


# ---- Edge Methods (12) ----
@igmedia_server.tool
@wrapped_fn_tool
def get_boost_ads_list(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_boost_ads_list(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_branded_content_partner_promote(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_branded_content_partner_promote(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def create_branded_content_partner_promote(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).create_branded_content_partner_promote(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_children(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_children(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_collaborators(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_collaborators(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_comments(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_comments(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def create_comment(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).create_comment(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_insights(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_insights(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def delete_partnership_ad_code(
    igmedia_id: str,
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).delete_partnership_ad_code(params=params)


@igmedia_server.tool
@wrapped_fn_tool
def create_partnership_ad_code(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).create_partnership_ad_code(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def get_product_tags(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).get_product_tags(fields=fields, params=params)


@igmedia_server.tool
@wrapped_fn_tool
def create_product_tag(
    igmedia_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return IGMedia(igmedia_id).create_product_tag(fields=fields, params=params)

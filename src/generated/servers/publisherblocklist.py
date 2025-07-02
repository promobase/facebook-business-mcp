"""PublisherBlockList MCP Server."""

from typing import Any

from facebook_business.adobjects.publisherblocklist import PublisherBlockList
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPublisherBlockList"
instructions = """
PublisherBlockList MCP Server for Facebook Business API.

Provides typed access to all PublisherBlockList operations.
"""

publisherblocklist_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@publisherblocklist_server.tool
@wrapped_fn_tool
def get_publisherblocklist(
    publisherblocklist_id: str,
    fields: list[str] = [],
) -> str:
    obj = PublisherBlockList(publisherblocklist_id)
    return obj.api_get(fields=fields)


@publisherblocklist_server.tool
@wrapped_fn_tool
def update_publisherblocklist(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return PublisherBlockList(publisherblocklist_id).api_update(fields=fields, params=params)


@publisherblocklist_server.tool
@wrapped_fn_tool
def delete_publisherblocklist(
    publisherblocklist_id: str,
) -> str:
    return PublisherBlockList(publisherblocklist_id).api_delete()


# ---- Edge Methods (2) ----
@publisherblocklist_server.tool
@wrapped_fn_tool
def create_append_publisher_url(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PublisherBlockList(publisherblocklist_id).create_append_publisher_url(
        fields=fields, params=params
    )


@publisherblocklist_server.tool
@wrapped_fn_tool
def get_paged_web_publishers(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PublisherBlockList(publisherblocklist_id).get_paged_web_publishers(
        fields=fields, params=params
    )

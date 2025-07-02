"""PageUserMessageThreadLabel MCP Server."""

from typing import Any

from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageUserMessageThreadLabel"
instructions = """
PageUserMessageThreadLabel MCP Server for Facebook Business API.

Provides typed access to all PageUserMessageThreadLabel operations.
"""

pageusermessagethreadlabel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def get_pageusermessagethreadlabel(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
) -> str:
    obj = PageUserMessageThreadLabel(pageusermessagethreadlabel_id)
    return obj.api_get(fields=fields)


@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def delete_pageusermessagethreadlabel(
    pageusermessagethreadlabel_id: str,
) -> str:
    return PageUserMessageThreadLabel(pageusermessagethreadlabel_id).api_delete()


# ---- Edge Methods (2) ----
@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def delete_label(
    pageusermessagethreadlabel_id: str,
    params: dict[str, Any] = {},
):
    return PageUserMessageThreadLabel(pageusermessagethreadlabel_id).delete_label(params=params)


@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def create_label(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return PageUserMessageThreadLabel(pageusermessagethreadlabel_id).create_label(
        fields=fields, params=params
    )

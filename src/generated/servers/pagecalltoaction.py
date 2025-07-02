"""PageCallToAction MCP Server."""

from typing import Any

from facebook_business.adobjects.pagecalltoaction import PageCallToAction
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageCallToAction"
instructions = """
PageCallToAction MCP Server for Facebook Business API.

Provides typed access to all PageCallToAction operations.
"""

pagecalltoaction_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@pagecalltoaction_server.tool
@wrapped_fn_tool
def get_pagecalltoaction(
    pagecalltoaction_id: str,
    fields: list[str] = [],
) -> str:
    obj = PageCallToAction(pagecalltoaction_id)
    return obj.api_get(fields=fields)


@pagecalltoaction_server.tool
@wrapped_fn_tool
def update_pagecalltoaction(
    pagecalltoaction_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return PageCallToAction(pagecalltoaction_id).api_update(fields=fields, params=params)


@pagecalltoaction_server.tool
@wrapped_fn_tool
def delete_pagecalltoaction(
    pagecalltoaction_id: str,
) -> str:
    return PageCallToAction(pagecalltoaction_id).api_delete()

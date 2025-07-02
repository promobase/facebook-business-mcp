"""ClickTrackingTag MCP Server."""

from typing import Any

from facebook_business.adobjects.clicktrackingtag import ClickTrackingTag
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookClickTrackingTag"
instructions = """
ClickTrackingTag MCP Server for Facebook Business API.

Provides typed access to all ClickTrackingTag operations.
"""

clicktrackingtag_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (2) ----
@clicktrackingtag_server.tool
@wrapped_fn_tool
def get_endpoint(
    clicktrackingtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ClickTrackingTag(clicktrackingtag_id).get_endpoint(fields=fields, params=params)


@clicktrackingtag_server.tool
@wrapped_fn_tool
def get_node_path(
    clicktrackingtag_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return ClickTrackingTag(clicktrackingtag_id).get_node_path(fields=fields, params=params)

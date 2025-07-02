"""LocalServiceBusiness MCP Server."""

from typing import Any

from facebook_business.adobjects.localservicebusiness import LocalServiceBusiness
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLocalServiceBusiness"
instructions = """
LocalServiceBusiness MCP Server for Facebook Business API.

Provides typed access to all LocalServiceBusiness operations.
"""

localservicebusiness_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@localservicebusiness_server.tool
@wrapped_fn_tool
def get_localservicebusiness(
    localservicebusiness_id: str,
    fields: list[str] = [],
) -> str:
    obj = LocalServiceBusiness(localservicebusiness_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@localservicebusiness_server.tool
@wrapped_fn_tool
def get_override_details(
    localservicebusiness_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LocalServiceBusiness(localservicebusiness_id).get_override_details(
        fields=fields, params=params
    )

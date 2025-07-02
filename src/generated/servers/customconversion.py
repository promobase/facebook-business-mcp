"""CustomConversion MCP Server."""

from typing import Any

from facebook_business.adobjects.customconversion import CustomConversion
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCustomConversion"
instructions = """
CustomConversion MCP Server for Facebook Business API.

Provides typed access to all CustomConversion operations.
"""

customconversion_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@customconversion_server.tool
@wrapped_fn_tool
def get_customconversion(
    customconversion_id: str,
    fields: list[str] = [],
) -> str:
    obj = CustomConversion(customconversion_id)
    return obj.api_get(fields=fields)


@customconversion_server.tool
@wrapped_fn_tool
def update_customconversion(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return CustomConversion(customconversion_id).api_update(fields=fields, params=params)


@customconversion_server.tool
@wrapped_fn_tool
def delete_customconversion(
    customconversion_id: str,
) -> str:
    return CustomConversion(customconversion_id).api_delete()


# ---- Edge Methods (1) ----
@customconversion_server.tool
@wrapped_fn_tool
def get_stats(
    customconversion_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CustomConversion(customconversion_id).get_stats(fields=fields, params=params)

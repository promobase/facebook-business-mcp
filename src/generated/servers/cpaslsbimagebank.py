"""CPASLsbImageBank MCP Server."""

from typing import Any

from facebook_business.adobjects.cpaslsbimagebank import CPASLsbImageBank
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASLsbImageBank"
instructions = """
CPASLsbImageBank MCP Server for Facebook Business API.

Provides typed access to all CPASLsbImageBank operations.
"""

cpaslsbimagebank_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@cpaslsbimagebank_server.tool
@wrapped_fn_tool
def get_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
) -> str:
    obj = CPASLsbImageBank(cpaslsbimagebank_id)
    return obj.api_get(fields=fields)


@cpaslsbimagebank_server.tool
@wrapped_fn_tool
def update_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return CPASLsbImageBank(cpaslsbimagebank_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@cpaslsbimagebank_server.tool
@wrapped_fn_tool
def get_backup_images(
    cpaslsbimagebank_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return CPASLsbImageBank(cpaslsbimagebank_id).get_backup_images(fields=fields, params=params)

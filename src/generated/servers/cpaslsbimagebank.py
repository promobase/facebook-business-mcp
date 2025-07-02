"""CPASLsbImageBank MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.cpaslsbimagebank import CPASLsbImageBank
from fastmcp import FastMCP

from src.generated.models.cpaslsbimagebank import (
    CPASLsbImageBankField,
    CPASLsbImageBankUpdateParams,
)
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
    fields: list[CPASLsbImageBankField] = [],
) -> str:
    """Get a CPASLsbImageBank object by ID.

    Args:
        cpaslsbimagebank_id: The ID of the CPASLsbImageBank.
        fields: Fields to retrieve. Available fields: See CPASLsbImageBankField type.
    """
    obj = CPASLsbImageBank(cpaslsbimagebank_id)
    return obj.api_get(fields=fields)


@cpaslsbimagebank_server.tool
@wrapped_fn_tool
def update_cpaslsbimagebank(
    cpaslsbimagebank_id: str,
    fields: list[CPASLsbImageBankField] = [],
    params: CPASLsbImageBankUpdateParams | dict = {},
) -> str:
    """Update a CPASLsbImageBank object.

    Args:
        cpaslsbimagebank_id: The ID of the CPASLsbImageBank.
        fields: Fields to return after update. Available fields: See CPASLsbImageBankField type.
        params: Parameters to update. Available params: See CPASLsbImageBankUpdateParams type.
    """
    return CPASLsbImageBank(cpaslsbimagebank_id).api_update(fields=fields, params=params)

"""ExtendedCreditAllocationConfig MCP Server."""

from typing import Any

from facebook_business.adobjects.extendedcreditallocationconfig import (
    ExtendedCreditAllocationConfig,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExtendedCreditAllocationConfig"
instructions = """
ExtendedCreditAllocationConfig MCP Server for Facebook Business API.

Provides typed access to all ExtendedCreditAllocationConfig operations.
"""

extendedcreditallocationconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@extendedcreditallocationconfig_server.tool
@wrapped_fn_tool
def get_extendedcreditallocationconfig(
    extendedcreditallocationconfig_id: str,
    fields: list[str] = [],
) -> str:
    obj = ExtendedCreditAllocationConfig(extendedcreditallocationconfig_id)
    return obj.api_get(fields=fields)


@extendedcreditallocationconfig_server.tool
@wrapped_fn_tool
def update_extendedcreditallocationconfig(
    extendedcreditallocationconfig_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return ExtendedCreditAllocationConfig(extendedcreditallocationconfig_id).api_update(
        fields=fields, params=params
    )


@extendedcreditallocationconfig_server.tool
@wrapped_fn_tool
def delete_extendedcreditallocationconfig(
    extendedcreditallocationconfig_id: str,
) -> str:
    return ExtendedCreditAllocationConfig(extendedcreditallocationconfig_id).api_delete()

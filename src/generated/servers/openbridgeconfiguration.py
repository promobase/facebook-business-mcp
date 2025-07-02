"""OpenBridgeConfiguration MCP Server."""

from typing import Any

from facebook_business.adobjects.openbridgeconfiguration import OpenBridgeConfiguration
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOpenBridgeConfiguration"
instructions = """
OpenBridgeConfiguration MCP Server for Facebook Business API.

Provides typed access to all OpenBridgeConfiguration operations.
"""

openbridgeconfiguration_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@openbridgeconfiguration_server.tool
@wrapped_fn_tool
def get_openbridgeconfiguration(
    openbridgeconfiguration_id: str,
    fields: list[str] = [],
) -> str:
    obj = OpenBridgeConfiguration(openbridgeconfiguration_id)
    return obj.api_get(fields=fields)


@openbridgeconfiguration_server.tool
@wrapped_fn_tool
def update_openbridgeconfiguration(
    openbridgeconfiguration_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return OpenBridgeConfiguration(openbridgeconfiguration_id).api_update(
        fields=fields, params=params
    )


@openbridgeconfiguration_server.tool
@wrapped_fn_tool
def delete_openbridgeconfiguration(
    openbridgeconfiguration_id: str,
) -> str:
    return OpenBridgeConfiguration(openbridgeconfiguration_id).api_delete()

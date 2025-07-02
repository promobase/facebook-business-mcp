"""OpenBridgeConfiguration MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.openbridgeconfiguration import OpenBridgeConfiguration
from fastmcp import FastMCP

from src.generated.models.openbridgeconfiguration import (
    OpenBridgeConfigurationField,
    OpenBridgeConfigurationUpdateParams,
)
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
    fields: list[OpenBridgeConfigurationField] = [],
) -> str:
    """Get a OpenBridgeConfiguration object by ID.

    Args:
        openbridgeconfiguration_id: The ID of the OpenBridgeConfiguration.
        fields: Fields to retrieve. Available fields: See OpenBridgeConfigurationField type.
    """
    obj = OpenBridgeConfiguration(openbridgeconfiguration_id)
    return obj.api_get(fields=fields)


@openbridgeconfiguration_server.tool
@wrapped_fn_tool
def update_openbridgeconfiguration(
    openbridgeconfiguration_id: str,
    fields: list[OpenBridgeConfigurationField] = [],
    params: OpenBridgeConfigurationUpdateParams | dict = {},
) -> str:
    """Update a OpenBridgeConfiguration object.

    Args:
        openbridgeconfiguration_id: The ID of the OpenBridgeConfiguration.
        fields: Fields to return after update. Available fields: See OpenBridgeConfigurationField type.
        params: Parameters to update. Available params: See OpenBridgeConfigurationUpdateParams type.
    """
    return OpenBridgeConfiguration(openbridgeconfiguration_id).api_update(
        fields=fields, params=params
    )


@openbridgeconfiguration_server.tool
@wrapped_fn_tool
def delete_openbridgeconfiguration(
    openbridgeconfiguration_id: str,
) -> str:
    """Delete a OpenBridgeConfiguration object.

    Args:
        openbridgeconfiguration_id: The ID of the OpenBridgeConfiguration.
    """
    return OpenBridgeConfiguration(openbridgeconfiguration_id).api_delete()

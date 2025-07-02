"""SystemUser MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.systemuser import SystemUser
from fastmcp import FastMCP

from src.generated.models.businessassetgroup import BusinessAssetGroupField
from src.generated.models.page import PageField
from src.generated.models.systemuser import (
    SystemUserField,
    SystemUserGetAssignedBusinessAssetGroupsParams,
    SystemUserGetAssignedPagesParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSystemUser"
instructions = """
SystemUser MCP Server for Facebook Business API.

Provides typed access to all SystemUser operations.
"""

systemuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@systemuser_server.tool
@wrapped_fn_tool
def get_systemuser(
    systemuser_id: str,
    fields: list[SystemUserField] = [],
) -> str:
    """Get a SystemUser object by ID.

    Args:
        systemuser_id: The ID of the SystemUser.
        fields: Fields to retrieve. Available fields: See SystemUserField type.
    """
    obj = SystemUser(systemuser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (2) ----
@systemuser_server.tool
@wrapped_fn_tool
def get_assigned_business_asset_groups(
    systemuser_id: str,
    fields: list[BusinessAssetGroupField] = [],
    params: SystemUserGetAssignedBusinessAssetGroupsParams | dict = {},
):
    """Get Assigned Business Asset Groups for this SystemUser.

    Args:
        systemuser_id: The ID of the SystemUser.
        fields: Fields to retrieve. Available fields: See BusinessAssetGroupField type.
        params: Query parameters. Available params: See SystemUserGetAssignedBusinessAssetGroupsParams type.
    """
    return SystemUser(systemuser_id).get_assigned_business_asset_groups(
        fields=fields, params=params
    )


@systemuser_server.tool
@wrapped_fn_tool
def get_assigned_pages(
    systemuser_id: str,
    fields: list[PageField] = [],
    params: SystemUserGetAssignedPagesParams | dict = {},
):
    """Get Assigned Pages for this SystemUser.

    Args:
        systemuser_id: The ID of the SystemUser.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See SystemUserGetAssignedPagesParams type.
    """
    return SystemUser(systemuser_id).get_assigned_pages(fields=fields, params=params)

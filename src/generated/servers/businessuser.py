"""BusinessUser MCP Server with typed wrappers."""

from facebook_business.adobjects.businessuser import BusinessUser
from fastmcp import FastMCP

from src.generated.models.businessassetgroup import BusinessAssetGroupField
from src.generated.models.businessuser import (
    BusinessUserField,
    BusinessUserGetAssignedBusinessAssetGroupsParams,
    BusinessUserGetAssignedPagesParams,
    BusinessUserUpdateParams,
)
from src.generated.models.page import PageField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessUser"
instructions = """
BusinessUser MCP Server for Facebook Business API.

Provides typed access to all BusinessUser operations.
"""

businessuser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@businessuser_server.tool
@wrapped_fn_tool
def get_businessuser(
    businessuser_id: str,
    fields: list[BusinessUserField] = [],
) -> str:
    """Get a BusinessUser object by ID.

    Args:
        businessuser_id: The ID of the BusinessUser.
        fields: Fields to retrieve. Available fields: See BusinessUserField type.
    """
    obj = BusinessUser(businessuser_id)
    return obj.api_get(fields=fields)


@businessuser_server.tool
@wrapped_fn_tool
def update_businessuser(
    businessuser_id: str,
    fields: list[BusinessUserField] = [],
    params: BusinessUserUpdateParams | dict = {},
) -> str:
    """Update a BusinessUser object.

    Args:
        businessuser_id: The ID of the BusinessUser.
        fields: Fields to return after update. Available fields: See BusinessUserField type.
        params: Parameters to update. Available params: See BusinessUserUpdateParams type.
    """
    return BusinessUser(businessuser_id).api_update(fields=fields, params=params)


@businessuser_server.tool
@wrapped_fn_tool
def delete_businessuser(
    businessuser_id: str,
) -> str:
    """Delete a BusinessUser object.

    Args:
        businessuser_id: The ID of the BusinessUser.
    """
    return BusinessUser(businessuser_id).api_delete()


# ---- Edge Methods (2) ----
@businessuser_server.tool
@wrapped_fn_tool
def get_assigned_business_asset_groups(
    businessuser_id: str,
    fields: list[BusinessAssetGroupField] = [],
    params: BusinessUserGetAssignedBusinessAssetGroupsParams | dict = {},
):
    """Get Assigned Business Asset Groups for this BusinessUser.

    Args:
        businessuser_id: The ID of the BusinessUser.
        fields: Fields to retrieve. Available fields: See BusinessAssetGroupField type.
        params: Query parameters. Available params: See BusinessUserGetAssignedBusinessAssetGroupsParams type.
    """
    return BusinessUser(businessuser_id).get_assigned_business_asset_groups(
        fields=fields, params=params
    )


@businessuser_server.tool
@wrapped_fn_tool
def get_assigned_pages(
    businessuser_id: str,
    fields: list[PageField] = [],
    params: BusinessUserGetAssignedPagesParams | dict = {},
):
    """Get Assigned Pages for this BusinessUser.

    Args:
        businessuser_id: The ID of the BusinessUser.
        fields: Fields to retrieve. Available fields: See PageField type.
        params: Query parameters. Available params: See BusinessUserGetAssignedPagesParams type.
    """
    return BusinessUser(businessuser_id).get_assigned_pages(fields=fields, params=params)

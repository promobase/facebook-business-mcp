"""BusinessRoleRequest MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.businessrolerequest import BusinessRoleRequest
from fastmcp import FastMCP

from src.generated.models.businessrolerequest import (
    BusinessRoleRequestField,
    BusinessRoleRequestUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessRoleRequest"
instructions = """
BusinessRoleRequest MCP Server for Facebook Business API.

Provides typed access to all BusinessRoleRequest operations.
"""

businessrolerequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@businessrolerequest_server.tool
@wrapped_fn_tool
def get_businessrolerequest(
    businessrolerequest_id: str,
    fields: list[BusinessRoleRequestField] = [],
) -> str:
    """Get a BusinessRoleRequest object by ID.

    Args:
        businessrolerequest_id: The ID of the BusinessRoleRequest.
        fields: Fields to retrieve. Available fields: See BusinessRoleRequestField type.
    """
    obj = BusinessRoleRequest(businessrolerequest_id)
    return obj.api_get(fields=fields)


@businessrolerequest_server.tool
@wrapped_fn_tool
def update_businessrolerequest(
    businessrolerequest_id: str,
    fields: list[BusinessRoleRequestField] = [],
    params: BusinessRoleRequestUpdateParams | dict = {},
) -> str:
    """Update a BusinessRoleRequest object.

    Args:
        businessrolerequest_id: The ID of the BusinessRoleRequest.
        fields: Fields to return after update. Available fields: See BusinessRoleRequestField type.
        params: Parameters to update. Available params: See BusinessRoleRequestUpdateParams type.
    """
    return BusinessRoleRequest(businessrolerequest_id).api_update(fields=fields, params=params)


@businessrolerequest_server.tool
@wrapped_fn_tool
def delete_businessrolerequest(
    businessrolerequest_id: str,
) -> str:
    """Delete a BusinessRoleRequest object.

    Args:
        businessrolerequest_id: The ID of the BusinessRoleRequest.
    """
    return BusinessRoleRequest(businessrolerequest_id).api_delete()

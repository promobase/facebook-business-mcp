"""BusinessRoleRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.businessrolerequest import BusinessRoleRequest
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = BusinessRoleRequest(businessrolerequest_id)
    return obj.api_get(fields=fields)


@businessrolerequest_server.tool
@wrapped_fn_tool
def update_businessrolerequest(
    businessrolerequest_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return BusinessRoleRequest(businessrolerequest_id).api_update(fields=fields, params=params)


@businessrolerequest_server.tool
@wrapped_fn_tool
def delete_businessrolerequest(
    businessrolerequest_id: str,
) -> str:
    return BusinessRoleRequest(businessrolerequest_id).api_delete()

"""LocalServiceBusiness MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.localservicebusiness import LocalServiceBusiness
from fastmcp import FastMCP

from src.generated.models.localservicebusiness import (
    LocalServiceBusinessField,
    LocalServiceBusinessGetOverrideDetailsParams,
)
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLocalServiceBusiness"
instructions = """
LocalServiceBusiness MCP Server for Facebook Business API.

Provides typed access to all LocalServiceBusiness operations.
"""

localservicebusiness_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@localservicebusiness_server.tool
@wrapped_fn_tool
def get_localservicebusiness(
    localservicebusiness_id: str,
    fields: list[LocalServiceBusinessField] = [],
) -> str:
    """Get a LocalServiceBusiness object by ID.

    Args:
        localservicebusiness_id: The ID of the LocalServiceBusiness.
        fields: Fields to retrieve. Available fields: See LocalServiceBusinessField type.
    """
    obj = LocalServiceBusiness(localservicebusiness_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@localservicebusiness_server.tool
@wrapped_fn_tool
def get_override_details(
    localservicebusiness_id: str,
    fields: list[OverrideDetailsField] = [],
    params: LocalServiceBusinessGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this LocalServiceBusiness.

    Args:
        localservicebusiness_id: The ID of the LocalServiceBusiness.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See LocalServiceBusinessGetOverrideDetailsParams type.
    """
    return LocalServiceBusiness(localservicebusiness_id).get_override_details(
        fields=fields, params=params
    )

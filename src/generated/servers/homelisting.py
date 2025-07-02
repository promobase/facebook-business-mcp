"""HomeListing MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.homelisting import HomeListing
from fastmcp import FastMCP

from src.generated.models.homelisting import (
    HomeListingField,
    HomeListingGetOverrideDetailsParams,
    HomeListingUpdateParams,
)
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookHomeListing"
instructions = """
HomeListing MCP Server for Facebook Business API.

Provides typed access to all HomeListing operations.
"""

homelisting_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@homelisting_server.tool
@wrapped_fn_tool
def get_homelisting(
    homelisting_id: str,
    fields: list[HomeListingField] = [],
) -> str:
    """Get a HomeListing object by ID.

    Args:
        homelisting_id: The ID of the HomeListing.
        fields: Fields to retrieve. Available fields: See HomeListingField type.
    """
    obj = HomeListing(homelisting_id)
    return obj.api_get(fields=fields)


@homelisting_server.tool
@wrapped_fn_tool
def update_homelisting(
    homelisting_id: str,
    fields: list[HomeListingField] = [],
    params: HomeListingUpdateParams | dict = {},
) -> str:
    """Update a HomeListing object.

    Args:
        homelisting_id: The ID of the HomeListing.
        fields: Fields to return after update. Available fields: See HomeListingField type.
        params: Parameters to update. Available params: See HomeListingUpdateParams type.
    """
    return HomeListing(homelisting_id).api_update(fields=fields, params=params)


@homelisting_server.tool
@wrapped_fn_tool
def delete_homelisting(
    homelisting_id: str,
) -> str:
    """Delete a HomeListing object.

    Args:
        homelisting_id: The ID of the HomeListing.
    """
    return HomeListing(homelisting_id).api_delete()


# ---- Edge Methods (1) ----
@homelisting_server.tool
@wrapped_fn_tool
def get_override_details(
    homelisting_id: str,
    fields: list[OverrideDetailsField] = [],
    params: HomeListingGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this HomeListing.

    Args:
        homelisting_id: The ID of the HomeListing.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See HomeListingGetOverrideDetailsParams type.
    """
    return HomeListing(homelisting_id).get_override_details(fields=fields, params=params)

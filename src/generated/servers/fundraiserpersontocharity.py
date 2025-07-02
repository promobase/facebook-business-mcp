"""FundraiserPersonToCharity MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.fundraiserpersontocharity import FundraiserPersonToCharity
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.fundraiserpersontocharity import (
    FundraiserPersonToCharityCreateExternalDonationParams,
    FundraiserPersonToCharityField,
    FundraiserPersonToCharityUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFundraiserPersonToCharity"
instructions = """
FundraiserPersonToCharity MCP Server for Facebook Business API.

Provides typed access to all FundraiserPersonToCharity operations.
"""

fundraiserpersontocharity_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@fundraiserpersontocharity_server.tool
@wrapped_fn_tool
def get_fundraiserpersontocharity(
    fundraiserpersontocharity_id: str,
    fields: list[FundraiserPersonToCharityField] = [],
) -> str:
    """Get a FundraiserPersonToCharity object by ID.

    Args:
        fundraiserpersontocharity_id: The ID of the FundraiserPersonToCharity.
        fields: Fields to retrieve. Available fields: See FundraiserPersonToCharityField type.
    """
    obj = FundraiserPersonToCharity(fundraiserpersontocharity_id)
    return obj.api_get(fields=fields)


@fundraiserpersontocharity_server.tool
@wrapped_fn_tool
def update_fundraiserpersontocharity(
    fundraiserpersontocharity_id: str,
    fields: list[FundraiserPersonToCharityField] = [],
    params: FundraiserPersonToCharityUpdateParams | dict = {},
) -> str:
    """Update a FundraiserPersonToCharity object.

    Args:
        fundraiserpersontocharity_id: The ID of the FundraiserPersonToCharity.
        fields: Fields to return after update. Available fields: See FundraiserPersonToCharityField type.
        params: Parameters to update. Available params: See FundraiserPersonToCharityUpdateParams type.
    """
    return FundraiserPersonToCharity(fundraiserpersontocharity_id).api_update(
        fields=fields, params=params
    )


# ---- Edge Methods (1) ----
@fundraiserpersontocharity_server.tool
@wrapped_fn_tool
def create_external_donation(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: FundraiserPersonToCharityCreateExternalDonationParams | dict = {},
):
    """Create External Donation for this FundraiserPersonToCharity.

    Args:
        fundraiserpersontocharity_id: The ID of the FundraiserPersonToCharity.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See FundraiserPersonToCharityCreateExternalDonationParams type.
    """
    return FundraiserPersonToCharity(fundraiserpersontocharity_id).create_external_donation(
        fields=fields, params=params
    )

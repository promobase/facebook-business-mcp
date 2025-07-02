"""FundraiserPersonToCharity MCP Server."""

from typing import Any

from facebook_business.adobjects.fundraiserpersontocharity import FundraiserPersonToCharity
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = FundraiserPersonToCharity(fundraiserpersontocharity_id)
    return obj.api_get(fields=fields)


@fundraiserpersontocharity_server.tool
@wrapped_fn_tool
def update_fundraiserpersontocharity(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return FundraiserPersonToCharity(fundraiserpersontocharity_id).api_update(
        fields=fields, params=params
    )


# ---- Edge Methods (1) ----
@fundraiserpersontocharity_server.tool
@wrapped_fn_tool
def create_external_donation(
    fundraiserpersontocharity_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return FundraiserPersonToCharity(fundraiserpersontocharity_id).create_external_donation(
        fields=fields, params=params
    )

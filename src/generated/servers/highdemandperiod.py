"""HighDemandPeriod MCP Server with typed wrappers."""

from facebook_business.adobjects.highdemandperiod import HighDemandPeriod
from fastmcp import FastMCP

from src.generated.models.highdemandperiod import (
    HighDemandPeriodField,
    HighDemandPeriodUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookHighDemandPeriod"
instructions = """
HighDemandPeriod MCP Server for Facebook Business API.

Provides typed access to all HighDemandPeriod operations.
"""

highdemandperiod_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@highdemandperiod_server.tool
@wrapped_fn_tool
def get_highdemandperiod(
    highdemandperiod_id: str,
    fields: list[HighDemandPeriodField] = [],
) -> str:
    """Get a HighDemandPeriod object by ID.

    Args:
        highdemandperiod_id: The ID of the HighDemandPeriod.
        fields: Fields to retrieve. Available fields: See HighDemandPeriodField type.
    """
    obj = HighDemandPeriod(highdemandperiod_id)
    return obj.api_get(fields=fields)


@highdemandperiod_server.tool
@wrapped_fn_tool
def update_highdemandperiod(
    highdemandperiod_id: str,
    fields: list[HighDemandPeriodField] = [],
    params: HighDemandPeriodUpdateParams | dict = {},
) -> str:
    """Update a HighDemandPeriod object.

    Args:
        highdemandperiod_id: The ID of the HighDemandPeriod.
        fields: Fields to return after update. Available fields: See HighDemandPeriodField type.
        params: Parameters to update. Available params: See HighDemandPeriodUpdateParams type.
    """
    return HighDemandPeriod(highdemandperiod_id).api_update(fields=fields, params=params)


@highdemandperiod_server.tool
@wrapped_fn_tool
def delete_highdemandperiod(
    highdemandperiod_id: str,
) -> str:
    """Delete a HighDemandPeriod object.

    Args:
        highdemandperiod_id: The ID of the HighDemandPeriod.
    """
    return HighDemandPeriod(highdemandperiod_id).api_delete()

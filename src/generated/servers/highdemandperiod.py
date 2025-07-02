"""HighDemandPeriod MCP Server."""

from typing import Any

from facebook_business.adobjects.highdemandperiod import HighDemandPeriod
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = HighDemandPeriod(highdemandperiod_id)
    return obj.api_get(fields=fields)


@highdemandperiod_server.tool
@wrapped_fn_tool
def update_highdemandperiod(
    highdemandperiod_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return HighDemandPeriod(highdemandperiod_id).api_update(fields=fields, params=params)


@highdemandperiod_server.tool
@wrapped_fn_tool
def delete_highdemandperiod(
    highdemandperiod_id: str,
) -> str:
    return HighDemandPeriod(highdemandperiod_id).api_delete()

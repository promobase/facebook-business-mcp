"""AdsReportBuilderMMMReportScheduler MCP Server."""

from typing import Any

from facebook_business.adobjects.adsreportbuildermmmreportscheduler import (
    AdsReportBuilderMMMReportScheduler,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsReportBuilderMMMReportScheduler"
instructions = """
AdsReportBuilderMMMReportScheduler MCP Server for Facebook Business API.

Provides typed access to all AdsReportBuilderMMMReportScheduler operations.
"""

adsreportbuildermmmreportscheduler_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsreportbuildermmmreportscheduler_server.tool
@wrapped_fn_tool
def get_adsreportbuildermmmreportscheduler(
    adsreportbuildermmmreportscheduler_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsReportBuilderMMMReportScheduler(adsreportbuildermmmreportscheduler_id)
    return obj.api_get(fields=fields)

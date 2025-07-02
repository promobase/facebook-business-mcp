"""AdsReportBuilderMMMReport MCP Server."""

from typing import Any

from facebook_business.adobjects.adsreportbuildermmmreport import AdsReportBuilderMMMReport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsReportBuilderMMMReport"
instructions = """
AdsReportBuilderMMMReport MCP Server for Facebook Business API.

Provides typed access to all AdsReportBuilderMMMReport operations.
"""

adsreportbuildermmmreport_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsreportbuildermmmreport_server.tool
@wrapped_fn_tool
def get_adsreportbuildermmmreport(
    adsreportbuildermmmreport_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsReportBuilderMMMReport(adsreportbuildermmmreport_id)
    return obj.api_get(fields=fields)

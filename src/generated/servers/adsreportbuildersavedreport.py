"""AdsReportBuilderSavedReport MCP Server."""

from typing import Any

from facebook_business.adobjects.adsreportbuildersavedreport import AdsReportBuilderSavedReport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsReportBuilderSavedReport"
instructions = """
AdsReportBuilderSavedReport MCP Server for Facebook Business API.

Provides typed access to all AdsReportBuilderSavedReport operations.
"""

adsreportbuildersavedreport_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsreportbuildersavedreport_server.tool
@wrapped_fn_tool
def get_adsreportbuildersavedreport(
    adsreportbuildersavedreport_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsReportBuilderSavedReport(adsreportbuildersavedreport_id)
    return obj.api_get(fields=fields)

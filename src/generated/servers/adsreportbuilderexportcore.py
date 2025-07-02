"""AdsReportBuilderExportCore MCP Server."""

from typing import Any

from facebook_business.adobjects.adsreportbuilderexportcore import AdsReportBuilderExportCore
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsReportBuilderExportCore"
instructions = """
AdsReportBuilderExportCore MCP Server for Facebook Business API.

Provides typed access to all AdsReportBuilderExportCore operations.
"""

adsreportbuilderexportcore_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsreportbuilderexportcore_server.tool
@wrapped_fn_tool
def get_adsreportbuilderexportcore(
    adsreportbuilderexportcore_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsReportBuilderExportCore(adsreportbuilderexportcore_id)
    return obj.api_get(fields=fields)

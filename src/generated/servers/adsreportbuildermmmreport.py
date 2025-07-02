"""AdsReportBuilderMMMReport MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adsreportbuildermmmreport import AdsReportBuilderMMMReport
from fastmcp import FastMCP

from src.generated.models.adsreportbuildermmmreport import AdsReportBuilderMMMReportField
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
    fields: list[AdsReportBuilderMMMReportField] = [],
) -> str:
    """Get a AdsReportBuilderMMMReport object by ID.

    Args:
        adsreportbuildermmmreport_id: The ID of the AdsReportBuilderMMMReport.
        fields: Fields to retrieve. Available fields: See AdsReportBuilderMMMReportField type.
    """
    obj = AdsReportBuilderMMMReport(adsreportbuildermmmreport_id)
    return obj.api_get(fields=fields)

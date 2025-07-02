"""AdsReportBuilderMMMReportScheduler MCP Server with typed wrappers."""

from facebook_business.adobjects.adsreportbuildermmmreportscheduler import (
    AdsReportBuilderMMMReportScheduler,
)
from fastmcp import FastMCP

from src.generated.models.adsreportbuildermmmreportscheduler import (
    AdsReportBuilderMMMReportSchedulerField,
)
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
    fields: list[AdsReportBuilderMMMReportSchedulerField] = [],
) -> str:
    """Get a AdsReportBuilderMMMReportScheduler object by ID.

    Args:
        adsreportbuildermmmreportscheduler_id: The ID of the AdsReportBuilderMMMReportScheduler.
        fields: Fields to retrieve. Available fields: See AdsReportBuilderMMMReportSchedulerField type.
    """
    obj = AdsReportBuilderMMMReportScheduler(adsreportbuildermmmreportscheduler_id)
    return obj.api_get(fields=fields)

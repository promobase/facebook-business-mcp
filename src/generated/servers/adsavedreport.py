"""AdSavedReport MCP Server with typed wrappers."""

from facebook_business.adobjects.adsavedreport import AdSavedReport
from fastmcp import FastMCP

from src.generated.models.adsavedreport import AdSavedReportField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSavedReport"
instructions = """
AdSavedReport MCP Server for Facebook Business API.

Provides typed access to all AdSavedReport operations.
"""

adsavedreport_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsavedreport_server.tool
@wrapped_fn_tool
def get_adsavedreport(
    adsavedreport_id: str,
    fields: list[AdSavedReportField] = [],
) -> str:
    """Get a AdSavedReport object by ID.

    Args:
        adsavedreport_id: The ID of the AdSavedReport.
        fields: Fields to retrieve. Available fields: See AdSavedReportField type.
    """
    obj = AdSavedReport(adsavedreport_id)
    return obj.api_get(fields=fields)

"""AdReportRun MCP Server with typed wrappers."""

from facebook_business.adobjects.adreportrun import AdReportRun
from fastmcp import FastMCP

from src.generated.models.adreportrun import AdReportRunField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdReportRun"
instructions = """
AdReportRun MCP Server for Facebook Business API.

Provides typed access to all AdReportRun operations.
"""

adreportrun_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adreportrun_server.tool
@wrapped_fn_tool
def get_adreportrun(
    adreportrun_id: str,
    fields: list[AdReportRunField] = [],
) -> str:
    """Get a AdReportRun object by ID.

    Args:
        adreportrun_id: The ID of the AdReportRun.
        fields: Fields to retrieve. Available fields: See AdReportRunField type.
    """
    obj = AdReportRun(adreportrun_id)
    return obj.api_get(fields=fields)

"""PageInsightsAsyncExportRun MCP Server with typed wrappers."""

from facebook_business.adobjects.pageinsightsasyncexportrun import PageInsightsAsyncExportRun
from fastmcp import FastMCP

from src.generated.models.pageinsightsasyncexportrun import PageInsightsAsyncExportRunField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageInsightsAsyncExportRun"
instructions = """
PageInsightsAsyncExportRun MCP Server for Facebook Business API.

Provides typed access to all PageInsightsAsyncExportRun operations.
"""

pageinsightsasyncexportrun_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@pageinsightsasyncexportrun_server.tool
@wrapped_fn_tool
def get_pageinsightsasyncexportrun(
    pageinsightsasyncexportrun_id: str,
    fields: list[PageInsightsAsyncExportRunField] = [],
) -> str:
    """Get a PageInsightsAsyncExportRun object by ID.

    Args:
        pageinsightsasyncexportrun_id: The ID of the PageInsightsAsyncExportRun.
        fields: Fields to retrieve. Available fields: See PageInsightsAsyncExportRunField type.
    """
    obj = PageInsightsAsyncExportRun(pageinsightsasyncexportrun_id)
    return obj.api_get(fields=fields)

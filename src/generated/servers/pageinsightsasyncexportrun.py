"""PageInsightsAsyncExportRun MCP Server."""

from typing import Any

from facebook_business.adobjects.pageinsightsasyncexportrun import PageInsightsAsyncExportRun
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = PageInsightsAsyncExportRun(pageinsightsasyncexportrun_id)
    return obj.api_get(fields=fields)

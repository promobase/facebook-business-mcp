"""AnalyticsSegment MCP Server."""

from typing import Any

from facebook_business.adobjects.analyticssegment import AnalyticsSegment
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAnalyticsSegment"
instructions = """
AnalyticsSegment MCP Server for Facebook Business API.

Provides typed access to all AnalyticsSegment operations.
"""

analyticssegment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@analyticssegment_server.tool
@wrapped_fn_tool
def get_analyticssegment(
    analyticssegment_id: str,
    fields: list[str] = [],
) -> str:
    obj = AnalyticsSegment(analyticssegment_id)
    return obj.api_get(fields=fields)

"""AdCustomDerivedMetrics MCP Server."""

from typing import Any

from facebook_business.adobjects.adcustomderivedmetrics import AdCustomDerivedMetrics
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdCustomDerivedMetrics"
instructions = """
AdCustomDerivedMetrics MCP Server for Facebook Business API.

Provides typed access to all AdCustomDerivedMetrics operations.
"""

adcustomderivedmetrics_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adcustomderivedmetrics_server.tool
@wrapped_fn_tool
def get_adcustomderivedmetrics(
    adcustomderivedmetrics_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdCustomDerivedMetrics(adcustomderivedmetrics_id)
    return obj.api_get(fields=fields)

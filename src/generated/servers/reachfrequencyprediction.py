"""ReachFrequencyPrediction MCP Server."""

from typing import Any

from facebook_business.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookReachFrequencyPrediction"
instructions = """
ReachFrequencyPrediction MCP Server for Facebook Business API.

Provides typed access to all ReachFrequencyPrediction operations.
"""

reachfrequencyprediction_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@reachfrequencyprediction_server.tool
@wrapped_fn_tool
def get_reachfrequencyprediction(
    reachfrequencyprediction_id: str,
    fields: list[str] = [],
) -> str:
    obj = ReachFrequencyPrediction(reachfrequencyprediction_id)
    return obj.api_get(fields=fields)

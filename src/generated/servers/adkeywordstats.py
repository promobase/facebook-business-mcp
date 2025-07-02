"""AdKeywordStats MCP Server."""

from typing import Any

from facebook_business.adobjects.adkeywordstats import AdKeywordStats
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdKeywordStats"
instructions = """
AdKeywordStats MCP Server for Facebook Business API.

Provides typed access to all AdKeywordStats operations.
"""

adkeywordstats_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adkeywordstats_server.tool
@wrapped_fn_tool
def get_endpoint(
    adkeywordstats_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdKeywordStats(adkeywordstats_id).get_endpoint(fields=fields, params=params)

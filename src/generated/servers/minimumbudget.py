"""MinimumBudget MCP Server."""

from typing import Any

from facebook_business.adobjects.minimumbudget import MinimumBudget
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMinimumBudget"
instructions = """
MinimumBudget MCP Server for Facebook Business API.

Provides typed access to all MinimumBudget operations.
"""

minimumbudget_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@minimumbudget_server.tool
@wrapped_fn_tool
def get_endpoint(
    minimumbudget_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return MinimumBudget(minimumbudget_id).get_endpoint(fields=fields, params=params)

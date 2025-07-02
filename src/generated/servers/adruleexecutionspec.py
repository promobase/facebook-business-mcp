"""AdRuleExecutionSpec MCP Server."""

from typing import Any

from facebook_business.adobjects.adruleexecutionspec import AdRuleExecutionSpec
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdRuleExecutionSpec"
instructions = """
AdRuleExecutionSpec MCP Server for Facebook Business API.

Provides typed access to all AdRuleExecutionSpec operations.
"""

adruleexecutionspec_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adruleexecutionspec_server.tool
@wrapped_fn_tool
def get_adruleexecutionspec(
    adruleexecutionspec_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdRuleExecutionSpec(adruleexecutionspec_id)
    return obj.api_get(fields=fields)

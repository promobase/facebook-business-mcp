"""BizInboxOffsiteEmailAccount MCP Server."""

from typing import Any

from facebook_business.adobjects.bizinboxoffsiteemailaccount import BizInboxOffsiteEmailAccount
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBizInboxOffsiteEmailAccount"
instructions = """
BizInboxOffsiteEmailAccount MCP Server for Facebook Business API.

Provides typed access to all BizInboxOffsiteEmailAccount operations.
"""

bizinboxoffsiteemailaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@bizinboxoffsiteemailaccount_server.tool
@wrapped_fn_tool
def get_bizinboxoffsiteemailaccount(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[str] = [],
) -> str:
    obj = BizInboxOffsiteEmailAccount(bizinboxoffsiteemailaccount_id)
    return obj.api_get(fields=fields)

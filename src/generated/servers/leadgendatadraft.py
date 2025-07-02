"""LeadGenDataDraft MCP Server."""

from typing import Any

from facebook_business.adobjects.leadgendatadraft import LeadGenDataDraft
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLeadGenDataDraft"
instructions = """
LeadGenDataDraft MCP Server for Facebook Business API.

Provides typed access to all LeadGenDataDraft operations.
"""

leadgendatadraft_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@leadgendatadraft_server.tool
@wrapped_fn_tool
def get_leadgendatadraft(
    leadgendatadraft_id: str,
    fields: list[str] = [],
) -> str:
    obj = LeadGenDataDraft(leadgendatadraft_id)
    return obj.api_get(fields=fields)

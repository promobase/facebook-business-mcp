"""ResearchPollStudy MCP Server."""

from typing import Any

from facebook_business.adobjects.researchpollstudy import ResearchPollStudy
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookResearchPollStudy"
instructions = """
ResearchPollStudy MCP Server for Facebook Business API.

Provides typed access to all ResearchPollStudy operations.
"""

researchpollstudy_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@researchpollstudy_server.tool
@wrapped_fn_tool
def get_researchpollstudy(
    researchpollstudy_id: str,
    fields: list[str] = [],
) -> str:
    obj = ResearchPollStudy(researchpollstudy_id)
    return obj.api_get(fields=fields)

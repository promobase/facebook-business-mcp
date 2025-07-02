"""AdStudyObjective MCP Server."""

from typing import Any

from facebook_business.adobjects.adstudyobjective import AdStudyObjective
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdStudyObjective"
instructions = """
AdStudyObjective MCP Server for Facebook Business API.

Provides typed access to all AdStudyObjective operations.
"""

adstudyobjective_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adstudyobjective_server.tool
@wrapped_fn_tool
def get_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdStudyObjective(adstudyobjective_id)
    return obj.api_get(fields=fields)


@adstudyobjective_server.tool
@wrapped_fn_tool
def update_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdStudyObjective(adstudyobjective_id).api_update(fields=fields, params=params)

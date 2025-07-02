"""WorkSkill MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.workskill import WorkSkill
from fastmcp import FastMCP

from src.generated.models.workskill import WorkSkillField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWorkSkill"
instructions = """
WorkSkill MCP Server for Facebook Business API.

Provides typed access to all WorkSkill operations.
"""

workskill_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@workskill_server.tool
@wrapped_fn_tool
def get_workskill(
    workskill_id: str,
    fields: list[WorkSkillField] = [],
) -> str:
    """Get a WorkSkill object by ID.

    Args:
        workskill_id: The ID of the WorkSkill.
        fields: Fields to retrieve. Available fields: See WorkSkillField type.
    """
    obj = WorkSkill(workskill_id)
    return obj.api_get(fields=fields)

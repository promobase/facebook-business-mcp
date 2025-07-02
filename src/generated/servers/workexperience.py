"""WorkExperience MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.workexperience import WorkExperience
from fastmcp import FastMCP

from src.generated.models.workexperience import WorkExperienceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWorkExperience"
instructions = """
WorkExperience MCP Server for Facebook Business API.

Provides typed access to all WorkExperience operations.
"""

workexperience_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@workexperience_server.tool
@wrapped_fn_tool
def get_workexperience(
    workexperience_id: str,
    fields: list[WorkExperienceField] = [],
) -> str:
    """Get a WorkExperience object by ID.

    Args:
        workexperience_id: The ID of the WorkExperience.
        fields: Fields to retrieve. Available fields: See WorkExperienceField type.
    """
    obj = WorkExperience(workexperience_id)
    return obj.api_get(fields=fields)

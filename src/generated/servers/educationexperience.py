"""EducationExperience MCP Server."""

from typing import Any

from facebook_business.adobjects.educationexperience import EducationExperience
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookEducationExperience"
instructions = """
EducationExperience MCP Server for Facebook Business API.

Provides typed access to all EducationExperience operations.
"""

educationexperience_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@educationexperience_server.tool
@wrapped_fn_tool
def get_educationexperience(
    educationexperience_id: str,
    fields: list[str] = [],
) -> str:
    obj = EducationExperience(educationexperience_id)
    return obj.api_get(fields=fields)

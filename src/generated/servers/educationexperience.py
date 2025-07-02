"""EducationExperience MCP Server with typed wrappers."""

from facebook_business.adobjects.educationexperience import EducationExperience
from fastmcp import FastMCP

from src.generated.models.educationexperience import EducationExperienceField
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
    fields: list[EducationExperienceField] = [],
) -> str:
    """Get a EducationExperience object by ID.

    Args:
        educationexperience_id: The ID of the EducationExperience.
        fields: Fields to retrieve. Available fields: See EducationExperienceField type.
    """
    obj = EducationExperience(educationexperience_id)
    return obj.api_get(fields=fields)

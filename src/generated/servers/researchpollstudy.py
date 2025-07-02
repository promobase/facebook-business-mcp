"""ResearchPollStudy MCP Server with typed wrappers."""

from facebook_business.adobjects.researchpollstudy import ResearchPollStudy
from fastmcp import FastMCP

from src.generated.models.researchpollstudy import ResearchPollStudyField
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
    fields: list[ResearchPollStudyField] = [],
) -> str:
    """Get a ResearchPollStudy object by ID.

    Args:
        researchpollstudy_id: The ID of the ResearchPollStudy.
        fields: Fields to retrieve. Available fields: See ResearchPollStudyField type.
    """
    obj = ResearchPollStudy(researchpollstudy_id)
    return obj.api_get(fields=fields)

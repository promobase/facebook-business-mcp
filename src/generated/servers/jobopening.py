"""JobOpening MCP Server with typed wrappers."""

from facebook_business.adobjects.jobopening import JobOpening
from fastmcp import FastMCP

from src.generated.models.jobopening import JobOpeningField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookJobOpening"
instructions = """
JobOpening MCP Server for Facebook Business API.

Provides typed access to all JobOpening operations.
"""

jobopening_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@jobopening_server.tool
@wrapped_fn_tool
def get_jobopening(
    jobopening_id: str,
    fields: list[JobOpeningField] = [],
) -> str:
    """Get a JobOpening object by ID.

    Args:
        jobopening_id: The ID of the JobOpening.
        fields: Fields to retrieve. Available fields: See JobOpeningField type.
    """
    obj = JobOpening(jobopening_id)
    return obj.api_get(fields=fields)

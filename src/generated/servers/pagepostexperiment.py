"""PagePostExperiment MCP Server with typed wrappers."""

from facebook_business.adobjects.pagepostexperiment import PagePostExperiment
from fastmcp import FastMCP

from src.generated.models.pagepostexperiment import PagePostExperimentField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPagePostExperiment"
instructions = """
PagePostExperiment MCP Server for Facebook Business API.

Provides typed access to all PagePostExperiment operations.
"""

pagepostexperiment_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@pagepostexperiment_server.tool
@wrapped_fn_tool
def get_pagepostexperiment(
    pagepostexperiment_id: str,
    fields: list[PagePostExperimentField] = [],
) -> str:
    """Get a PagePostExperiment object by ID.

    Args:
        pagepostexperiment_id: The ID of the PagePostExperiment.
        fields: Fields to retrieve. Available fields: See PagePostExperimentField type.
    """
    obj = PagePostExperiment(pagepostexperiment_id)
    return obj.api_get(fields=fields)


@pagepostexperiment_server.tool
@wrapped_fn_tool
def delete_pagepostexperiment(
    pagepostexperiment_id: str,
) -> str:
    """Delete a PagePostExperiment object.

    Args:
        pagepostexperiment_id: The ID of the PagePostExperiment.
    """
    return PagePostExperiment(pagepostexperiment_id).api_delete()

"""AdStudyObjective MCP Server with typed wrappers."""

from facebook_business.adobjects.adstudyobjective import AdStudyObjective
from fastmcp import FastMCP

from src.generated.models.adstudyobjective import (
    AdStudyObjectiveField,
    AdStudyObjectiveUpdateParams,
)
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
    fields: list[AdStudyObjectiveField] = [],
) -> str:
    """Get a AdStudyObjective object by ID.

    Args:
        adstudyobjective_id: The ID of the AdStudyObjective.
        fields: Fields to retrieve. Available fields: See AdStudyObjectiveField type.
    """
    obj = AdStudyObjective(adstudyobjective_id)
    return obj.api_get(fields=fields)


@adstudyobjective_server.tool
@wrapped_fn_tool
def update_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[AdStudyObjectiveField] = [],
    params: AdStudyObjectiveUpdateParams | dict = {},
) -> str:
    """Update a AdStudyObjective object.

    Args:
        adstudyobjective_id: The ID of the AdStudyObjective.
        fields: Fields to return after update. Available fields: See AdStudyObjectiveField type.
        params: Parameters to update. Available params: See AdStudyObjectiveUpdateParams type.
    """
    return AdStudyObjective(adstudyobjective_id).api_update(fields=fields, params=params)

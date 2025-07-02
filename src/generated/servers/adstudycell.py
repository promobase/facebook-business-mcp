"""AdStudyCell MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adstudycell import AdStudyCell
from fastmcp import FastMCP

from src.generated.models.adstudycell import AdStudyCellField, AdStudyCellUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdStudyCell"
instructions = """
AdStudyCell MCP Server for Facebook Business API.

Provides typed access to all AdStudyCell operations.
"""

adstudycell_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adstudycell_server.tool
@wrapped_fn_tool
def get_adstudycell(
    adstudycell_id: str,
    fields: list[AdStudyCellField] = [],
) -> str:
    """Get a AdStudyCell object by ID.

    Args:
        adstudycell_id: The ID of the AdStudyCell.
        fields: Fields to retrieve. Available fields: See AdStudyCellField type.
    """
    obj = AdStudyCell(adstudycell_id)
    return obj.api_get(fields=fields)


@adstudycell_server.tool
@wrapped_fn_tool
def update_adstudycell(
    adstudycell_id: str,
    fields: list[AdStudyCellField] = [],
    params: AdStudyCellUpdateParams | dict = {},
) -> str:
    """Update a AdStudyCell object.

    Args:
        adstudycell_id: The ID of the AdStudyCell.
        fields: Fields to return after update. Available fields: See AdStudyCellField type.
        params: Parameters to update. Available params: See AdStudyCellUpdateParams type.
    """
    return AdStudyCell(adstudycell_id).api_update(fields=fields, params=params)

"""AdLabel MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adlabel import AdLabel
from fastmcp import FastMCP

from src.generated.models.adlabel import AdLabelField, AdLabelUpdateParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdLabel"
instructions = """
AdLabel MCP Server for Facebook Business API.

Provides typed access to all AdLabel operations.
"""

adlabel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adlabel_server.tool
@wrapped_fn_tool
def get_adlabel(
    adlabel_id: str,
    fields: list[AdLabelField] = [],
) -> str:
    """Get a AdLabel object by ID.

    Args:
        adlabel_id: The ID of the AdLabel.
        fields: Fields to retrieve. Available fields: See AdLabelField type.
    """
    obj = AdLabel(adlabel_id)
    return obj.api_get(fields=fields)


@adlabel_server.tool
@wrapped_fn_tool
def update_adlabel(
    adlabel_id: str,
    fields: list[AdLabelField] = [],
    params: AdLabelUpdateParams | dict = {},
) -> str:
    """Update a AdLabel object.

    Args:
        adlabel_id: The ID of the AdLabel.
        fields: Fields to return after update. Available fields: See AdLabelField type.
        params: Parameters to update. Available params: See AdLabelUpdateParams type.
    """
    return AdLabel(adlabel_id).api_update(fields=fields, params=params)


@adlabel_server.tool
@wrapped_fn_tool
def delete_adlabel(
    adlabel_id: str,
) -> str:
    """Delete a AdLabel object.

    Args:
        adlabel_id: The ID of the AdLabel.
    """
    return AdLabel(adlabel_id).api_delete()

"""PageCallToAction MCP Server with typed wrappers."""

from facebook_business.adobjects.pagecalltoaction import PageCallToAction
from fastmcp import FastMCP

from src.generated.models.pagecalltoaction import (
    PageCallToActionField,
    PageCallToActionUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageCallToAction"
instructions = """
PageCallToAction MCP Server for Facebook Business API.

Provides typed access to all PageCallToAction operations.
"""

pagecalltoaction_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@pagecalltoaction_server.tool
@wrapped_fn_tool
def get_pagecalltoaction(
    pagecalltoaction_id: str,
    fields: list[PageCallToActionField] = [],
) -> str:
    """Get a PageCallToAction object by ID.

    Args:
        pagecalltoaction_id: The ID of the PageCallToAction.
        fields: Fields to retrieve. Available fields: See PageCallToActionField type.
    """
    obj = PageCallToAction(pagecalltoaction_id)
    return obj.api_get(fields=fields)


@pagecalltoaction_server.tool
@wrapped_fn_tool
def update_pagecalltoaction(
    pagecalltoaction_id: str,
    fields: list[PageCallToActionField] = [],
    params: PageCallToActionUpdateParams | dict = {},
) -> str:
    """Update a PageCallToAction object.

    Args:
        pagecalltoaction_id: The ID of the PageCallToAction.
        fields: Fields to return after update. Available fields: See PageCallToActionField type.
        params: Parameters to update. Available params: See PageCallToActionUpdateParams type.
    """
    return PageCallToAction(pagecalltoaction_id).api_update(fields=fields, params=params)


@pagecalltoaction_server.tool
@wrapped_fn_tool
def delete_pagecalltoaction(
    pagecalltoaction_id: str,
) -> str:
    """Delete a PageCallToAction object.

    Args:
        pagecalltoaction_id: The ID of the PageCallToAction.
    """
    return PageCallToAction(pagecalltoaction_id).api_delete()

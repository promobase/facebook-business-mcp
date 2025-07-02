"""PageUserMessageThreadLabel MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.pageusermessagethreadlabel import (
    PageUserMessageThreadLabelCreateLabelParams,
    PageUserMessageThreadLabelDeleteLabelParams,
    PageUserMessageThreadLabelField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPageUserMessageThreadLabel"
instructions = """
PageUserMessageThreadLabel MCP Server for Facebook Business API.

Provides typed access to all PageUserMessageThreadLabel operations.
"""

pageusermessagethreadlabel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def get_pageusermessagethreadlabel(
    pageusermessagethreadlabel_id: str,
    fields: list[PageUserMessageThreadLabelField] = [],
) -> str:
    """Get a PageUserMessageThreadLabel object by ID.

    Args:
        pageusermessagethreadlabel_id: The ID of the PageUserMessageThreadLabel.
        fields: Fields to retrieve. Available fields: See PageUserMessageThreadLabelField type.
    """
    obj = PageUserMessageThreadLabel(pageusermessagethreadlabel_id)
    return obj.api_get(fields=fields)


@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def delete_pageusermessagethreadlabel(
    pageusermessagethreadlabel_id: str,
) -> str:
    """Delete a PageUserMessageThreadLabel object.

    Args:
        pageusermessagethreadlabel_id: The ID of the PageUserMessageThreadLabel.
    """
    return PageUserMessageThreadLabel(pageusermessagethreadlabel_id).api_delete()


# ---- Edge Methods (2) ----
@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def delete_label(
    pageusermessagethreadlabel_id: str,
    params: PageUserMessageThreadLabelDeleteLabelParams | dict = {},
):
    """Delete Label for this PageUserMessageThreadLabel.

    Args:
        pageusermessagethreadlabel_id: The ID of the PageUserMessageThreadLabel.
        params: Query parameters. Available params: See PageUserMessageThreadLabelDeleteLabelParams type.
    """
    return PageUserMessageThreadLabel(pageusermessagethreadlabel_id).delete_label(params=params)


@pageusermessagethreadlabel_server.tool
@wrapped_fn_tool
def create_label(
    pageusermessagethreadlabel_id: str,
    fields: list[str] = [],
    params: PageUserMessageThreadLabelCreateLabelParams | dict = {},
):
    """Create Label for this PageUserMessageThreadLabel.

    Args:
        pageusermessagethreadlabel_id: The ID of the PageUserMessageThreadLabel.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PageUserMessageThreadLabelCreateLabelParams type.
    """
    return PageUserMessageThreadLabel(pageusermessagethreadlabel_id).create_label(
        fields=fields, params=params
    )

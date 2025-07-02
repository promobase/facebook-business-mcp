"""PublisherBlockList MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.publisherblocklist import PublisherBlockList
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.publisherblocklist import (
    PublisherBlockListCreateAppendPublisherUrlParams,
    PublisherBlockListField,
    PublisherBlockListGetPagedWebPublishersParams,
    PublisherBlockListUpdateParams,
)
from src.generated.models.webpublisher import WebPublisherField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPublisherBlockList"
instructions = """
PublisherBlockList MCP Server for Facebook Business API.

Provides typed access to all PublisherBlockList operations.
"""

publisherblocklist_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@publisherblocklist_server.tool
@wrapped_fn_tool
def get_publisherblocklist(
    publisherblocklist_id: str,
    fields: list[PublisherBlockListField] = [],
) -> str:
    """Get a PublisherBlockList object by ID.

    Args:
        publisherblocklist_id: The ID of the PublisherBlockList.
        fields: Fields to retrieve. Available fields: See PublisherBlockListField type.
    """
    obj = PublisherBlockList(publisherblocklist_id)
    return obj.api_get(fields=fields)


@publisherblocklist_server.tool
@wrapped_fn_tool
def update_publisherblocklist(
    publisherblocklist_id: str,
    fields: list[PublisherBlockListField] = [],
    params: PublisherBlockListUpdateParams | dict = {},
) -> str:
    """Update a PublisherBlockList object.

    Args:
        publisherblocklist_id: The ID of the PublisherBlockList.
        fields: Fields to return after update. Available fields: See PublisherBlockListField type.
        params: Parameters to update. Available params: See PublisherBlockListUpdateParams type.
    """
    return PublisherBlockList(publisherblocklist_id).api_update(fields=fields, params=params)


@publisherblocklist_server.tool
@wrapped_fn_tool
def delete_publisherblocklist(
    publisherblocklist_id: str,
) -> str:
    """Delete a PublisherBlockList object.

    Args:
        publisherblocklist_id: The ID of the PublisherBlockList.
    """
    return PublisherBlockList(publisherblocklist_id).api_delete()


# ---- Edge Methods (2) ----
@publisherblocklist_server.tool
@wrapped_fn_tool
def create_append_publisher_url(
    publisherblocklist_id: str,
    fields: list[str] = [],
    params: PublisherBlockListCreateAppendPublisherUrlParams | dict = {},
):
    """Create Append Publisher Url for this PublisherBlockList.

    Args:
        publisherblocklist_id: The ID of the PublisherBlockList.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See PublisherBlockListCreateAppendPublisherUrlParams type.
    """
    return PublisherBlockList(publisherblocklist_id).create_append_publisher_url(
        fields=fields, params=params
    )


@publisherblocklist_server.tool
@wrapped_fn_tool
def get_paged_web_publishers(
    publisherblocklist_id: str,
    fields: list[WebPublisherField] = [],
    params: PublisherBlockListGetPagedWebPublishersParams | dict = {},
):
    """Get Paged Web Publishers for this PublisherBlockList.

    Args:
        publisherblocklist_id: The ID of the PublisherBlockList.
        fields: Fields to retrieve. Available fields: See WebPublisherField type.
        params: Query parameters. Available params: See PublisherBlockListGetPagedWebPublishersParams type.
    """
    return PublisherBlockList(publisherblocklist_id).get_paged_web_publishers(
        fields=fields, params=params
    )

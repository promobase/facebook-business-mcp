"""Streamlined IGUser MCP Server - Core Operations Only."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.iguser import IGUser
from fastmcp import FastMCP

from src.generated.models.iguser import IGUserField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUser"
instructions = """
IGUser MCP Server for Facebook Business API.

Provides typed access to all IGUser operations.
"""

iguser_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@wrapped_fn_tool
def get_iguser(
    iguser_id: str,
    fields: list[IGUserField] = [],
) -> str:
    """Get a IGUser object by ID.

    Args:
        iguser_id: The ID of the IGUser.
        fields: Fields to retrieve.
    """
    obj = IGUser(iguser_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (20) ----
# Import and register wrapper functions from generated wrappers
from src.generated.wrappers.iguser_wrappers import (
    create_authorized_ad_account,
    create_branded_content_ad_permission,
    create_branded_content_tag_approval,
    create_dataset,
    create_media,
    create_media_publish,
    create_mention,
    create_product_appeal,
    create_upcoming_event,
    delete_branded_content_tag_approval,
    get_authorized_ad_accounts,
    get_branded_content_advertisable_medias,
    get_branded_content_tag_approval,
    get_catalog_product_search,
    get_content_publishing_limit,
    get_insights,
    get_live_media,
    get_media,
    get_product_appeal,
    get_welcome_message_flows,
)

# ---- Register tools ----
# Register CRUD operations
iguser_server.tool(get_iguser)

# Register edge methods from wrappers
iguser_server.tool(get_authorized_ad_accounts)
iguser_server.tool(create_authorized_ad_account)
iguser_server.tool(create_branded_content_ad_permission)
iguser_server.tool(get_branded_content_advertisable_medias)
iguser_server.tool(delete_branded_content_tag_approval)
iguser_server.tool(get_branded_content_tag_approval)
iguser_server.tool(create_branded_content_tag_approval)
iguser_server.tool(get_catalog_product_search)
iguser_server.tool(get_content_publishing_limit)
iguser_server.tool(create_dataset)
iguser_server.tool(get_insights)
iguser_server.tool(get_live_media)
iguser_server.tool(get_media)
iguser_server.tool(create_media)
iguser_server.tool(create_media_publish)
iguser_server.tool(create_mention)
iguser_server.tool(get_product_appeal)
iguser_server.tool(create_product_appeal)
iguser_server.tool(create_upcoming_event)
iguser_server.tool(get_welcome_message_flows)

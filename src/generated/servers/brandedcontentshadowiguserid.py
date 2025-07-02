"""
Auto-generated MCP server for Facebook BrandedContentShadowIGUserID.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.brandedcontentshadowiguserid import BrandedContentShadowIGUserID
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-brandedcontentshadowiguserid")


# CRUD Operations


@mcp.tool()
async def api_create_brandedcontentshadowiguserid(
    brandedcontentshadowiguserid_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BrandedContentShadowIGUserID(fbid=brandedcontentshadowiguserid_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_brandedcontentshadowiguserid(
    brandedcontentshadowiguserid_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BrandedContentShadowIGUserID(fbid=brandedcontentshadowiguserid_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_brandedcontentshadowiguserid(
    brandedcontentshadowiguserid_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BrandedContentShadowIGUserID(fbid=brandedcontentshadowiguserid_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_brandedcontentshadowiguserid(
    brandedcontentshadowiguserid_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = BrandedContentShadowIGUserID(fbid=brandedcontentshadowiguserid_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
brandedcontentshadowiguserid_server = mcp

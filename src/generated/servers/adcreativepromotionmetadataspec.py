"""
Auto-generated MCP server for Facebook AdCreativePromotionMetadataSpec.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcreativepromotionmetadataspec import (
    AdCreativePromotionMetadataSpec,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcreativepromotionmetadataspec")


# CRUD Operations


@mcp.tool()
async def create_adcreativepromotionmetadataspec(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativePromotionMetadataSpec(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_adcreativepromotionmetadataspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativePromotionMetadataSpec(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adcreativepromotionmetadataspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativePromotionMetadataSpec(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adcreativepromotionmetadataspec(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativePromotionMetadataSpec(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreativepromotionmetadataspec_server = mcp

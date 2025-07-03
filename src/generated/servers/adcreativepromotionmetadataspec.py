"""
Auto-generated MCP server for Facebook AdCreativePromotionMetadataSpec.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcreativepromotionmetadataspec import (
    AdCreativePromotionMetadataSpec,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-adcreativepromotionmetadataspec")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    adcreativepromotionmetadataspec_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCreativePromotionMetadataSpec(fbid=adcreativepromotionmetadataspec_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    adcreativepromotionmetadataspec_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCreativePromotionMetadataSpec(fbid=adcreativepromotionmetadataspec_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    adcreativepromotionmetadataspec_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCreativePromotionMetadataSpec(fbid=adcreativepromotionmetadataspec_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    adcreativepromotionmetadataspec_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AdCreativePromotionMetadataSpec(fbid=adcreativepromotionmetadataspec_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreativepromotionmetadataspec_server = mcp

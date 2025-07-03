"""
Auto-generated MCP server for Facebook BusinessAssetSharingAgreement.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.businessassetsharingagreement import BusinessAssetSharingAgreement
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-businessassetsharingagreement")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    businessassetsharingagreement_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessAssetSharingAgreement(fbid=businessassetsharingagreement_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    businessassetsharingagreement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessAssetSharingAgreement(fbid=businessassetsharingagreement_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    businessassetsharingagreement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessAssetSharingAgreement(fbid=businessassetsharingagreement_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    businessassetsharingagreement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = BusinessAssetSharingAgreement(fbid=businessassetsharingagreement_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
businessassetsharingagreement_server = mcp

"""
Auto-generated MCP server for Facebook ProductDeliveryPreference.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.productdeliverypreference import ProductDeliveryPreference
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-productdeliverypreference")


# CRUD Operations


@mcp.tool()
async def create_productdeliverypreference(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductDeliveryPreference(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_productdeliverypreference(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductDeliveryPreference(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_productdeliverypreference(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductDeliveryPreference(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_productdeliverypreference(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ProductDeliveryPreference(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
productdeliverypreference_server = mcp

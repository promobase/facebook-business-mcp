"""
Auto-generated MCP server for Facebook AppRequestFormerRecipient.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.apprequestformerrecipient import AppRequestFormerRecipient
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-apprequestformerrecipient")


# CRUD Operations


@mcp.tool()
async def create_apprequestformerrecipient(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequestFormerRecipient(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_apprequestformerrecipient(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequestFormerRecipient(fbid=object_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_apprequestformerrecipient(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequestFormerRecipient(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_apprequestformerrecipient(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AppRequestFormerRecipient(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
apprequestformerrecipient_server = mcp

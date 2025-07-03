"""
Auto-generated MCP server for Facebook AppRequestFormerRecipient.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.apprequestformerrecipient import AppRequestFormerRecipient
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-apprequestformerrecipient")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    apprequestformerrecipient_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppRequestFormerRecipient(fbid=apprequestformerrecipient_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    apprequestformerrecipient_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppRequestFormerRecipient(fbid=apprequestformerrecipient_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    apprequestformerrecipient_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppRequestFormerRecipient(fbid=apprequestformerrecipient_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    apprequestformerrecipient_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = AppRequestFormerRecipient(fbid=apprequestformerrecipient_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
apprequestformerrecipient_server = mcp

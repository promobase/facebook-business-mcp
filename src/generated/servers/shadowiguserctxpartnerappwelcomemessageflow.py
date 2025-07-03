"""
Auto-generated MCP server for Facebook ShadowIGUserCTXPartnerAppWelcomeMessageFlow.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowiguserctxpartnerappwelcomemessageflow import (
    ShadowIGUserCTXPartnerAppWelcomeMessageFlow,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowiguserctxpartnerappwelcomemessageflow")


# CRUD Operations


@mcp.tool()
@wrapped_fn_tool
async def api_create(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_delete(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_get(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
@wrapped_fn_tool
async def api_update(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> Any:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowiguserctxpartnerappwelcomemessageflow_server = mcp

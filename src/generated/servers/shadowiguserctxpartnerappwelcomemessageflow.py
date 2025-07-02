"""
Auto-generated MCP server for Facebook ShadowIGUserCTXPartnerAppWelcomeMessageFlow.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.shadowiguserctxpartnerappwelcomemessageflow import (
    ShadowIGUserCTXPartnerAppWelcomeMessageFlow,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-shadowiguserctxpartnerappwelcomemessageflow")


# CRUD Operations


@mcp.tool()
async def api_create_shadowiguserctxpartnerappwelcomemessageflow(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_shadowiguserctxpartnerappwelcomemessageflow(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_shadowiguserctxpartnerappwelcomemessageflow(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_shadowiguserctxpartnerappwelcomemessageflow(
    shadowiguserctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ShadowIGUserCTXPartnerAppWelcomeMessageFlow(
        fbid=shadowiguserctxpartnerappwelcomemessageflow_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
shadowiguserctxpartnerappwelcomemessageflow_server = mcp

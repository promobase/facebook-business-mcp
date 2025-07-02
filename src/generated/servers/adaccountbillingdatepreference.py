"""
Auto-generated MCP server for Facebook AdAccountBillingDatePreference.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adaccountbillingdatepreference import (
    AdAccountBillingDatePreference,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adaccountbillingdatepreference")


# CRUD Operations


@mcp.tool()
async def api_create_adaccountbillingdatepreference(
    adaccountbillingdatepreference_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountBillingDatePreference(fbid=adaccountbillingdatepreference_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adaccountbillingdatepreference(
    adaccountbillingdatepreference_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountBillingDatePreference(fbid=adaccountbillingdatepreference_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adaccountbillingdatepreference(
    adaccountbillingdatepreference_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountBillingDatePreference(fbid=adaccountbillingdatepreference_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adaccountbillingdatepreference(
    adaccountbillingdatepreference_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdAccountBillingDatePreference(fbid=adaccountbillingdatepreference_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adaccountbillingdatepreference_server = mcp

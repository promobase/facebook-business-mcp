"""
Auto-generated MCP server for Facebook AdCreativeLinkDataMoment.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adcreativelinkdatamoment import AdCreativeLinkDataMoment
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adcreativelinkdatamoment")


# CRUD Operations


@mcp.tool()
async def api_create_adcreativelinkdatamoment(
    adcreativelinkdatamoment_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativeLinkDataMoment(fbid=adcreativelinkdatamoment_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_adcreativelinkdatamoment(
    adcreativelinkdatamoment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativeLinkDataMoment(fbid=adcreativelinkdatamoment_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_adcreativelinkdatamoment(
    adcreativelinkdatamoment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativeLinkDataMoment(fbid=adcreativelinkdatamoment_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_adcreativelinkdatamoment(
    adcreativelinkdatamoment_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = AdCreativeLinkDataMoment(fbid=adcreativelinkdatamoment_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adcreativelinkdatamoment_server = mcp

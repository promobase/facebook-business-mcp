"""
Auto-generated MCP server for Facebook ThirdPartyMeasurementReportDataset.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartymeasurementreportdataset import (
    ThirdPartyMeasurementReportDataset,
)
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartymeasurementreportdataset")


# CRUD Operations


@mcp.tool()
async def api_create_thirdpartymeasurementreportdataset(
    thirdpartymeasurementreportdataset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyMeasurementReportDataset(
        fbid=thirdpartymeasurementreportdataset_id
    ).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_thirdpartymeasurementreportdataset(
    thirdpartymeasurementreportdataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyMeasurementReportDataset(
        fbid=thirdpartymeasurementreportdataset_id
    ).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_thirdpartymeasurementreportdataset(
    thirdpartymeasurementreportdataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyMeasurementReportDataset(fbid=thirdpartymeasurementreportdataset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_thirdpartymeasurementreportdataset(
    thirdpartymeasurementreportdataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = ThirdPartyMeasurementReportDataset(
        fbid=thirdpartymeasurementreportdataset_id
    ).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartymeasurementreportdataset_server = mcp

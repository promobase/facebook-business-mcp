"""ThirdPartyMeasurementReportDataset MCP Server."""

from typing import Any

from facebook_business.adobjects.thirdpartymeasurementreportdataset import (
    ThirdPartyMeasurementReportDataset,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookThirdPartyMeasurementReportDataset"
instructions = """
ThirdPartyMeasurementReportDataset MCP Server for Facebook Business API.

Provides typed access to all ThirdPartyMeasurementReportDataset operations.
"""

thirdpartymeasurementreportdataset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@thirdpartymeasurementreportdataset_server.tool
@wrapped_fn_tool
def get_thirdpartymeasurementreportdataset(
    thirdpartymeasurementreportdataset_id: str,
    fields: list[str] = [],
) -> str:
    obj = ThirdPartyMeasurementReportDataset(thirdpartymeasurementreportdataset_id)
    return obj.api_get(fields=fields)

"""MeasurementReport MCP Server."""

from typing import Any

from facebook_business.adobjects.measurementreport import MeasurementReport
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookMeasurementReport"
instructions = """
MeasurementReport MCP Server for Facebook Business API.

Provides typed access to all MeasurementReport operations.
"""

measurementreport_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@measurementreport_server.tool
@wrapped_fn_tool
def get_measurementreport(
    measurementreport_id: str,
    fields: list[str] = [],
) -> str:
    obj = MeasurementReport(measurementreport_id)
    return obj.api_get(fields=fields)

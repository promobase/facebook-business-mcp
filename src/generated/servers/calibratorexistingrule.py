"""CalibratorExistingRule MCP Server."""

from typing import Any

from facebook_business.adobjects.calibratorexistingrule import CalibratorExistingRule
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCalibratorExistingRule"
instructions = """
CalibratorExistingRule MCP Server for Facebook Business API.

Provides typed access to all CalibratorExistingRule operations.
"""

calibratorexistingrule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@calibratorexistingrule_server.tool
@wrapped_fn_tool
def get_calibratorexistingrule(
    calibratorexistingrule_id: str,
    fields: list[str] = [],
) -> str:
    obj = CalibratorExistingRule(calibratorexistingrule_id)
    return obj.api_get(fields=fields)

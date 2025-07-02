"""ChinaBusinessOnboardingVettingRequest MCP Server."""

from typing import Any

from facebook_business.adobjects.chinabusinessonboardingvettingrequest import (
    ChinaBusinessOnboardingVettingRequest,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookChinaBusinessOnboardingVettingRequest"
instructions = """
ChinaBusinessOnboardingVettingRequest MCP Server for Facebook Business API.

Provides typed access to all ChinaBusinessOnboardingVettingRequest operations.
"""

chinabusinessonboardingvettingrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@chinabusinessonboardingvettingrequest_server.tool
@wrapped_fn_tool
def get_chinabusinessonboardingvettingrequest(
    chinabusinessonboardingvettingrequest_id: str,
    fields: list[str] = [],
) -> str:
    obj = ChinaBusinessOnboardingVettingRequest(chinabusinessonboardingvettingrequest_id)
    return obj.api_get(fields=fields)

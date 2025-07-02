"""TargetingSentenceLine MCP Server."""

from typing import Any

from facebook_business.adobjects.targetingsentenceline import TargetingSentenceLine
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookTargetingSentenceLine"
instructions = """
TargetingSentenceLine MCP Server for Facebook Business API.

Provides typed access to all TargetingSentenceLine operations.
"""

targetingsentenceline_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@targetingsentenceline_server.tool
@wrapped_fn_tool
def get_endpoint(
    targetingsentenceline_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return TargetingSentenceLine(targetingsentenceline_id).get_endpoint(
        fields=fields, params=params
    )

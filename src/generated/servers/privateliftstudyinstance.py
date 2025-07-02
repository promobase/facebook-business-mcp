"""PrivateLiftStudyInstance MCP Server."""

from typing import Any

from facebook_business.adobjects.privateliftstudyinstance import PrivateLiftStudyInstance
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPrivateLiftStudyInstance"
instructions = """
PrivateLiftStudyInstance MCP Server for Facebook Business API.

Provides typed access to all PrivateLiftStudyInstance operations.
"""

privateliftstudyinstance_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@privateliftstudyinstance_server.tool
@wrapped_fn_tool
def get_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[str] = [],
) -> str:
    obj = PrivateLiftStudyInstance(privateliftstudyinstance_id)
    return obj.api_get(fields=fields)


@privateliftstudyinstance_server.tool
@wrapped_fn_tool
def update_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return PrivateLiftStudyInstance(privateliftstudyinstance_id).api_update(
        fields=fields, params=params
    )

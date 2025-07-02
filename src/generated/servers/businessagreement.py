"""BusinessAgreement MCP Server."""

from typing import Any

from facebook_business.adobjects.businessagreement import BusinessAgreement
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessAgreement"
instructions = """
BusinessAgreement MCP Server for Facebook Business API.

Provides typed access to all BusinessAgreement operations.
"""

businessagreement_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@businessagreement_server.tool
@wrapped_fn_tool
def get_businessagreement(
    businessagreement_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessAgreement(businessagreement_id)
    return obj.api_get(fields=fields)


@businessagreement_server.tool
@wrapped_fn_tool
def update_businessagreement(
    businessagreement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return BusinessAgreement(businessagreement_id).api_update(fields=fields, params=params)

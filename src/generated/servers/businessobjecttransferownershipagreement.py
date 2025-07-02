"""BusinessObjectTransferOwnershipAgreement MCP Server."""

from typing import Any

from facebook_business.adobjects.businessobjecttransferownershipagreement import (
    BusinessObjectTransferOwnershipAgreement,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessObjectTransferOwnershipAgreement"
instructions = """
BusinessObjectTransferOwnershipAgreement MCP Server for Facebook Business API.

Provides typed access to all BusinessObjectTransferOwnershipAgreement operations.
"""

businessobjecttransferownershipagreement_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@businessobjecttransferownershipagreement_server.tool
@wrapped_fn_tool
def get_businessobjecttransferownershipagreement(
    businessobjecttransferownershipagreement_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessObjectTransferOwnershipAgreement(businessobjecttransferownershipagreement_id)
    return obj.api_get(fields=fields)

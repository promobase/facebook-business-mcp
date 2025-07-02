"""BusinessAssetSharingAgreement MCP Server."""

from typing import Any

from facebook_business.adobjects.businessassetsharingagreement import BusinessAssetSharingAgreement
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessAssetSharingAgreement"
instructions = """
BusinessAssetSharingAgreement MCP Server for Facebook Business API.

Provides typed access to all BusinessAssetSharingAgreement operations.
"""

businessassetsharingagreement_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@businessassetsharingagreement_server.tool
@wrapped_fn_tool
def get_businessassetsharingagreement(
    businessassetsharingagreement_id: str,
    fields: list[str] = [],
) -> str:
    obj = BusinessAssetSharingAgreement(businessassetsharingagreement_id)
    return obj.api_get(fields=fields)


@businessassetsharingagreement_server.tool
@wrapped_fn_tool
def update_businessassetsharingagreement(
    businessassetsharingagreement_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return BusinessAssetSharingAgreement(businessassetsharingagreement_id).api_update(
        fields=fields, params=params
    )

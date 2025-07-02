"""BusinessAssetSharingAgreement MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.businessassetsharingagreement import BusinessAssetSharingAgreement
from fastmcp import FastMCP

from src.generated.models.businessassetsharingagreement import (
    BusinessAssetSharingAgreementField,
    BusinessAssetSharingAgreementUpdateParams,
)
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
    fields: list[BusinessAssetSharingAgreementField] = [],
) -> str:
    """Get a BusinessAssetSharingAgreement object by ID.

    Args:
        businessassetsharingagreement_id: The ID of the BusinessAssetSharingAgreement.
        fields: Fields to retrieve. Available fields: See BusinessAssetSharingAgreementField type.
    """
    obj = BusinessAssetSharingAgreement(businessassetsharingagreement_id)
    return obj.api_get(fields=fields)


@businessassetsharingagreement_server.tool
@wrapped_fn_tool
def update_businessassetsharingagreement(
    businessassetsharingagreement_id: str,
    fields: list[BusinessAssetSharingAgreementField] = [],
    params: BusinessAssetSharingAgreementUpdateParams | dict = {},
) -> str:
    """Update a BusinessAssetSharingAgreement object.

    Args:
        businessassetsharingagreement_id: The ID of the BusinessAssetSharingAgreement.
        fields: Fields to return after update. Available fields: See BusinessAssetSharingAgreementField type.
        params: Parameters to update. Available params: See BusinessAssetSharingAgreementUpdateParams type.
    """
    return BusinessAssetSharingAgreement(businessassetsharingagreement_id).api_update(
        fields=fields, params=params
    )

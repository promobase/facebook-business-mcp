"""BusinessAgreement MCP Server with typed wrappers."""

from facebook_business.adobjects.businessagreement import BusinessAgreement
from fastmcp import FastMCP

from src.generated.models.businessagreement import (
    BusinessAgreementField,
    BusinessAgreementUpdateParams,
)
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
    fields: list[BusinessAgreementField] = [],
) -> str:
    """Get a BusinessAgreement object by ID.

    Args:
        businessagreement_id: The ID of the BusinessAgreement.
        fields: Fields to retrieve. Available fields: See BusinessAgreementField type.
    """
    obj = BusinessAgreement(businessagreement_id)
    return obj.api_get(fields=fields)


@businessagreement_server.tool
@wrapped_fn_tool
def update_businessagreement(
    businessagreement_id: str,
    fields: list[BusinessAgreementField] = [],
    params: BusinessAgreementUpdateParams | dict = {},
) -> str:
    """Update a BusinessAgreement object.

    Args:
        businessagreement_id: The ID of the BusinessAgreement.
        fields: Fields to return after update. Available fields: See BusinessAgreementField type.
        params: Parameters to update. Available params: See BusinessAgreementUpdateParams type.
    """
    return BusinessAgreement(businessagreement_id).api_update(fields=fields, params=params)

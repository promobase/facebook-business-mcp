"""BusinessObjectTransferOwnershipAgreement MCP Server with typed wrappers."""

from facebook_business.adobjects.businessobjecttransferownershipagreement import (
    BusinessObjectTransferOwnershipAgreement,
)
from fastmcp import FastMCP

from src.generated.models.businessobjecttransferownershipagreement import (
    BusinessObjectTransferOwnershipAgreementField,
)
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
    fields: list[BusinessObjectTransferOwnershipAgreementField] = [],
) -> str:
    """Get a BusinessObjectTransferOwnershipAgreement object by ID.

    Args:
        businessobjecttransferownershipagreement_id: The ID of the BusinessObjectTransferOwnershipAgreement.
        fields: Fields to retrieve. Available fields: See BusinessObjectTransferOwnershipAgreementField type.
    """
    obj = BusinessObjectTransferOwnershipAgreement(businessobjecttransferownershipagreement_id)
    return obj.api_get(fields=fields)

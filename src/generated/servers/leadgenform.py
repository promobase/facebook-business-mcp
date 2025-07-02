"""LeadgenForm MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.leadgenform import LeadgenForm
from fastmcp import FastMCP

from src.generated.models.lead import LeadField
from src.generated.models.leadgenform import (
    LeadgenFormCreateTestLeadParams,
    LeadgenFormField,
    LeadgenFormUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLeadgenForm"
instructions = """
LeadgenForm MCP Server for Facebook Business API.

Provides typed access to all LeadgenForm operations.
"""

leadgenform_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@leadgenform_server.tool
@wrapped_fn_tool
def get_leadgenform(
    leadgenform_id: str,
    fields: list[LeadgenFormField] = [],
) -> str:
    """Get a LeadgenForm object by ID.

    Args:
        leadgenform_id: The ID of the LeadgenForm.
        fields: Fields to retrieve. Available fields: See LeadgenFormField type.
    """
    obj = LeadgenForm(leadgenform_id)
    return obj.api_get(fields=fields)


@leadgenform_server.tool
@wrapped_fn_tool
def update_leadgenform(
    leadgenform_id: str,
    fields: list[LeadgenFormField] = [],
    params: LeadgenFormUpdateParams | dict = {},
) -> str:
    """Update a LeadgenForm object.

    Args:
        leadgenform_id: The ID of the LeadgenForm.
        fields: Fields to return after update. Available fields: See LeadgenFormField type.
        params: Parameters to update. Available params: See LeadgenFormUpdateParams type.
    """
    return LeadgenForm(leadgenform_id).api_update(fields=fields, params=params)


# ---- Edge Methods (1) ----
@leadgenform_server.tool
@wrapped_fn_tool
def create_test_lead(
    leadgenform_id: str,
    fields: list[str] = [],
    params: LeadgenFormCreateTestLeadParams | dict = {},
):
    """Create Test Lead for this LeadgenForm.

    Args:
        leadgenform_id: The ID of the LeadgenForm.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See LeadgenFormCreateTestLeadParams type.
    """
    return LeadgenForm(leadgenform_id).create_test_lead(fields=fields, params=params)

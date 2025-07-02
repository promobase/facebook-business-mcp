"""LeadgenForm MCP Server."""

from typing import Any

from facebook_business.adobjects.leadgenform import LeadgenForm
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = LeadgenForm(leadgenform_id)
    return obj.api_get(fields=fields)


@leadgenform_server.tool
@wrapped_fn_tool
def update_leadgenform(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return LeadgenForm(leadgenform_id).api_update(fields=fields, params=params)


# ---- Edge Methods (3) ----
@leadgenform_server.tool
@wrapped_fn_tool
def get_leads(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LeadgenForm(leadgenform_id).get_leads(fields=fields, params=params)


@leadgenform_server.tool
@wrapped_fn_tool
def get_test_leads(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LeadgenForm(leadgenform_id).get_test_leads(fields=fields, params=params)


@leadgenform_server.tool
@wrapped_fn_tool
def create_test_lead(
    leadgenform_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return LeadgenForm(leadgenform_id).create_test_lead(fields=fields, params=params)

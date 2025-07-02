"""CTXPartnerAppWelcomeMessageFlow MCP Server."""

from typing import Any

from facebook_business.adobjects.ctxpartnerappwelcomemessageflow import (
    CTXPartnerAppWelcomeMessageFlow,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCTXPartnerAppWelcomeMessageFlow"
instructions = """
CTXPartnerAppWelcomeMessageFlow MCP Server for Facebook Business API.

Provides typed access to all CTXPartnerAppWelcomeMessageFlow operations.
"""

ctxpartnerappwelcomemessageflow_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@ctxpartnerappwelcomemessageflow_server.tool
@wrapped_fn_tool
def get_ctxpartnerappwelcomemessageflow(
    ctxpartnerappwelcomemessageflow_id: str,
    fields: list[str] = [],
) -> str:
    obj = CTXPartnerAppWelcomeMessageFlow(ctxpartnerappwelcomemessageflow_id)
    return obj.api_get(fields=fields)

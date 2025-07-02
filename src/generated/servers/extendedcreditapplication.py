"""ExtendedCreditApplication MCP Server."""

from typing import Any

from facebook_business.adobjects.extendedcreditapplication import ExtendedCreditApplication
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExtendedCreditApplication"
instructions = """
ExtendedCreditApplication MCP Server for Facebook Business API.

Provides typed access to all ExtendedCreditApplication operations.
"""

extendedcreditapplication_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@extendedcreditapplication_server.tool
@wrapped_fn_tool
def get_extendedcreditapplication(
    extendedcreditapplication_id: str,
    fields: list[str] = [],
) -> str:
    obj = ExtendedCreditApplication(extendedcreditapplication_id)
    return obj.api_get(fields=fields)

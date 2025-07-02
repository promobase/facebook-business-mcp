"""AdsNamingTemplate MCP Server."""

from typing import Any

from facebook_business.adobjects.adsnamingtemplate import AdsNamingTemplate
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsNamingTemplate"
instructions = """
AdsNamingTemplate MCP Server for Facebook Business API.

Provides typed access to all AdsNamingTemplate operations.
"""

adsnamingtemplate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsnamingtemplate_server.tool
@wrapped_fn_tool
def get_adsnamingtemplate(
    adsnamingtemplate_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsNamingTemplate(adsnamingtemplate_id)
    return obj.api_get(fields=fields)

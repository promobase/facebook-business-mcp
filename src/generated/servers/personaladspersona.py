"""PersonalAdsPersona MCP Server."""

from typing import Any

from facebook_business.adobjects.personaladspersona import PersonalAdsPersona
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPersonalAdsPersona"
instructions = """
PersonalAdsPersona MCP Server for Facebook Business API.

Provides typed access to all PersonalAdsPersona operations.
"""

personaladspersona_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@personaladspersona_server.tool
@wrapped_fn_tool
def get_personaladspersona(
    personaladspersona_id: str,
    fields: list[str] = [],
) -> str:
    obj = PersonalAdsPersona(personaladspersona_id)
    return obj.api_get(fields=fields)

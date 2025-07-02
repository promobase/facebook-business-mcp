"""Persona MCP Server."""

from typing import Any

from facebook_business.adobjects.persona import Persona
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPersona"
instructions = """
Persona MCP Server for Facebook Business API.

Provides typed access to all Persona operations.
"""

persona_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@persona_server.tool
@wrapped_fn_tool
def get_persona(
    persona_id: str,
    fields: list[str] = [],
) -> str:
    obj = Persona(persona_id)
    return obj.api_get(fields=fields)


@persona_server.tool
@wrapped_fn_tool
def delete_persona(
    persona_id: str,
) -> str:
    return Persona(persona_id).api_delete()

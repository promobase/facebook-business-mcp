"""Persona MCP Server with typed wrappers."""

from facebook_business.adobjects.persona import Persona
from fastmcp import FastMCP

from src.generated.models.persona import PersonaField
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
    fields: list[PersonaField] = [],
) -> str:
    """Get a Persona object by ID.

    Args:
        persona_id: The ID of the Persona.
        fields: Fields to retrieve. Available fields: See PersonaField type.
    """
    obj = Persona(persona_id)
    return obj.api_get(fields=fields)


@persona_server.tool
@wrapped_fn_tool
def delete_persona(
    persona_id: str,
) -> str:
    """Delete a Persona object.

    Args:
        persona_id: The ID of the Persona.
    """
    return Persona(persona_id).api_delete()

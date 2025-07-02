"""CPASAdCreationTemplate MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.cpasadcreationtemplate import CPASAdCreationTemplate
from fastmcp import FastMCP

from src.generated.models.cpasadcreationtemplate import CPASAdCreationTemplateField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASAdCreationTemplate"
instructions = """
CPASAdCreationTemplate MCP Server for Facebook Business API.

Provides typed access to all CPASAdCreationTemplate operations.
"""

cpasadcreationtemplate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpasadcreationtemplate_server.tool
@wrapped_fn_tool
def get_cpasadcreationtemplate(
    cpasadcreationtemplate_id: str,
    fields: list[CPASAdCreationTemplateField] = [],
) -> str:
    """Get a CPASAdCreationTemplate object by ID.

    Args:
        cpasadcreationtemplate_id: The ID of the CPASAdCreationTemplate.
        fields: Fields to retrieve. Available fields: See CPASAdCreationTemplateField type.
    """
    obj = CPASAdCreationTemplate(cpasadcreationtemplate_id)
    return obj.api_get(fields=fields)

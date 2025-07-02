"""FAMEKumo MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.famekumo import FAMEKumo
from fastmcp import FastMCP

from src.generated.models.famekumo import FAMEKumoField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookFAMEKumo"
instructions = """
FAMEKumo MCP Server for Facebook Business API.

Provides typed access to all FAMEKumo operations.
"""

famekumo_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@famekumo_server.tool
@wrapped_fn_tool
def get_famekumo(
    famekumo_id: str,
    fields: list[FAMEKumoField] = [],
) -> str:
    """Get a FAMEKumo object by ID.

    Args:
        famekumo_id: The ID of the FAMEKumo.
        fields: Fields to retrieve. Available fields: See FAMEKumoField type.
    """
    obj = FAMEKumo(famekumo_id)
    return obj.api_get(fields=fields)

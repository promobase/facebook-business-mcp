"""PrivateLiftStudyInstance MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.privateliftstudyinstance import PrivateLiftStudyInstance
from fastmcp import FastMCP

from src.generated.models.privateliftstudyinstance import (
    PrivateLiftStudyInstanceField,
    PrivateLiftStudyInstanceUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPrivateLiftStudyInstance"
instructions = """
PrivateLiftStudyInstance MCP Server for Facebook Business API.

Provides typed access to all PrivateLiftStudyInstance operations.
"""

privateliftstudyinstance_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@privateliftstudyinstance_server.tool
@wrapped_fn_tool
def get_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[PrivateLiftStudyInstanceField] = [],
) -> str:
    """Get a PrivateLiftStudyInstance object by ID.

    Args:
        privateliftstudyinstance_id: The ID of the PrivateLiftStudyInstance.
        fields: Fields to retrieve. Available fields: See PrivateLiftStudyInstanceField type.
    """
    obj = PrivateLiftStudyInstance(privateliftstudyinstance_id)
    return obj.api_get(fields=fields)


@privateliftstudyinstance_server.tool
@wrapped_fn_tool
def update_privateliftstudyinstance(
    privateliftstudyinstance_id: str,
    fields: list[PrivateLiftStudyInstanceField] = [],
    params: PrivateLiftStudyInstanceUpdateParams | dict = {},
) -> str:
    """Update a PrivateLiftStudyInstance object.

    Args:
        privateliftstudyinstance_id: The ID of the PrivateLiftStudyInstance.
        fields: Fields to return after update. Available fields: See PrivateLiftStudyInstanceField type.
        params: Parameters to update. Available params: See PrivateLiftStudyInstanceUpdateParams type.
    """
    return PrivateLiftStudyInstance(privateliftstudyinstance_id).api_update(
        fields=fields, params=params
    )

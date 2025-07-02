"""AdToplineDetail MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adtoplinedetail import AdToplineDetail
from fastmcp import FastMCP

from src.generated.models.adtoplinedetail import AdToplineDetailField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdToplineDetail"
instructions = """
AdToplineDetail MCP Server for Facebook Business API.

Provides typed access to all AdToplineDetail operations.
"""

adtoplinedetail_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adtoplinedetail_server.tool
@wrapped_fn_tool
def get_adtoplinedetail(
    adtoplinedetail_id: str,
    fields: list[AdToplineDetailField] = [],
) -> str:
    """Get a AdToplineDetail object by ID.

    Args:
        adtoplinedetail_id: The ID of the AdToplineDetail.
        fields: Fields to retrieve. Available fields: See AdToplineDetailField type.
    """
    obj = AdToplineDetail(adtoplinedetail_id)
    return obj.api_get(fields=fields)

"""ArAdsDataContainer MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.aradsdatacontainer import ArAdsDataContainer
from fastmcp import FastMCP

from src.generated.models.aradsdatacontainer import ArAdsDataContainerField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookArAdsDataContainer"
instructions = """
ArAdsDataContainer MCP Server for Facebook Business API.

Provides typed access to all ArAdsDataContainer operations.
"""

aradsdatacontainer_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@aradsdatacontainer_server.tool
@wrapped_fn_tool
def get_aradsdatacontainer(
    aradsdatacontainer_id: str,
    fields: list[ArAdsDataContainerField] = [],
) -> str:
    """Get a ArAdsDataContainer object by ID.

    Args:
        aradsdatacontainer_id: The ID of the ArAdsDataContainer.
        fields: Fields to retrieve. Available fields: See ArAdsDataContainerField type.
    """
    obj = ArAdsDataContainer(aradsdatacontainer_id)
    return obj.api_get(fields=fields)

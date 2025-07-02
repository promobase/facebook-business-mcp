"""ChinaBusinessOnboardingVettingRequest MCP Server with typed wrappers."""

from facebook_business.adobjects.chinabusinessonboardingvettingrequest import (
    ChinaBusinessOnboardingVettingRequest,
)
from fastmcp import FastMCP

from src.generated.models.chinabusinessonboardingvettingrequest import (
    ChinaBusinessOnboardingVettingRequestField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookChinaBusinessOnboardingVettingRequest"
instructions = """
ChinaBusinessOnboardingVettingRequest MCP Server for Facebook Business API.

Provides typed access to all ChinaBusinessOnboardingVettingRequest operations.
"""

chinabusinessonboardingvettingrequest_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@chinabusinessonboardingvettingrequest_server.tool
@wrapped_fn_tool
def get_chinabusinessonboardingvettingrequest(
    chinabusinessonboardingvettingrequest_id: str,
    fields: list[ChinaBusinessOnboardingVettingRequestField] = [],
) -> str:
    """Get a ChinaBusinessOnboardingVettingRequest object by ID.

    Args:
        chinabusinessonboardingvettingrequest_id: The ID of the ChinaBusinessOnboardingVettingRequest.
        fields: Fields to retrieve. Available fields: See ChinaBusinessOnboardingVettingRequestField type.
    """
    obj = ChinaBusinessOnboardingVettingRequest(chinabusinessonboardingvettingrequest_id)
    return obj.api_get(fields=fields)

"""CPASAdvertiserPartnershipRecommendation MCP Server with typed wrappers."""

from facebook_business.adobjects.cpasadvertiserpartnershiprecommendation import (
    CPASAdvertiserPartnershipRecommendation,
)
from fastmcp import FastMCP

from src.generated.models.cpasadvertiserpartnershiprecommendation import (
    CPASAdvertiserPartnershipRecommendationField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCPASAdvertiserPartnershipRecommendation"
instructions = """
CPASAdvertiserPartnershipRecommendation MCP Server for Facebook Business API.

Provides typed access to all CPASAdvertiserPartnershipRecommendation operations.
"""

cpasadvertiserpartnershiprecommendation_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@cpasadvertiserpartnershiprecommendation_server.tool
@wrapped_fn_tool
def get_cpasadvertiserpartnershiprecommendation(
    cpasadvertiserpartnershiprecommendation_id: str,
    fields: list[CPASAdvertiserPartnershipRecommendationField] = [],
) -> str:
    """Get a CPASAdvertiserPartnershipRecommendation object by ID.

    Args:
        cpasadvertiserpartnershiprecommendation_id: The ID of the CPASAdvertiserPartnershipRecommendation.
        fields: Fields to retrieve. Available fields: See CPASAdvertiserPartnershipRecommendationField type.
    """
    obj = CPASAdvertiserPartnershipRecommendation(cpasadvertiserpartnershiprecommendation_id)
    return obj.api_get(fields=fields)

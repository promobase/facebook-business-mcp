"""PartnerStudy MCP Server with typed wrappers."""

from facebook_business.adobjects.partnerstudy import PartnerStudy
from fastmcp import FastMCP

from src.generated.models.partnerstudy import PartnerStudyField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookPartnerStudy"
instructions = """
PartnerStudy MCP Server for Facebook Business API.

Provides typed access to all PartnerStudy operations.
"""

partnerstudy_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@partnerstudy_server.tool
@wrapped_fn_tool
def get_partnerstudy(
    partnerstudy_id: str,
    fields: list[PartnerStudyField] = [],
) -> str:
    """Get a PartnerStudy object by ID.

    Args:
        partnerstudy_id: The ID of the PartnerStudy.
        fields: Fields to retrieve. Available fields: See PartnerStudyField type.
    """
    obj = PartnerStudy(partnerstudy_id)
    return obj.api_get(fields=fields)

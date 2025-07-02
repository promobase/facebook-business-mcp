"""AdSavedKeywords MCP Server with typed wrappers."""

from facebook_business.adobjects.adsavedkeywords import AdSavedKeywords
from fastmcp import FastMCP

from src.generated.models.adsavedkeywords import AdSavedKeywordsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSavedKeywords"
instructions = """
AdSavedKeywords MCP Server for Facebook Business API.

Provides typed access to all AdSavedKeywords operations.
"""

adsavedkeywords_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsavedkeywords_server.tool
@wrapped_fn_tool
def get_adsavedkeywords(
    adsavedkeywords_id: str,
    fields: list[AdSavedKeywordsField] = [],
) -> str:
    """Get a AdSavedKeywords object by ID.

    Args:
        adsavedkeywords_id: The ID of the AdSavedKeywords.
        fields: Fields to retrieve. Available fields: See AdSavedKeywordsField type.
    """
    obj = AdSavedKeywords(adsavedkeywords_id)
    return obj.api_get(fields=fields)

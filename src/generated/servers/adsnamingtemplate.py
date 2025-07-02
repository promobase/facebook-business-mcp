"""AdsNamingTemplate MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adsnamingtemplate import AdsNamingTemplate
from fastmcp import FastMCP

from src.generated.models.adsnamingtemplate import AdsNamingTemplateField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsNamingTemplate"
instructions = """
AdsNamingTemplate MCP Server for Facebook Business API.

Provides typed access to all AdsNamingTemplate operations.
"""

adsnamingtemplate_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsnamingtemplate_server.tool
@wrapped_fn_tool
def get_adsnamingtemplate(
    adsnamingtemplate_id: str,
    fields: list[AdsNamingTemplateField] = [],
) -> str:
    """Get a AdsNamingTemplate object by ID.

    Args:
        adsnamingtemplate_id: The ID of the AdsNamingTemplate.
        fields: Fields to retrieve. Available fields: See AdsNamingTemplateField type.
    """
    obj = AdsNamingTemplate(adsnamingtemplate_id)
    return obj.api_get(fields=fields)

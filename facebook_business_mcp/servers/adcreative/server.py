"""AdCreative MCP Server configuration."""

from fastmcp import FastMCP

# Import all adcreative operations
from .crud import (
    adaccount_get_ad_creatives,
    adcreative_api_create,
    adcreative_api_delete,
    adcreative_api_get,
    adcreative_api_update,
)
from .helpers import (
    create_carousel_ad_creative,
    create_dynamic_asset_ad_creative,
    create_link_ad_creative,
    create_video_ad_creative,
)
from .operations import (
    adcreative_create_ad_label,
    adcreative_get_creative_insights,
    adcreative_get_previews,
)

server_name = "FacebookAdCreative"
instructions = """
AdCreative MCP Server for Facebook Business API.

Provides typed access to all AdCreative operations including:
- CRUD operations (create, read, update, delete)
- Preview generation for different ad formats
- Creative insights
- Helper functions for common creative types:
  - Link ads
  - Video ads
  - Carousel ads
  - Dynamic product ads

Use the helper functions for simplified creative creation, or the raw CRUD operations
for full control over creative parameters.
"""

# Initialize server
server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register all tools
# CRUD operations
server.tool(adcreative_api_get)
server.tool(adcreative_api_create)
server.tool(adcreative_api_update)
server.tool(adcreative_api_delete)

# Additional operations
server.tool(adcreative_get_previews)
server.tool(adcreative_create_ad_label)
server.tool(adcreative_get_creative_insights)

# Helper functions
server.tool(create_link_ad_creative)
server.tool(create_video_ad_creative)
server.tool(create_carousel_ad_creative)
server.tool(create_dynamic_asset_ad_creative)

# Ad account level operations
server.tool(adaccount_get_ad_creatives)

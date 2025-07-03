"""Ad MCP Server configuration."""

from fastmcp import FastMCP

# Import all ad operations
from .crud import (
    ad_api_create,
    ad_api_create_from_adaccount,
    ad_api_create_from_campaign,
    ad_api_delete,
    ad_api_get,
    ad_api_update,
)
from .operations import (
    ad_add_labels,
    ad_archive,
    ad_create_copy,
    ad_get_adcreatives,
    ad_get_copies,
    ad_get_insights,
    ad_get_leads,
    ad_get_previews,
    ad_get_targetingsentencelines,
    ad_pause,
    ad_resume,
    adaccount_get_ads,
)

server_name = "FacebookAd"
instructions = """
Ad MCP Server for Facebook Business API.

Provides typed access to all Ad operations including:
- CRUD operations (create, read, update, delete)
- Ad creative management
- Performance insights and metrics
- Ad previews for different placements
- Lead generation data access
- Ad status management (pause, resume, archive)
- Ad copying and labeling

Use this server to manage individual ads within ad sets.
"""

# Initialize server
server = FastMCP(
    name=server_name,
    instructions=instructions,
)

# Register all tools
# CRUD operations
server.tool(adaccount_get_ads)
server.tool(ad_api_get)
server.tool(ad_api_create)
server.tool(ad_api_create_from_adaccount)
server.tool(ad_api_create_from_campaign)
server.tool(ad_api_update)
server.tool(ad_api_delete)

# Creative and preview operations
server.tool(ad_get_adcreatives)
server.tool(ad_get_previews)
server.tool(ad_get_targetingsentencelines)

# Performance and insights
server.tool(ad_get_insights)
server.tool(ad_get_leads)

# Status management
server.tool(ad_pause)
server.tool(ad_resume)
server.tool(ad_archive)

# Organization and copying
server.tool(ad_add_labels)
server.tool(ad_create_copy)
server.tool(ad_get_copies)

from fastmcp import FastMCP

from src.servers import ad_account_server, ad_server, adset_server, campaign_server, insights_server

mcp = FastMCP(
    name="FacebookBusinessMCP",
    description="Facebook Business MCP Server for managing Ads, Campaigns, Ad Accounts, and Insights.",
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)

mcp.mount(ad_account_server, "ad_account")
mcp.mount(ad_server, "ad")
mcp.mount(adset_server, "adset")
mcp.mount(campaign_server, "campaign")
mcp.mount(insights_server, "insights")

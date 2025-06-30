from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

from src.config import get_config_from_env
from src.utils import handle_facebook_errors

# Foundation layer
from src.servers.foundation.universal_server import higher_order_server

# Resources layer
from src.servers.resources.ad_account import ad_account_server
from src.servers.resources.campaign import campaign_server
from src.servers.resources.adset import adset_server
from src.servers.resources.ad import ad_server

# Workflows layer
from src.servers.workflows.campaign_management_server import campaign_management_server
from src.servers.workflows.reporting_server import reporting_server
from src.servers.workflows.audience_server import audience_server

# Legacy imports (to be phased out)
from src.servers.marketing_api.insights import insights_server

instructions = """
Facebook Business MCP Server - Three-Layer Architecture

🚀 QUICK START: Use workflow servers for common tasks:
- campaign_management: Create and manage complete campaigns
- reporting: Generate performance reports and analytics  
- audience: Create and manage custom/lookalike audiences

📊 CORE OPERATIONS: Use resource servers for specific operations:
- ad_account, campaign, adset, ad: Streamlined essential operations

🔧 ADVANCED: Use universal server for any SDK operation:
- universal: Direct access to any Facebook SDK method

Each server has focused tools optimized for specific use cases.
"""


def create_root_mcp() -> FastMCP:
    mcp = FastMCP(
        name="FacebookBusinessMCP",
        instructions=instructions,
        on_duplicate_prompts="error",
        on_duplicate_resources="error",
        on_duplicate_tools="error",
    )

    @mcp.tool
    @handle_facebook_errors
    def health_check() -> str:
        """Check if the Facebook Business API is properly configured and accessible.

        Returns:
            Health status information including API connectivity and user details
        """
        config = get_config_from_env()

        if not config["app_id"] or not config["app_secret"] or not config["access_token"]:
            return "error: Missing Facebook API configuration"
        api = FacebookAdsApi.get_default_api()
        user = User(fbid="me", api=api)
        user_data = user.api_get(fields=["id", "name"])

        return dict(user_data)

    @mcp.tool
    def get_default_ad_account() -> str:
        """Get the default ad account ID from the environment configuration."""
        config = get_config_from_env()
        return config.get("ad_account_id", "No default ad account configured")

    # Mount workflow servers (high-level operations)
    mcp.mount(campaign_management_server, "campaign_management")
    mcp.mount(reporting_server, "reporting")
    mcp.mount(audience_server, "audience")

    # Mount resource servers (core operations)
    mcp.mount(ad_account_server, "ad_account")
    mcp.mount(campaign_server, "campaign")
    mcp.mount(adset_server, "adset")
    mcp.mount(ad_server, "ad")

    # Mount insights server (to be refactored)
    mcp.mount(insights_server, "insights")

    # Mount universal server (foundation layer)
    mcp.mount(higher_order_server, "universal")

    return mcp

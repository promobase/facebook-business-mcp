from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

from .config import get_config_from_env
from .servers.adaccount import adaccount_server
from .servers.campaign import server as campaign_server
from .servers.adset import server as adset_server
from .servers.insights import server as insights_server
from .servers.adcreative import server as adcreative_server
from .utils import handle_facebook_errors

__version__ = "0.1.0"
__all__ = ["create_root_mcp", "__version__", "get_config_from_env", "handle_facebook_errors"]

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

    @mcp.prompt
    def test_prompt():
        return "This is a test prompt"

    @mcp.resource("data://app-status")
    def test_resource():
        return "This is a test resource"

    mcp.mount(adaccount_server)
    mcp.mount(campaign_server)
    mcp.mount(adset_server)
    mcp.mount(insights_server)
    mcp.mount(adcreative_server)

    return mcp

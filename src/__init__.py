from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

from src.config import get_config_from_env
from src.servers import ad_account_server
from src.utils import handle_facebook_errors

instructions = """
Facebook Business MCP Server for managing Ads, Campaigns, Ad Accounts, and Insights. Use the tools provided to interact with the Facebook Business API.

For each tools, you should always get the prompt first to check how to use the apis, e.g. campaigns, ads, adset, ad_accounts, etc.
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

    mcp.mount(ad_account_server, "ad_account")

    return mcp

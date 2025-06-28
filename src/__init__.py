from typing import Any

from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookError
from fastmcp import FastMCP

from src.config import get_config_from_env, validate_facebook_connection
from src.servers import ad_account_server, ad_server, adset_server, campaign_server, insights_server

instructions = """
Facebook Business MCP Server for managing Ads, Campaigns, Ad Accounts, and Insights. Use the tools provided to interact with the Facebook Business API.
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
    def health_check() -> dict[str, Any]:
        """Check if the Facebook Business API is properly configured and accessible.

        Returns:
            Health status information including API connectivity and user details
        """
        try:
            config = get_config_from_env()

            if not config["app_id"] or not config["app_secret"] or not config["access_token"]:
                return {"status": "error", "message": "Missing required Facebook API credentials"}

            # Validate connection
            if not validate_facebook_connection():
                return {"status": "error", "message": "Unable to connect to Facebook API"}

            # Get user info
            api = FacebookAdsApi.get_default_api()
            user = User(fbid="me", api=api)
            user_data = user.api_get(fields=["id", "name"])

            return dict(user_data)
        except FacebookError as e:
            return {"status": "error", "message": f"Facebook API error: {str(e)}"}
        except Exception as e:
            return {"status": "error", "message": f"Health check failed: {str(e)}"}

    mcp.mount(ad_account_server, "ad_account")
    mcp.mount(ad_server, "ad")
    mcp.mount(adset_server, "adset")
    mcp.mount(campaign_server, "campaign")
    mcp.mount(insights_server, "insights")
    return mcp

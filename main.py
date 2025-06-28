"""Facebook Business MCP Server - Modular implementation with mounted sub-servers."""

import asyncio
from typing import Any

from facebook_business.adobjects.user import User
from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookError

from src import mcp
from src.config import get_config_from_env, initialize_facebook_api, validate_facebook_connection
from src.utils import get_logger, load_dotenv

logger = get_logger(__name__)

load_dotenv(".env")


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

        return {
            "status": "healthy",
            "message": "Facebook Business API is accessible",
            "user_id": user_data.get("id"),
            "user_name": user_data.get("name"),
            "api_version": config["api_version"],
            "default_account_id": config.get("ad_account_id"),
        }

    except FacebookError as e:
        return {"status": "error", "message": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Health check failed: {str(e)}"}


async def main() -> None:
    """Main entry point."""
    try:
        # Initialize Facebook API
        config = initialize_facebook_api()
        logger.info("Starting Facebook Business MCP Server...")
        logger.info(f"API Version: {config['api_version']}")
        if config["ad_account_id"]:
            logger.info(f"Default Ad Account: {config['ad_account_id']}")

        tools = await mcp.get_tools()
        logger.info(f"Available tools: {', '.join(tools.keys())}")

        await mcp.run_async()

    except KeyboardInterrupt:
        logger.info("\nServer stopped by user.")
    except Exception as e:
        logger.info(f"Error starting server: {e}")
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())

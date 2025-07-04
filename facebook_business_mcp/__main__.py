"""Entry point for facebook-business-mcp when run as a module."""

import asyncio
import sys

from . import create_root_mcp
from .config import initialize_facebook_api
from .utils import get_logger, load_dotenv

logger = get_logger(__name__)

load_dotenv(".env")


async def run() -> None:
    """Main entry point."""
    try:
        # root mcp server
        mcp = create_root_mcp()
        # Initialize Facebook API
        config = initialize_facebook_api()
        logger.info("Starting Facebook Business MCP Server...")
        logger.info(f"API Version: {config['api_version']}")
        if config["ad_account_id"]:
            logger.info(f"Default Ad Account: {config['ad_account_id']}")

        tools = await mcp.get_tools()
        logger.info(f"Available tools: {tools}")

        await mcp.run_async(transport="stdio")

    except KeyboardInterrupt:
        logger.info("\nServer stopped by user.")
    except Exception as e:
        logger.info(f"Error starting server: {e}")
    finally:
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    asyncio.run(run())


if __name__ == "__main__":
    main()

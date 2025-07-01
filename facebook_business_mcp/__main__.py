"""Entry point for facebook-business-mcp when run as a module."""
import asyncio
import sys
from pathlib import Path

# Add parent directory to path to allow imports when run as module
parent_dir = Path(__file__).parent.parent
if parent_dir not in sys.path:
    sys.path.insert(0, str(parent_dir))

from src import create_root_mcp
from src.config import initialize_facebook_api
from src.utils import get_logger, load_dotenv

logger = get_logger(__name__)

load_dotenv(".env")


async def async_main() -> None:
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
        sys.exit(1)


def main() -> None:
    """Synchronous entry point."""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
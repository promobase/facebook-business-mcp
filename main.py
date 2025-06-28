import asyncio

from src import create_root_mcp
from src.config import initialize_facebook_api
from src.utils import get_logger, load_dotenv

logger = get_logger(__name__)

load_dotenv(".env")


async def main() -> None:
    """Main entry point."""
    try:
        mcp = create_root_mcp()
        # Initialize Facebook API
        config = initialize_facebook_api()
        logger.info("Starting Facebook Business MCP Server...")
        logger.info(f"API Version: {config['api_version']}")
        if config["ad_account_id"]:
            logger.info(f"Default Ad Account: {config['ad_account_id']}")

        tools = await mcp.get_tools()
        logger.info(f"Available tools: {', '.join(tools.keys())}")

        await mcp.run_async(
            transport="stdio",
            # port=8000,
        )

    except KeyboardInterrupt:
        logger.info("\nServer stopped by user.")
    except Exception as e:
        logger.info(f"Error starting server: {e}")
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())

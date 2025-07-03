import asyncio

from fastmcp import Client, FastMCP

# Local Python script
client = Client("main.py")


async def main():
    async with client:
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        print("Available Tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")
        print("\nAvailable Resources:")
        for resource in resources:  # noqa: E501
            print(f"- {resource.name}: {resource.description}")
        print("\nAvailable Prompts:")
        for prompt in prompts:
            print(f"- {prompt.name}: {prompt.description}")


if __name__ == "__main__":
    asyncio.run(main())

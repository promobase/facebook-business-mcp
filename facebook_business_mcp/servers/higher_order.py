import importlib
from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from facebook_business_mcp.utils import wrapped_fn_tool

server_name = "HigherOrderMCPServer"
instructions = """
Higher Order MCP server that provides directory, navigation, and management of all the endpoints/tools in the MCP.

Always use this to find docs for specific tools or endpoints to see what are the inputs & params.
"""

higher_order_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


@higher_order_server.tool
@wrapped_fn_tool
def get_tool_referece(tool_name: str) -> str:
    """Given a tool name, e.g. adaccount_api_create, return the params & inputs
    and documentation on how to use this tool.
    """
    # tool is of <domain>_<tool_name>
    domain, tool = tool_name.split("_", 1)
    if not domain or not tool:
        raise ValueError("Tool name must be in the format <domain>_<tool_name>")
    # domain is an adobject class name, from facebook_business.adobjects.adaccount import AdAccount

    raise NotImplementedError


@higher_order_server.tool
@wrapped_fn_tool
def run_any_sdk_tool() -> str:
    pass

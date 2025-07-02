"""Robot MCP Server."""

from typing import Any

from facebook_business.adobjects.robot import Robot
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookRobot"
instructions = """
Robot MCP Server for Facebook Business API.

Provides typed access to all Robot operations.
"""

robot_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@robot_server.tool
@wrapped_fn_tool
def get_robot(
    robot_id: str,
    fields: list[str] = [],
) -> str:
    obj = Robot(robot_id)
    return obj.api_get(fields=fields)

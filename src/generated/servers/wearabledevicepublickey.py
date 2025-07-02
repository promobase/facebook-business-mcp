"""WearableDevicePublicKey MCP Server."""

from typing import Any

from facebook_business.adobjects.wearabledevicepublickey import WearableDevicePublicKey
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookWearableDevicePublicKey"
instructions = """
WearableDevicePublicKey MCP Server for Facebook Business API.

Provides typed access to all WearableDevicePublicKey operations.
"""

wearabledevicepublickey_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@wearabledevicepublickey_server.tool
@wrapped_fn_tool
def get_wearabledevicepublickey(
    wearabledevicepublickey_id: str,
    fields: list[str] = [],
) -> str:
    obj = WearableDevicePublicKey(wearabledevicepublickey_id)
    return obj.api_get(fields=fields)

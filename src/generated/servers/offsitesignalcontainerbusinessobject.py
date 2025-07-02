"""OffsiteSignalContainerBusinessObject MCP Server."""

from typing import Any

from facebook_business.adobjects.offsitesignalcontainerbusinessobject import (
    OffsiteSignalContainerBusinessObject,
)
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOffsiteSignalContainerBusinessObject"
instructions = """
OffsiteSignalContainerBusinessObject MCP Server for Facebook Business API.

Provides typed access to all OffsiteSignalContainerBusinessObject operations.
"""

offsitesignalcontainerbusinessobject_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offsitesignalcontainerbusinessobject_server.tool
@wrapped_fn_tool
def get_offsitesignalcontainerbusinessobject(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[str] = [],
) -> str:
    obj = OffsiteSignalContainerBusinessObject(offsitesignalcontainerbusinessobject_id)
    return obj.api_get(fields=fields)

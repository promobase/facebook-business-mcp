"""AdgroupFacebookFeedback MCP Server."""

from typing import Any

from facebook_business.adobjects.adgroupfacebookfeedback import AdgroupFacebookFeedback
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdgroupFacebookFeedback"
instructions = """
AdgroupFacebookFeedback MCP Server for Facebook Business API.

Provides typed access to all AdgroupFacebookFeedback operations.
"""

adgroupfacebookfeedback_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adgroupfacebookfeedback_server.tool
@wrapped_fn_tool
def get_comments(
    adgroupfacebookfeedback_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdgroupFacebookFeedback(adgroupfacebookfeedback_id).get_comments(
        fields=fields, params=params
    )

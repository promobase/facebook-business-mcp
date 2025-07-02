"""AdsStartYourDayWidget MCP Server."""

from typing import Any

from facebook_business.adobjects.adsstartyourdaywidget import AdsStartYourDayWidget
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsStartYourDayWidget"
instructions = """
AdsStartYourDayWidget MCP Server for Facebook Business API.

Provides typed access to all AdsStartYourDayWidget operations.
"""

adsstartyourdaywidget_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adsstartyourdaywidget_server.tool
@wrapped_fn_tool
def get_adsstartyourdaywidget(
    adsstartyourdaywidget_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdsStartYourDayWidget(adsstartyourdaywidget_id)
    return obj.api_get(fields=fields)

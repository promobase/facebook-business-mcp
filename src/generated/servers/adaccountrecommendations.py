"""AdAccountRecommendations MCP Server."""

from typing import Any

from facebook_business.adobjects.adaccountrecommendations import AdAccountRecommendations
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAccountRecommendations"
instructions = """
AdAccountRecommendations MCP Server for Facebook Business API.

Provides typed access to all AdAccountRecommendations operations.
"""

adaccountrecommendations_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adaccountrecommendations_server.tool
@wrapped_fn_tool
def get_endpoint(
    adaccountrecommendations_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdAccountRecommendations(adaccountrecommendations_id).get_endpoint(
        fields=fields, params=params
    )

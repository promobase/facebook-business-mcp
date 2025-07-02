"""
Auto-generated MCP server for Facebook ThirdPartyPartnerPanelScheduled.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.thirdpartypartnerpanelscheduled import (
    ThirdPartyPartnerPanelScheduled,
)
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-thirdpartypartnerpanelscheduled")


# CRUD Operations


@mcp.tool()
async def get_thirdpartypartnerpanelscheduled(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a ThirdPartyPartnerPanelScheduled.

    Args:
        object_id: The ID of the ThirdPartyPartnerPanelScheduled
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = ThirdPartyPartnerPanelScheduled(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


# Export the server
thirdpartypartnerpanelscheduled_server = mcp

"""
Auto-generated MCP server for Facebook AdsPixel.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.adspixel import AdsPixel
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-adspixel")


# CRUD Operations


@mcp.tool()
async def create_adspixel(
    object_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        parent_id: parent_id
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create result
    """
    result = AdsPixel(fbid=object_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get a AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get result
    """
    result = AdsPixel(fbid=object_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def update_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Update a AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The update result
    """
    result = AdsPixel(fbid=object_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Edge Methods


@mcp.tool()
async def create_agency_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Agency for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_agency result
    """
    result = AdsPixel(fbid=object_id).create_agency(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_ahp_config_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Ahp Config for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_ahp_config result
    """
    result = AdsPixel(fbid=object_id).create_ahp_config(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_assigned_user_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Assigned User for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_assigned_user result
    """
    result = AdsPixel(fbid=object_id).create_assigned_user(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_event_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Event for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_event result
    """
    result = AdsPixel(fbid=object_id).create_event(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shadow_traffic_helper_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Shadow Traffic Helper for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_shadow_traffic_helper result
    """
    result = AdsPixel(fbid=object_id).create_shadow_traffic_helper(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def create_shared_account_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create Shared Account for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The create_shared_account result
    """
    result = AdsPixel(fbid=object_id).create_shared_account(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_agencies_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Agencies for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_agencies result
    """
    result = AdsPixel(fbid=object_id).delete_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def delete_shared_accounts_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Delete Shared Accounts for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The delete_shared_accounts result
    """
    result = AdsPixel(fbid=object_id).delete_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_ad_accounts_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Ad Accounts for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_ad_accounts result
    """
    result = AdsPixel(fbid=object_id).get_ad_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_agencies_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Agencies for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_agencies result
    """
    result = AdsPixel(fbid=object_id).get_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_assigned_users_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Assigned Users for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_assigned_users result
    """
    result = AdsPixel(fbid=object_id).get_assigned_users(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_da_checks_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Da Checks for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_da_checks result
    """
    result = AdsPixel(fbid=object_id).get_da_checks(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_offline_event_uploads_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Offline Event Uploads for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_offline_event_uploads result
    """
    result = AdsPixel(fbid=object_id).get_offline_event_uploads(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_open_bridge_configurations_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Open Bridge Configurations for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_open_bridge_configurations result
    """
    result = AdsPixel(fbid=object_id).get_open_bridge_configurations(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_accounts_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shared Accounts for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_accounts result
    """
    result = AdsPixel(fbid=object_id).get_shared_accounts(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_shared_agencies_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Shared Agencies for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_shared_agencies result
    """
    result = AdsPixel(fbid=object_id).get_shared_agencies(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def get_stats_for_adspixel(
    object_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Get Stats for AdsPixel.

    Args:
        object_id: The ID of the AdsPixel
        fields: Fields to return
        params: Additional parameters

    Returns:
        The get_stats result
    """
    result = AdsPixel(fbid=object_id).get_stats(
        fields=fields,
        params=params,
    )

    return result


# Export the server
adspixel_server = mcp

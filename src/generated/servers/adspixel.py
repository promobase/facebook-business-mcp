"""AdsPixel MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adspixel import AdsPixel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsPixel"
instructions = """
AdsPixel MCP Server for Facebook Business API.

Provides typed access to all AdsPixel operations.
"""

adspixel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adspixel_server.tool
@wrapped_fn_tool
def get_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
) -> str:
    """Get a AdsPixel object by ID.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See {server_info.object_name}Field type.
    """
    obj = AdsPixel(adspixel_id)
    return obj.api_get(fields=fields)


@adspixel_server.tool
@wrapped_fn_tool
def update_adspixel(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
) -> str:
    """Update a AdsPixel object.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to return after update. Available fields: See {server_info.object_name}Field type.
        params: Parameters to update. Available params: See AdsPixelUpdateParams type.
    """
    return AdsPixel(adspixel_id).api_update(fields=fields, params=params)


# ---- Edge Methods (13) ----
@adspixel_server.tool
@wrapped_fn_tool
def get_ad_accounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Ad Accounts for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See AdsPixelGetAdAccountsParams type.
    """
    return AdsPixel(adspixel_id).get_ad_accounts(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def delete_agencies(
    adspixel_id: str,
    params: dict = {},
):
    """Delete Agencies for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        params: Query parameters. Available params: See AdsPixelDeleteAgenciesParams type.
    """
    return AdsPixel(adspixel_id).delete_agencies(params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_agency(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Agency for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdsPixelCreateAgencyParams type.
    """
    return AdsPixel(adspixel_id).create_agency(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_ahp_config(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Ahp Config for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdsPixelCreateAhpConfigParams type.
    """
    return AdsPixel(adspixel_id).create_ahp_config(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_assigned_users(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Assigned Users for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See AssignedUserField type.
        params: Query parameters. Available params: See AdsPixelGetAssignedUsersParams type.
    """
    return AdsPixel(adspixel_id).get_assigned_users(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_assigned_user(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Assigned User for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdsPixelCreateAssignedUserParams type.
    """
    return AdsPixel(adspixel_id).create_assigned_user(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_da_checks(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Da Checks for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See DACheckField type.
        params: Query parameters. Available params: See AdsPixelGetDaChecksParams type.
    """
    return AdsPixel(adspixel_id).get_da_checks(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_event(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Event for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdsPixelCreateEventParams type.
    """
    return AdsPixel(adspixel_id).create_event(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_offline_event_uploads(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Offline Event Uploads for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See OfflineConversionDataSetUploadField type.
        params: Query parameters. Available params: See AdsPixelGetOfflineEventUploadsParams type.
    """
    return AdsPixel(adspixel_id).get_offline_event_uploads(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def delete_shared_accounts(
    adspixel_id: str,
    params: dict = {},
):
    """Delete Shared Accounts for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        params: Query parameters. Available params: See AdsPixelDeleteSharedAccountsParams type.
    """
    return AdsPixel(adspixel_id).delete_shared_accounts(params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_shared_accounts(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Shared Accounts for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See AdsPixelGetSharedAccountsParams type.
    """
    return AdsPixel(adspixel_id).get_shared_accounts(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def create_shared_account(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Shared Account for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdsPixelCreateSharedAccountParams type.
    """
    return AdsPixel(adspixel_id).create_shared_account(fields=fields, params=params)


@adspixel_server.tool
@wrapped_fn_tool
def get_stats(
    adspixel_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Stats for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See AdsPixelStatsResultField type.
        params: Query parameters. Available params: See AdsPixelGetStatsParams type.
    """
    return AdsPixel(adspixel_id).get_stats(fields=fields, params=params)

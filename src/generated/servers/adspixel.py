"""AdsPixel MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adspixel import AdsPixel
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.adaccount import AdAccountField
from src.generated.models.adspixel import (
    AdsPixelCreateAgencyParams,
    AdsPixelCreateAhpConfigParams,
    AdsPixelCreateAssignedUserParams,
    AdsPixelCreateEventParams,
    AdsPixelCreateSharedAccountParams,
    AdsPixelDeleteAgenciesParams,
    AdsPixelDeleteSharedAccountsParams,
    AdsPixelField,
    AdsPixelGetAdAccountsParams,
    AdsPixelGetAssignedUsersParams,
    AdsPixelGetDaChecksParams,
    AdsPixelGetOfflineEventUploadsParams,
    AdsPixelGetSharedAccountsParams,
    AdsPixelGetStatsParams,
    AdsPixelUpdateParams,
)
from src.generated.models.adspixelstatsresult import AdsPixelStatsResultField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.dacheck import DACheckField
from src.generated.models.offlineconversiondatasetupload import OfflineConversionDataSetUploadField
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
    fields: list[AdsPixelField] = [],
) -> str:
    """Get a AdsPixel object by ID.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See AdsPixelField type.
    """
    obj = AdsPixel(adspixel_id)
    return obj.api_get(fields=fields)


@adspixel_server.tool
@wrapped_fn_tool
def update_adspixel(
    adspixel_id: str,
    fields: list[AdsPixelField] = [],
    params: AdsPixelUpdateParams | dict = {},
) -> str:
    """Update a AdsPixel object.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to return after update. Available fields: See AdsPixelField type.
        params: Parameters to update. Available params: See AdsPixelUpdateParams type.
    """
    return AdsPixel(adspixel_id).api_update(fields=fields, params=params)


# ---- Edge Methods (13) ----
@adspixel_server.tool
@wrapped_fn_tool
def get_ad_accounts(
    adspixel_id: str,
    fields: list[AdAccountField] = [],
    params: AdsPixelGetAdAccountsParams | dict = {},
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
    params: AdsPixelDeleteAgenciesParams | dict = {},
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
    params: AdsPixelCreateAgencyParams | dict = {},
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
    params: AdsPixelCreateAhpConfigParams | dict = {},
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
    fields: list[AssignedUserField] = [],
    params: AdsPixelGetAssignedUsersParams | dict = {},
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
    params: AdsPixelCreateAssignedUserParams | dict = {},
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
    fields: list[DACheckField] = [],
    params: AdsPixelGetDaChecksParams | dict = {},
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
    params: AdsPixelCreateEventParams | dict = {},
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
    fields: list[OfflineConversionDataSetUploadField] = [],
    params: AdsPixelGetOfflineEventUploadsParams | dict = {},
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
    params: AdsPixelDeleteSharedAccountsParams | dict = {},
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
    fields: list[AdAccountField] = [],
    params: AdsPixelGetSharedAccountsParams | dict = {},
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
    params: AdsPixelCreateSharedAccountParams | dict = {},
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
    fields: list[AdsPixelStatsResultField] = [],
    params: AdsPixelGetStatsParams | dict = {},
):
    """Get Stats for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve. Available fields: See AdsPixelStatsResultField type.
        params: Query parameters. Available params: See AdsPixelGetStatsParams type.
    """
    return AdsPixel(adspixel_id).get_stats(fields=fields, params=params)

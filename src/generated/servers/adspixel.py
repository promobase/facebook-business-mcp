"""AdsPixel MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.adspixel import AdsPixel
from fastmcp import FastMCP

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
@wrapped_fn_tool
def get_adspixel(
    adspixel_id: str,
    fields: list[AdsPixelField] = [],
) -> str:
    """Get a AdsPixel object by ID.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
    """
    obj = AdsPixel(adspixel_id)
    return obj.api_get(fields=fields)


adspixel_server.tool(get_adspixel)


@wrapped_fn_tool
def update_adspixel(
    adspixel_id: str,
    fields: list[AdsPixelField] = [],
    params: AdsPixelUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdsPixel object.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdsPixel(adspixel_id).api_update(fields=fields, params=params)


adspixel_server.tool(update_adspixel)


# ---- Edge Methods (13) ----
@wrapped_fn_tool
def get_ad_accounts(
    adspixel_id: str,
    fields: list[AdAccountField] = [],
    params: AdsPixelGetAdAccountsParams = {},
) -> Any:
    """Get Ad Accounts for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).get_ad_accounts(fields=fields, params=params)


adspixel_server.tool(get_ad_accounts)


@wrapped_fn_tool
def delete_agencies(
    adspixel_id: str,
    params: AdsPixelDeleteAgenciesParams = {},
) -> Any:
    """Delete Agencies for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).delete_agencies(params=params)


adspixel_server.tool(delete_agencies)


@wrapped_fn_tool
def create_agency(
    adspixel_id: str,
    fields: list[str] = [],
    params: AdsPixelCreateAgencyParams = {},
) -> Any:
    """Create Agency for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).create_agency(fields=fields, params=params)


adspixel_server.tool(create_agency)


@wrapped_fn_tool
def create_ahp_config(
    adspixel_id: str,
    fields: list[str] = [],
    params: AdsPixelCreateAhpConfigParams = {},
) -> Any:
    """Create Ahp Config for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).create_ahp_config(fields=fields, params=params)


adspixel_server.tool(create_ahp_config)


@wrapped_fn_tool
def get_assigned_users(
    adspixel_id: str,
    fields: list[AssignedUserField] = [],
    params: AdsPixelGetAssignedUsersParams = {},
) -> Any:
    """Get Assigned Users for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).get_assigned_users(fields=fields, params=params)


adspixel_server.tool(get_assigned_users)


@wrapped_fn_tool
def create_assigned_user(
    adspixel_id: str,
    fields: list[str] = [],
    params: AdsPixelCreateAssignedUserParams = {},
) -> Any:
    """Create Assigned User for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).create_assigned_user(fields=fields, params=params)


adspixel_server.tool(create_assigned_user)


@wrapped_fn_tool
def get_da_checks(
    adspixel_id: str,
    fields: list[DACheckField] = [],
    params: AdsPixelGetDaChecksParams = {},
) -> Any:
    """Get Da Checks for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).get_da_checks(fields=fields, params=params)


adspixel_server.tool(get_da_checks)


@wrapped_fn_tool
def create_event(
    adspixel_id: str,
    fields: list[str] = [],
    params: AdsPixelCreateEventParams = {},
) -> Any:
    """Create Event for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).create_event(fields=fields, params=params)


adspixel_server.tool(create_event)


@wrapped_fn_tool
def get_offline_event_uploads(
    adspixel_id: str,
    fields: list[OfflineConversionDataSetUploadField] = [],
    params: AdsPixelGetOfflineEventUploadsParams = {},
) -> Any:
    """Get Offline Event Uploads for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).get_offline_event_uploads(fields=fields, params=params)


adspixel_server.tool(get_offline_event_uploads)


@wrapped_fn_tool
def delete_shared_accounts(
    adspixel_id: str,
    params: AdsPixelDeleteSharedAccountsParams = {},
) -> Any:
    """Delete Shared Accounts for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).delete_shared_accounts(params=params)


adspixel_server.tool(delete_shared_accounts)


@wrapped_fn_tool
def get_shared_accounts(
    adspixel_id: str,
    fields: list[AdAccountField] = [],
    params: AdsPixelGetSharedAccountsParams = {},
) -> Any:
    """Get Shared Accounts for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).get_shared_accounts(fields=fields, params=params)


adspixel_server.tool(get_shared_accounts)


@wrapped_fn_tool
def create_shared_account(
    adspixel_id: str,
    fields: list[str] = [],
    params: AdsPixelCreateSharedAccountParams = {},
) -> Any:
    """Create Shared Account for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).create_shared_account(fields=fields, params=params)


adspixel_server.tool(create_shared_account)


@wrapped_fn_tool
def get_stats(
    adspixel_id: str,
    fields: list[AdsPixelStatsResultField] = [],
    params: AdsPixelGetStatsParams = {},
) -> Any:
    """Get Stats for this AdsPixel.

    Args:
        adspixel_id: The ID of the AdsPixel.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdsPixel(adspixel_id).get_stats(fields=fields, params=params)


adspixel_server.tool(get_stats)

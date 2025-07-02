"""OfflineConversionDataSet MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.adaccount import AdAccountField
from src.generated.models.business import BusinessField
from src.generated.models.customaudience import CustomAudienceField
from src.generated.models.customconversion import CustomConversionField
from src.generated.models.offlineconversiondataset import (
    OfflineConversionDataSetField,
    OfflineConversionDataSetGetAdAccountsParams,
    OfflineConversionDataSetGetAudiencesParams,
    OfflineConversionDataSetGetCustomConversionsParams,
    OfflineConversionDataSetGetSharedAccountsParams,
    OfflineConversionDataSetGetSharedAgenciesParams,
    OfflineConversionDataSetGetStatsParams,
    OfflineConversionDataSetGetUploadsParams,
)
from src.generated.models.offlineconversiondatasetupload import OfflineConversionDataSetUploadField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOfflineConversionDataSet"
instructions = """
OfflineConversionDataSet MCP Server for Facebook Business API.

Provides typed access to all OfflineConversionDataSet operations.
"""

offlineconversiondataset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_offlineconversiondataset(
    offlineconversiondataset_id: str,
    fields: list[OfflineConversionDataSetField] = [],
) -> str:
    """Get a OfflineConversionDataSet object by ID.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See OfflineConversionDataSetField type.
    """
    obj = OfflineConversionDataSet(offlineconversiondataset_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (7) ----
@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_ad_accounts(
    offlineconversiondataset_id: str,
    fields: list[AdAccountField] = [],
    params: OfflineConversionDataSetGetAdAccountsParams | dict = {},
):
    """Get Ad Accounts for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetAdAccountsParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_ad_accounts(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_audiences(
    offlineconversiondataset_id: str,
    fields: list[CustomAudienceField] = [],
    params: OfflineConversionDataSetGetAudiencesParams | dict = {},
):
    """Get Audiences for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See CustomAudienceField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetAudiencesParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_audiences(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_custom_conversions(
    offlineconversiondataset_id: str,
    fields: list[CustomConversionField] = [],
    params: OfflineConversionDataSetGetCustomConversionsParams | dict = {},
):
    """Get Custom Conversions for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See CustomConversionField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetCustomConversionsParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_custom_conversions(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_shared_accounts(
    offlineconversiondataset_id: str,
    fields: list[AdAccountField] = [],
    params: OfflineConversionDataSetGetSharedAccountsParams | dict = {},
):
    """Get Shared Accounts for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See AdAccountField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetSharedAccountsParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_shared_accounts(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_shared_agencies(
    offlineconversiondataset_id: str,
    fields: list[BusinessField] = [],
    params: OfflineConversionDataSetGetSharedAgenciesParams | dict = {},
):
    """Get Shared Agencies for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See BusinessField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetSharedAgenciesParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_shared_agencies(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_stats(
    offlineconversiondataset_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: OfflineConversionDataSetGetStatsParams | dict = {},
):
    """Get Stats for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetStatsParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_stats(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_uploads(
    offlineconversiondataset_id: str,
    fields: list[OfflineConversionDataSetUploadField] = [],
    params: OfflineConversionDataSetGetUploadsParams | dict = {},
):
    """Get Uploads for this OfflineConversionDataSet.

    Args:
        offlineconversiondataset_id: The ID of the OfflineConversionDataSet.
        fields: Fields to retrieve. Available fields: See OfflineConversionDataSetUploadField type.
        params: Query parameters. Available params: See OfflineConversionDataSetGetUploadsParams type.
    """
    return OfflineConversionDataSet(offlineconversiondataset_id).get_uploads(
        fields=fields, params=params
    )

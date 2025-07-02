"""OfflineConversionDataSet MCP Server."""

from typing import Any

from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
from fastmcp import FastMCP

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
    fields: list[str] = [],
) -> str:
    obj = OfflineConversionDataSet(offlineconversiondataset_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (9) ----
@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_adaccounts(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_adaccounts(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_agencies(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_agencies(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_audiences(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_audiences(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_customconversions(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_customconversions(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_server_events_permitted_business(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(
        offlineconversiondataset_id
    ).get_server_events_permitted_business(fields=fields, params=params)


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_shared_accounts(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_shared_accounts(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_shared_agencies(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_shared_agencies(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_stats(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_stats(
        fields=fields, params=params
    )


@offlineconversiondataset_server.tool
@wrapped_fn_tool
def get_uploads(
    offlineconversiondataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return OfflineConversionDataSet(offlineconversiondataset_id).get_uploads(
        fields=fields, params=params
    )

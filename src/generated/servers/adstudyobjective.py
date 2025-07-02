"""AdStudyObjective MCP Server."""

from typing import Any

from facebook_business.adobjects.adstudyobjective import AdStudyObjective
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdStudyObjective"
instructions = """
AdStudyObjective MCP Server for Facebook Business API.

Provides typed access to all AdStudyObjective operations.
"""

adstudyobjective_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adstudyobjective_server.tool
@wrapped_fn_tool
def get_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
) -> str:
    obj = AdStudyObjective(adstudyobjective_id)
    return obj.api_get(fields=fields)


@adstudyobjective_server.tool
@wrapped_fn_tool
def update_adstudyobjective(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdStudyObjective(adstudyobjective_id).api_update(fields=fields, params=params)


# ---- Edge Methods (7) ----
@adstudyobjective_server.tool
@wrapped_fn_tool
def get_adspixels(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_adspixels(fields=fields, params=params)


@adstudyobjective_server.tool
@wrapped_fn_tool
def get_applications(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_applications(fields=fields, params=params)


@adstudyobjective_server.tool
@wrapped_fn_tool
def get_brand_requests(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_brand_requests(fields=fields, params=params)


@adstudyobjective_server.tool
@wrapped_fn_tool
def get_customconversions(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_customconversions(fields=fields, params=params)


@adstudyobjective_server.tool
@wrapped_fn_tool
def get_offline_conversion_data_sets(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_offline_conversion_data_sets(
        fields=fields, params=params
    )


@adstudyobjective_server.tool
@wrapped_fn_tool
def get_partner_private_studies(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_partner_private_studies(
        fields=fields, params=params
    )


@adstudyobjective_server.tool
@wrapped_fn_tool
def get_partnerstudies(
    adstudyobjective_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AdStudyObjective(adstudyobjective_id).get_partnerstudies(fields=fields, params=params)

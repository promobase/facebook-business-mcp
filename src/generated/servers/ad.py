"""Ad MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAd"
instructions = """
Ad MCP Server for Facebook Business API.

Provides typed access to all Ad operations.
"""

ad_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@ad_server.tool
@wrapped_fn_tool
def get_ad(
    ad_id: str,
    fields: list[str] = [],
) -> str:
    """Get a Ad object by ID.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields: See {server_info.object_name}Field type.
    """
    obj = Ad(ad_id)
    return obj.api_get(fields=fields)


@ad_server.tool
@wrapped_fn_tool
def update_ad(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
) -> str:
    """Update a Ad object.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to return after update. Available fields: See {server_info.object_name}Field type.
        params: Parameters to update. Available params: See AdUpdateParams type.
    """
    return Ad(ad_id).api_update(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def delete_ad(
    ad_id: str,
) -> str:
    """Delete a Ad object.

    Args:
        ad_id: The ID of the Ad.
    """
    return Ad(ad_id).api_delete()


# ---- Edge Methods (7) ----
@ad_server.tool
@wrapped_fn_tool
def create_ad_label(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Ad Label for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdCreateAdLabelParams type.
    """
    return Ad(ad_id).create_ad_label(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_ad_rules_governed(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Ad Rules Governed for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields: See AdRuleField type.
        params: Query parameters. Available params: See AdGetAdRulesGovernedParams type.
    """
    return Ad(ad_id).get_ad_rules_governed(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_copies(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Copies for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields: See AdField type.
        params: Query parameters. Available params: See AdGetCopiesParams type.
    """
    return Ad(ad_id).get_copies(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def create_copy(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Copy for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdCreateCopyParams type.
    """
    return Ad(ad_id).create_copy(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_insights(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Insights for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields: See AdsInsightsField type.
        params: Query parameters. Available params: See AdGetInsightsParams type.
    """
    return Ad(ad_id).get_insights(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_insights_async(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Insights Async for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields: See AdReportRunField type.
        params: Query parameters. Available params: See AdGetInsightsAsyncParams type.
    """
    return Ad(ad_id).get_insights_async(fields=fields, params=params)


@ad_server.tool
@wrapped_fn_tool
def get_previews(
    ad_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Previews for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields: See AdPreviewField type.
        params: Query parameters. Available params: See AdGetPreviewsParams type.
    """
    return Ad(ad_id).get_previews(fields=fields, params=params)

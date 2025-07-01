"""Ad MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.generated.models.ad import (
    AdCreateAdLabelParams,
    AdCreateCopyParams,
    AdField,
    AdGetAdRulesGovernedParams,
    AdGetCopiesParams,
    AdGetInsightsAsyncParams,
    AdGetInsightsParams,
    AdGetPreviewsParams,
    AdUpdateParams,
)
from src.generated.models.adpreview import AdPreviewField
from src.generated.models.adreportrun import AdReportRunField
from src.generated.models.adrule import AdRuleField
from src.generated.models.adsinsights import AdsInsightsField
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
@wrapped_fn_tool
def get_ad(
    ad_id: str,
    fields: list[AdField] = [],
) -> str:
    """Get a Ad object by ID.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
    """
    obj = Ad(ad_id)
    return obj.api_get(fields=fields)


ad_server.tool(get_ad)


@wrapped_fn_tool
def update_ad(
    ad_id: str,
    fields: list[AdField] = [],
    params: AdUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a Ad object.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return Ad(ad_id).api_update(fields=fields, params=params)


ad_server.tool(update_ad)


@wrapped_fn_tool
def delete_ad(
    ad_id: str,
) -> str:
    """Delete a Ad object.

    Args:
        ad_id: The ID of the Ad.
    """
    return Ad(ad_id).api_delete()


ad_server.tool(delete_ad)


# ---- Edge Methods (7) ----
@wrapped_fn_tool
def create_ad_label(
    ad_id: str,
    fields: list[str] = [],
    params: AdCreateAdLabelParams = {},
) -> Any:
    """Create Ad Label for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).create_ad_label(fields=fields, params=params)


ad_server.tool(create_ad_label)


@wrapped_fn_tool
def get_ad_rules_governed(
    ad_id: str,
    fields: list[AdRuleField] = [],
    params: AdGetAdRulesGovernedParams = {},
) -> Any:
    """Get Ad Rules Governed for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).get_ad_rules_governed(fields=fields, params=params)


ad_server.tool(get_ad_rules_governed)


@wrapped_fn_tool
def get_copies(
    ad_id: str,
    fields: list[AdField] = [],
    params: AdGetCopiesParams = {},
) -> Any:
    """Get Copies for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).get_copies(fields=fields, params=params)


ad_server.tool(get_copies)


@wrapped_fn_tool
def create_copy(
    ad_id: str,
    fields: list[str] = [],
    params: AdCreateCopyParams = {},
) -> Any:
    """Create Copy for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).create_copy(fields=fields, params=params)


ad_server.tool(create_copy)


@wrapped_fn_tool
def get_insights(
    ad_id: str,
    fields: list[AdsInsightsField] = [],
    params: AdGetInsightsParams = {},
) -> Any:
    """Get Insights for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).get_insights(fields=fields, params=params)


ad_server.tool(get_insights)


@wrapped_fn_tool
def get_insights_async(
    ad_id: str,
    fields: list[AdReportRunField] = [],
    params: AdGetInsightsAsyncParams = {},
) -> Any:
    """Get Insights Async for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).get_insights_async(fields=fields, params=params)


ad_server.tool(get_insights_async)


@wrapped_fn_tool
def get_previews(
    ad_id: str,
    fields: list[AdPreviewField] = [],
    params: AdGetPreviewsParams = {},
) -> Any:
    """Get Previews for this Ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return Ad(ad_id).get_previews(fields=fields, params=params)


ad_server.tool(get_previews)

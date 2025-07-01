"""AdSet MCP Server with typed wrappers."""

from __future__ import annotations

from typing import Any

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

from src.generated.models.ad import AdField
from src.generated.models.adactivity import AdActivityField
from src.generated.models.adasyncrequest import AdAsyncRequestField
from src.generated.models.adcampaigndeliveryestimate import AdCampaignDeliveryEstimateField
from src.generated.models.adreportrun import AdReportRunField
from src.generated.models.adrule import AdRuleField
from src.generated.models.adset import (
    AdSetCreateAdLabelParams,
    AdSetCreateBudgetScheduleParams,
    AdSetCreateCopyParams,
    AdSetDeleteAdLabelsParams,
    AdSetField,
    AdSetGetActivitiesParams,
    AdSetGetAdRulesGovernedParams,
    AdSetGetAdsParams,
    AdSetGetAsyncAdRequestsParams,
    AdSetGetCopiesParams,
    AdSetGetDeliveryEstimateParams,
    AdSetGetInsightsAsyncParams,
    AdSetGetInsightsParams,
    AdSetGetMessageDeliveryEstimateParams,
    AdSetUpdateParams,
)
from src.generated.models.adsinsights import AdsInsightsField
from src.generated.models.messagedeliveryestimate import MessageDeliveryEstimateField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSet"
instructions = """
AdSet MCP Server for Facebook Business API.

Provides typed access to all AdSet operations.
"""

adset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_adset(
    adset_id: str,
    fields: list[AdSetField] = [],
) -> str:
    """Get a AdSet object by ID.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
    """
    obj = AdSet(adset_id)
    return obj.api_get(fields=fields)


adset_server.tool(get_adset)


@wrapped_fn_tool
def update_adset(
    adset_id: str,
    fields: list[AdSetField] = [],
    params: AdSetUpdateParams | dict[str, Any] = {},
) -> str:
    """Update a AdSet object.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to return after update.
        params: Parameters to update.
    """
    return AdSet(adset_id).api_update(fields=fields, params=params)


adset_server.tool(update_adset)


@wrapped_fn_tool
def delete_adset(
    adset_id: str,
) -> str:
    """Delete a AdSet object.

    Args:
        adset_id: The ID of the AdSet.
    """
    return AdSet(adset_id).api_delete()


adset_server.tool(delete_adset)


# ---- Edge Methods (13) ----
@wrapped_fn_tool
def get_activities(
    adset_id: str,
    fields: list[AdActivityField] = [],
    params: AdSetGetActivitiesParams = {},
) -> Any:
    """Get Activities for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_activities(fields=fields, params=params)


adset_server.tool(get_activities)


@wrapped_fn_tool
def delete_ad_labels(
    adset_id: str,
    params: AdSetDeleteAdLabelsParams = {},
) -> Any:
    """Delete Ad Labels for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        params: Query parameters.
    """
    return AdSet(adset_id).delete_ad_labels(params=params)


adset_server.tool(delete_ad_labels)


@wrapped_fn_tool
def create_ad_label(
    adset_id: str,
    fields: list[str] = [],
    params: AdSetCreateAdLabelParams = {},
) -> Any:
    """Create Ad Label for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).create_ad_label(fields=fields, params=params)


adset_server.tool(create_ad_label)


@wrapped_fn_tool
def get_ad_rules_governed(
    adset_id: str,
    fields: list[AdRuleField] = [],
    params: AdSetGetAdRulesGovernedParams = {},
) -> Any:
    """Get Ad Rules Governed for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_ad_rules_governed(fields=fields, params=params)


adset_server.tool(get_ad_rules_governed)


@wrapped_fn_tool
def get_ads(
    adset_id: str,
    fields: list[AdField] = [],
    params: AdSetGetAdsParams = {},
) -> Any:
    """Get Ads for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_ads(fields=fields, params=params)


adset_server.tool(get_ads)


@wrapped_fn_tool
def get_async_ad_requests(
    adset_id: str,
    fields: list[AdAsyncRequestField] = [],
    params: AdSetGetAsyncAdRequestsParams = {},
) -> Any:
    """Get Async Ad Requests for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_async_ad_requests(fields=fields, params=params)


adset_server.tool(get_async_ad_requests)


@wrapped_fn_tool
def create_budget_schedule(
    adset_id: str,
    fields: list[str] = [],
    params: AdSetCreateBudgetScheduleParams = {},
) -> Any:
    """Create Budget Schedule for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).create_budget_schedule(fields=fields, params=params)


adset_server.tool(create_budget_schedule)


@wrapped_fn_tool
def get_copies(
    adset_id: str,
    fields: list[AdSetField] = [],
    params: AdSetGetCopiesParams = {},
) -> Any:
    """Get Copies for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_copies(fields=fields, params=params)


adset_server.tool(get_copies)


@wrapped_fn_tool
def create_copy(
    adset_id: str,
    fields: list[str] = [],
    params: AdSetCreateCopyParams = {},
) -> Any:
    """Create Copy for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).create_copy(fields=fields, params=params)


adset_server.tool(create_copy)


@wrapped_fn_tool
def get_delivery_estimate(
    adset_id: str,
    fields: list[AdCampaignDeliveryEstimateField] = [],
    params: AdSetGetDeliveryEstimateParams = {},
) -> Any:
    """Get Delivery Estimate for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_delivery_estimate(fields=fields, params=params)


adset_server.tool(get_delivery_estimate)


@wrapped_fn_tool
def get_insights(
    adset_id: str,
    fields: list[AdsInsightsField] = [],
    params: AdSetGetInsightsParams = {},
) -> Any:
    """Get Insights for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_insights(fields=fields, params=params)


adset_server.tool(get_insights)


@wrapped_fn_tool
def get_insights_async(
    adset_id: str,
    fields: list[AdReportRunField] = [],
    params: AdSetGetInsightsAsyncParams = {},
) -> Any:
    """Get Insights Async for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_insights_async(fields=fields, params=params)


adset_server.tool(get_insights_async)


@wrapped_fn_tool
def get_message_delivery_estimate(
    adset_id: str,
    fields: list[MessageDeliveryEstimateField] = [],
    params: AdSetGetMessageDeliveryEstimateParams = {},
) -> Any:
    """Get Message Delivery Estimate for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters.
    """
    return AdSet(adset_id).get_message_delivery_estimate(fields=fields, params=params)


adset_server.tool(get_message_delivery_estimate)

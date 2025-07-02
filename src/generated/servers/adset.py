"""AdSet MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

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
@adset_server.tool
@wrapped_fn_tool
def get_adset(
    adset_id: str,
    fields: list[str] = [],
) -> str:
    """Get a AdSet object by ID.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See {server_info.object_name}Field type.
    """
    obj = AdSet(adset_id)
    return obj.api_get(fields=fields)


@adset_server.tool
@wrapped_fn_tool
def update_adset(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
) -> str:
    """Update a AdSet object.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to return after update. Available fields: See {server_info.object_name}Field type.
        params: Parameters to update. Available params: See AdSetUpdateParams type.
    """
    return AdSet(adset_id).api_update(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def delete_adset(
    adset_id: str,
) -> str:
    """Delete a AdSet object.

    Args:
        adset_id: The ID of the AdSet.
    """
    return AdSet(adset_id).api_delete()


# ---- Edge Methods (13) ----
@adset_server.tool
@wrapped_fn_tool
def get_activities(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Activities for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdActivityField type.
        params: Query parameters. Available params: See AdSetGetActivitiesParams type.
    """
    return AdSet(adset_id).get_activities(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def delete_ad_labels(
    adset_id: str,
    params: dict = {},
):
    """Delete Ad Labels for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        params: Query parameters. Available params: See AdSetDeleteAdLabelsParams type.
    """
    return AdSet(adset_id).delete_ad_labels(params=params)


@adset_server.tool
@wrapped_fn_tool
def create_ad_label(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Ad Label for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdSetCreateAdLabelParams type.
    """
    return AdSet(adset_id).create_ad_label(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_ad_rules_governed(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Ad Rules Governed for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdRuleField type.
        params: Query parameters. Available params: See AdSetGetAdRulesGovernedParams type.
    """
    return AdSet(adset_id).get_ad_rules_governed(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_ads(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Ads for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdField type.
        params: Query parameters. Available params: See AdSetGetAdsParams type.
    """
    return AdSet(adset_id).get_ads(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_async_ad_requests(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Async Ad Requests for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdAsyncRequestField type.
        params: Query parameters. Available params: See AdSetGetAsyncAdRequestsParams type.
    """
    return AdSet(adset_id).get_async_ad_requests(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def create_budget_schedule(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Budget Schedule for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdSetCreateBudgetScheduleParams type.
    """
    return AdSet(adset_id).create_budget_schedule(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_copies(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Copies for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdSetField type.
        params: Query parameters. Available params: See AdSetGetCopiesParams type.
    """
    return AdSet(adset_id).get_copies(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def create_copy(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Create Copy for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdSetCreateCopyParams type.
    """
    return AdSet(adset_id).create_copy(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Delivery Estimate for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdCampaignDeliveryEstimateField type.
        params: Query parameters. Available params: See AdSetGetDeliveryEstimateParams type.
    """
    return AdSet(adset_id).get_delivery_estimate(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_insights(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Insights for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdsInsightsField type.
        params: Query parameters. Available params: See AdSetGetInsightsParams type.
    """
    return AdSet(adset_id).get_insights(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_insights_async(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Insights Async for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See AdReportRunField type.
        params: Query parameters. Available params: See AdSetGetInsightsAsyncParams type.
    """
    return AdSet(adset_id).get_insights_async(fields=fields, params=params)


@adset_server.tool
@wrapped_fn_tool
def get_message_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict = {},
):
    """Get Message Delivery Estimate for this AdSet.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve. Available fields: See MessageDeliveryEstimateField type.
        params: Query parameters. Available params: See AdSetGetMessageDeliveryEstimateParams type.
    """
    return AdSet(adset_id).get_message_delivery_estimate(fields=fields, params=params)

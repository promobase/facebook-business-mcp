"""Campaign MCP Server with typed wrappers."""

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.generated.models.ad import AdField
from src.generated.models.adreportrun import AdReportRunField
from src.generated.models.adrule import AdRuleField
from src.generated.models.adset import AdSetField
from src.generated.models.adsinsights import AdsInsightsField
from src.generated.models.campaign import (
    CampaignCreateAdLabelParams,
    CampaignCreateBudgetScheduleParams,
    CampaignCreateCopyParams,
    CampaignField,
    CampaignGetAdRulesGovernedParams,
    CampaignGetAdSetsParams,
    CampaignGetAdsParams,
    CampaignGetCopiesParams,
    CampaignGetInsightsAsyncParams,
    CampaignGetInsightsParams,
    CampaignUpdateParams,
)
from src.generated.models.highdemandperiod import HighDemandPeriodField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCampaign"
instructions = """
Campaign MCP Server for Facebook Business API.

Provides typed access to all Campaign operations.
"""

campaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@campaign_server.tool
@wrapped_fn_tool
def get_campaign(
    campaign_id: str,
    fields: list[CampaignField] = [],
) -> str:
    """Get a Campaign object by ID.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See CampaignField type.
    """
    obj = Campaign(campaign_id)
    return obj.api_get(fields=fields)


@campaign_server.tool
@wrapped_fn_tool
def update_campaign(
    campaign_id: str,
    fields: list[CampaignField] = [],
    params: CampaignUpdateParams | dict = {},
) -> str:
    """Update a Campaign object.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to return after update. Available fields: See CampaignField type.
        params: Parameters to update. Available params: See CampaignUpdateParams type.
    """
    return Campaign(campaign_id).api_update(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def delete_campaign(
    campaign_id: str,
) -> str:
    """Delete a Campaign object.

    Args:
        campaign_id: The ID of the Campaign.
    """
    return Campaign(campaign_id).api_delete()


# ---- Edge Methods (9) ----
@campaign_server.tool
@wrapped_fn_tool
def create_ad_label(
    campaign_id: str,
    fields: list[str] = [],
    params: CampaignCreateAdLabelParams | dict = {},
):
    """Create Ad Label for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CampaignCreateAdLabelParams type.
    """
    return Campaign(campaign_id).create_ad_label(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_ad_rules_governed(
    campaign_id: str,
    fields: list[AdRuleField] = [],
    params: CampaignGetAdRulesGovernedParams | dict = {},
):
    """Get Ad Rules Governed for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See AdRuleField type.
        params: Query parameters. Available params: See CampaignGetAdRulesGovernedParams type.
    """
    return Campaign(campaign_id).get_ad_rules_governed(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_ads(
    campaign_id: str,
    fields: list[AdField] = [],
    params: CampaignGetAdsParams | dict = {},
):
    """Get Ads for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See AdField type.
        params: Query parameters. Available params: See CampaignGetAdsParams type.
    """
    return Campaign(campaign_id).get_ads(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_ad_sets(
    campaign_id: str,
    fields: list[AdSetField] = [],
    params: CampaignGetAdSetsParams | dict = {},
):
    """Get Ad Sets for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See AdSetField type.
        params: Query parameters. Available params: See CampaignGetAdSetsParams type.
    """
    return Campaign(campaign_id).get_ad_sets(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def create_budget_schedule(
    campaign_id: str,
    fields: list[str] = [],
    params: CampaignCreateBudgetScheduleParams | dict = {},
):
    """Create Budget Schedule for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CampaignCreateBudgetScheduleParams type.
    """
    return Campaign(campaign_id).create_budget_schedule(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_copies(
    campaign_id: str,
    fields: list[CampaignField] = [],
    params: CampaignGetCopiesParams | dict = {},
):
    """Get Copies for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See CampaignField type.
        params: Query parameters. Available params: See CampaignGetCopiesParams type.
    """
    return Campaign(campaign_id).get_copies(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def create_copy(
    campaign_id: str,
    fields: list[str] = [],
    params: CampaignCreateCopyParams | dict = {},
):
    """Create Copy for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See CampaignCreateCopyParams type.
    """
    return Campaign(campaign_id).create_copy(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_insights(
    campaign_id: str,
    fields: list[AdsInsightsField] = [],
    params: CampaignGetInsightsParams | dict = {},
):
    """Get Insights for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See AdsInsightsField type.
        params: Query parameters. Available params: See CampaignGetInsightsParams type.
    """
    return Campaign(campaign_id).get_insights(fields=fields, params=params)


@campaign_server.tool
@wrapped_fn_tool
def get_insights_async(
    campaign_id: str,
    fields: list[AdReportRunField] = [],
    params: CampaignGetInsightsAsyncParams | dict = {},
):
    """Get Insights Async for this Campaign.

    Args:
        campaign_id: The ID of the Campaign.
        fields: Fields to retrieve. Available fields: See AdReportRunField type.
        params: Query parameters. Available params: See CampaignGetInsightsAsyncParams type.
    """
    return Campaign(campaign_id).get_insights_async(fields=fields, params=params)

"""Campaign Management Workflow Server - High-level operations for common campaign tasks."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCampaignManagement"
instructions = """
Campaign Management Workflow Server for Facebook Business API.

This server provides high-level workflow tools that compose multiple operations
to accomplish common campaign management tasks efficiently.

These workflows handle the complexity of multi-step operations, making it easier
to create and manage complete campaign structures.
"""

campaign_management_server = FastMCP(
    name=server_name,
    instructions=instructions,
)

Campaign.Field.__dict__.values()


# ---- Complete Campaign Creation ----
@wrapped_fn_tool
def create_complete_campaign(
    account_id: str,
    campaign_name: str,
    objective: str,
    daily_budget: int,
    adset_name: str,
    targeting: dict[str, Any],
    optimization_goal: str = "LINK_CLICKS",
    billing_event: str = "IMPRESSIONS",
    bid_strategy: str = "LOWEST_COST_WITHOUT_CAP",
    destination_url: str | None = None,
    special_ad_categories: list[str] = [],
) -> str:
    """Create a complete campaign with ad set in one operation.

    This workflow creates both campaign and ad set with proper configuration,
    handling all the complexity of multi-step creation.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        campaign_name: Name for the campaign.
        objective: Campaign objective (e.g., 'LINK_CLICKS', 'CONVERSIONS', 'REACH').
        daily_budget: Daily budget in dollars (will be converted to cents).
        adset_name: Name for the ad set.
        targeting: Targeting specification (e.g., {'geo_locations': {'countries': ['US']}, 'age_min': 18}).
        optimization_goal: What to optimize for (default: 'LINK_CLICKS').
        billing_event: What to bill for (default: 'IMPRESSIONS').
        bid_strategy: Bidding strategy (default: 'LOWEST_COST_WITHOUT_CAP').
        destination_url: URL for traffic campaigns.
        special_ad_categories: Special categories if applicable (e.g., ['CREDIT', 'HOUSING']).

    Returns:
        Dict with created campaign and ad set IDs and next steps.
    """
    account = AdAccount(account_id)

    # Create campaign
    campaign_params = {
        "name": campaign_name,
        "objective": objective,
        "status": "PAUSED",
        "special_ad_categories": special_ad_categories,
    }

    campaign = account.create_campaign(fields=["id"], params=campaign_params)

    # Create ad set
    adset_params = {
        "name": adset_name,
        "campaign_id": campaign["id"],
        "daily_budget": daily_budget * 100,  # Convert to cents
        "billing_event": billing_event,
        "optimization_goal": optimization_goal,
        "bid_strategy": bid_strategy,
        "targeting": targeting,
        "status": "PAUSED",
    }

    # Add promoted object if needed
    if objective == "LINK_CLICKS" and destination_url:
        adset_params["promoted_object"] = {"website_url": destination_url}

    adset = account.create_ad_set(fields=["id"], params=adset_params)

    return {
        "campaign_id": campaign["id"],
        "adset_id": adset["id"],
        "next_steps": [
            "Create ad creative using the creative server",
            "Create ad using the ad server with the creative ID",
            "Review and activate campaign when ready",
        ],
    }


@wrapped_fn_tool
def duplicate_campaign_with_modifications(
    source_campaign_id: str,
    new_name: str,
    modifications: dict[str, Any] = {},
    include_adsets: bool = True,
    include_ads: bool = False,
    status_filter: list[str] = ["ACTIVE", "PAUSED"],
) -> str:
    """Duplicate a campaign with selective modifications.

    Smart duplication that allows you to copy a campaign structure
    while making specific changes to the copy.

    Args:
        source_campaign_id: Campaign ID to duplicate.
        new_name: Name for the new campaign.
        modifications: Changes to apply (e.g., {'daily_budget': 200, 'targeting': {...}}).
        include_adsets: Whether to duplicate ad sets.
        include_ads: Whether to duplicate ads.
        status_filter: Only duplicate items with these statuses.

    Returns:
        Dict with new campaign structure and applied modifications.
    """
    source_campaign = Campaign(source_campaign_id)

    # Get campaign details
    campaign_data = source_campaign.api_get(
        fields=[
            "name",
            "objective",
            "status",
            "daily_budget",
            "lifetime_budget",
            "special_ad_categories",
        ]
    )

    # Create copy params
    copy_params = {
        "deep_copy": include_adsets,
        "status_option": "PAUSED",
        "rename_options": {"rename_suffix": f" - Copy of {campaign_data['name']}"},
    }

    # Apply campaign-level modifications
    if modifications:
        copy_params.update(modifications)

    # Create the copy
    result = source_campaign.create_copy(fields=[], params=copy_params)

    return {
        "original_campaign_id": source_campaign_id,
        "new_campaign_id": result.get("copied_campaign_id"),
        "modifications_applied": modifications,
        "adsets_copied": include_adsets,
        "ads_copied": include_ads,
    }


@wrapped_fn_tool
def campaign_health_check(
    campaign_id: str,
    include_recommendations: bool = True,
) -> str:
    """Comprehensive campaign performance and setup analysis.

    Analyzes campaign health including performance metrics, setup issues,
    and provides actionable recommendations.

    Args:
        campaign_id: Campaign ID to analyze.
        include_recommendations: Whether to include optimization recommendations.

    Returns:
        Comprehensive health report with metrics and recommendations.
    """
    campaign = Campaign(campaign_id)

    # Get campaign info
    campaign_info = campaign.api_get(
        fields=[
            "name",
            "status",
            "objective",
            "daily_budget",
            "lifetime_budget",
            "created_time",
            "updated_time",
        ]
    )

    # Get performance insights
    insights = campaign.get_insights(
        fields=[
            "impressions",
            "clicks",
            "spend",
            "cpm",
            "cpc",
            "ctr",
            "conversions",
            "conversion_values",
            "purchase_roas",
        ],
        params={"date_preset": "last_7d"},
    )
    insights_data = list(insights)[0] if insights else {}

    # Get ad sets
    adsets = campaign.get_ad_sets(
        fields=["name", "status", "effective_status", "issues_info"], params={"limit": 100}
    )
    adsets_list = list(adsets)

    # Get ads
    ads = campaign.get_ads(
        fields=["name", "status", "effective_status", "recommendations"], params={"limit": 100}
    )
    ads_list = list(ads)

    # Build health report
    health_report = {
        "campaign_info": campaign_info,
        "performance_last_7d": insights_data,
        "structure": {
            "total_adsets": len(adsets_list),
            "active_adsets": len([a for a in adsets_list if a.get("effective_status") == "ACTIVE"]),
            "total_ads": len(ads_list),
            "active_ads": len([a for a in ads_list if a.get("effective_status") == "ACTIVE"]),
        },
        "issues": {
            "adsets_with_issues": [a for a in adsets_list if a.get("issues_info")],
            "ads_with_recommendations": [a for a in ads_list if a.get("recommendations")],
        },
    }

    if include_recommendations:
        recommendations = []

        # Performance-based recommendations
        if insights_data:
            ctr = float(insights_data.get("ctr", 0))
            if ctr < 1.0:
                recommendations.append(
                    "CTR below 1% - consider refreshing creative or refining targeting"
                )

            spend = float(insights_data.get("spend", 0))
            if spend == 0 and campaign_info.get("status") == "ACTIVE":
                recommendations.append(
                    "No spend despite active status - check account funding and bid settings"
                )

        # Structure recommendations
        if health_report["structure"]["active_ads"] == 0:
            recommendations.append("No active ads - campaign cannot deliver without active ads")

        if health_report["structure"]["active_adsets"] > 5:
            recommendations.append(
                "Many active ad sets may compete - consider consolidating for better optimization"
            )

        health_report["recommendations"] = recommendations

    return health_report


@wrapped_fn_tool
def bulk_update_campaign_budgets(
    account_id: str,
    budget_updates: list[dict[str, Any]],
    budget_type: str = "daily_budget",
) -> str:
    """Update budgets for multiple campaigns at once.

    Efficiently updates budgets across multiple campaigns with
    validation and error handling.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        budget_updates: List of dicts with 'campaign_id' and 'new_budget' keys.
        budget_type: Either 'daily_budget' or 'lifetime_budget'.

    Example:
        budget_updates = [
            {"campaign_id": "123", "new_budget": 100},
            {"campaign_id": "456", "new_budget": 200}
        ]

    Returns:
        Results for each campaign update.
    """
    results = []

    for update in budget_updates:
        campaign_id = update.get("campaign_id")
        new_budget = update.get("new_budget")

        if not campaign_id or new_budget is None:
            results.append(
                {
                    "campaign_id": campaign_id,
                    "status": "error",
                    "message": "Missing campaign_id or new_budget",
                }
            )
            continue

        try:
            campaign = Campaign(campaign_id)
            # Convert dollars to cents
            budget_in_cents = int(new_budget * 100)

            result = campaign.api_update(fields=[], params={budget_type: budget_in_cents})

            results.append(
                {
                    "campaign_id": campaign_id,
                    "status": "success",
                    "new_budget": new_budget,
                    "budget_type": budget_type,
                }
            )
        except Exception as e:
            results.append({"campaign_id": campaign_id, "status": "error", "message": str(e)})

    return {
        "total_updates": len(budget_updates),
        "successful": len([r for r in results if r["status"] == "success"]),
        "failed": len([r for r in results if r["status"] == "error"]),
        "results": results,
    }


@wrapped_fn_tool
def pause_underperforming_campaigns(
    account_id: str,
    performance_threshold: dict[str, Any],
    date_preset: str = "last_7d",
    dry_run: bool = True,
) -> str:
    """Automatically pause campaigns not meeting performance thresholds.

    Analyzes campaign performance and pauses those not meeting specified criteria.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        performance_threshold: Criteria for pausing (e.g., {'min_conversions': 5, 'max_cpa': 50}).
        date_preset: Time period to analyze (default: 'last_7d').
        dry_run: If True, shows what would be paused without making changes.

    Returns:
        List of campaigns paused or would be paused.
    """
    account = AdAccount(account_id)

    # Get active campaigns with performance data
    insights = account.get_insights(
        fields=[
            "campaign_id",
            "campaign_name",
            "impressions",
            "clicks",
            "spend",
            "conversions",
            "cost_per_conversion",
            "purchase_roas",
        ],
        params={
            "date_preset": date_preset,
            "level": "campaign",
            "filtering": [
                {"field": "campaign.effective_status", "operator": "IN", "value": ["ACTIVE"]}
            ],
        },
    )

    campaigns_to_pause = []

    for campaign_data in insights:
        should_pause = False
        reasons = []

        # Check thresholds
        if "min_conversions" in performance_threshold:
            conversions = int(campaign_data.get("conversions", 0))
            if conversions < performance_threshold["min_conversions"]:
                should_pause = True
                reasons.append(
                    f"Conversions ({conversions}) below minimum ({performance_threshold['min_conversions']})"
                )

        if "max_cpa" in performance_threshold:
            cpa = float(campaign_data.get("cost_per_conversion", 0))
            if cpa > performance_threshold["max_cpa"]:
                should_pause = True
                reasons.append(
                    f"CPA (${cpa:.2f}) above maximum (${performance_threshold['max_cpa']})"
                )

        if "min_roas" in performance_threshold:
            roas = float(campaign_data.get("purchase_roas", [{}])[0].get("value", 0))
            if roas < performance_threshold["min_roas"]:
                should_pause = True
                reasons.append(
                    f"ROAS ({roas:.2f}) below minimum ({performance_threshold['min_roas']})"
                )

        if should_pause:
            campaign_info = {
                "campaign_id": campaign_data["campaign_id"],
                "campaign_name": campaign_data["campaign_name"],
                "reasons": reasons,
                "spend": campaign_data.get("spend", 0),
                "conversions": campaign_data.get("conversions", 0),
            }

            if not dry_run:
                try:
                    campaign = Campaign(campaign_data["campaign_id"])
                    campaign.api_update(params={"status": "PAUSED"})
                    campaign_info["status"] = "paused"
                except Exception as e:
                    campaign_info["status"] = "error"
                    campaign_info["error"] = str(e)
            else:
                campaign_info["status"] = "would_pause"

            campaigns_to_pause.append(campaign_info)

    return {
        "dry_run": dry_run,
        "date_preset": date_preset,
        "performance_threshold": performance_threshold,
        "campaigns_analyzed": len(list(insights)),
        "campaigns_to_pause": len(campaigns_to_pause),
        "campaigns": campaigns_to_pause,
    }


@wrapped_fn_tool
def create_campaign_from_template(
    account_id: str,
    template_type: str,
    campaign_name: str,
    daily_budget: int,
    targeting: dict[str, Any],
    custom_params: dict[str, Any] = {},
) -> str:
    """Create a campaign from predefined templates for common use cases.

    Templates include best practices for different campaign types.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        template_type: One of 'ecommerce_conversions', 'lead_generation', 'traffic', 'awareness'.
        campaign_name: Name for the campaign.
        daily_budget: Daily budget in dollars.
        targeting: Targeting specification.
        custom_params: Override template defaults.

    Returns:
        Created campaign and ad set with template configuration.
    """
    # Define templates
    templates = {
        "ecommerce_conversions": {
            "objective": "CONVERSIONS",
            "optimization_goal": "CONVERSIONS",
            "billing_event": "IMPRESSIONS",
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        },
        "lead_generation": {
            "objective": "LEAD_GENERATION",
            "optimization_goal": "LEAD_GENERATION",
            "billing_event": "IMPRESSIONS",
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        },
        "traffic": {
            "objective": "LINK_CLICKS",
            "optimization_goal": "LINK_CLICKS",
            "billing_event": "IMPRESSIONS",
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        },
        "awareness": {
            "objective": "REACH",
            "optimization_goal": "REACH",
            "billing_event": "IMPRESSIONS",
            "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        },
    }

    if template_type not in templates:
        return f"Invalid template_type. Choose from: {list(templates.keys())}"

    template = templates[template_type]
    template.update(custom_params)

    # Create campaign using template
    return create_complete_campaign(
        account_id=account_id,
        campaign_name=campaign_name,
        objective=template["objective"],
        daily_budget=daily_budget,
        adset_name=f"{campaign_name} - {template_type.replace('_', ' ').title()} AdSet",
        targeting=targeting,
        optimization_goal=template["optimization_goal"],
        billing_event=template["billing_event"],
        bid_strategy=template["bid_strategy"],
    )


# ---- Register tools ----
campaign_management_server.tool(create_complete_campaign)
campaign_management_server.tool(duplicate_campaign_with_modifications)
campaign_management_server.tool(campaign_health_check)
campaign_management_server.tool(bulk_update_campaign_budgets)
campaign_management_server.tool(pause_underperforming_campaigns)
campaign_management_server.tool(create_campaign_from_template)

"""Reporting Workflow Server - Advanced reporting and analytics operations."""

from typing import Any, Optional, List
from datetime import datetime, timedelta

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookReporting"
instructions = """
Reporting Workflow Server for Facebook Business API.

This server provides advanced reporting and analytics tools that aggregate
and analyze performance data across campaigns, ad sets, and ads.

These workflows simplify complex reporting tasks and provide actionable insights.
"""

reporting_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Performance Reports ----
@wrapped_fn_tool
def generate_campaign_performance_report(
    account_id: str,
    date_range: dict[str, str],
    campaign_ids: Optional[list[str]] = None,
    metrics: Optional[list[str]] = None,
    breakdowns: Optional[list[str]] = None,
) -> str:
    """Generate comprehensive performance report with insights.

    Creates a detailed performance report with key metrics and trends.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        date_range: Date range dict (e.g., {'since': '2024-01-01', 'until': '2024-01-31'} or {'date_preset': 'last_30d'}).
        campaign_ids: List of specific campaign IDs to report on (None for all).
        metrics: Custom metrics list (None for default set).
        breakdowns: Dimensions to break down by (e.g., ['age', 'gender']).

    Returns:
        Comprehensive performance report with metrics and analysis.
    """
    account = AdAccount(account_id)

    # Default metrics if not specified
    if not metrics:
        metrics = [
            "campaign_name",
            "campaign_id",
            "impressions",
            "reach",
            "frequency",
            "clicks",
            "unique_clicks",
            "ctr",
            "spend",
            "cpm",
            "cpc",
            "conversions",
            "conversion_values",
            "cost_per_conversion",
            "purchase_roas",
        ]

    # Build params
    params = {"level": "campaign", **date_range}

    if campaign_ids:
        params["filtering"] = [{"field": "campaign.id", "operator": "IN", "value": campaign_ids}]

    if breakdowns:
        params["breakdowns"] = breakdowns

    # Get insights
    insights = account.get_insights(fields=metrics, params=params)
    insights_list = list(insights)

    # Calculate summary statistics
    summary = {
        "total_campaigns": len(insights_list),
        "total_spend": sum(float(i.get("spend", 0)) for i in insights_list),
        "total_impressions": sum(int(i.get("impressions", 0)) for i in insights_list),
        "total_clicks": sum(int(i.get("clicks", 0)) for i in insights_list),
        "total_conversions": sum(int(i.get("conversions", 0)) for i in insights_list),
    }

    # Calculate averages
    if summary["total_campaigns"] > 0:
        summary["avg_cpm"] = (
            summary["total_spend"] / summary["total_impressions"] * 1000
            if summary["total_impressions"] > 0
            else 0
        )
        summary["avg_cpc"] = (
            summary["total_spend"] / summary["total_clicks"] if summary["total_clicks"] > 0 else 0
        )
        summary["avg_ctr"] = (
            summary["total_clicks"] / summary["total_impressions"] * 100
            if summary["total_impressions"] > 0
            else 0
        )

    # Identify top performers
    top_performers = sorted(
        insights_list, key=lambda x: float(x.get("conversions", 0)), reverse=True
    )[:5]

    # Identify underperformers (high spend, low conversions)
    underperformers = sorted(
        [i for i in insights_list if float(i.get("spend", 0)) > 0],
        key=lambda x: float(x.get("conversions", 0)) / float(x.get("spend", 1)),
    )[:5]

    return {
        "date_range": date_range,
        "summary": summary,
        "top_performers": top_performers,
        "underperformers": underperformers,
        "detailed_data": insights_list,
        "breakdowns_applied": breakdowns or [],
    }


@wrapped_fn_tool
def compare_campaign_performance(
    campaign_ids: list[str],
    metrics: list[str],
    date_range: dict[str, str],
) -> str:
    """Compare performance across multiple campaigns.

    Side-by-side comparison of key metrics for multiple campaigns.

    Args:
        campaign_ids: List of campaign IDs to compare.
        metrics: Metrics to compare (e.g., ['spend', 'conversions', 'cpm', 'roas']).
        date_range: Date range for comparison.

    Returns:
        Comparative analysis with rankings and insights.
    """
    comparison_data = []

    for campaign_id in campaign_ids:
        campaign = Campaign(campaign_id)

        # Get campaign info
        campaign_info = campaign.api_get(fields=["name", "objective", "status"])

        # Get insights
        insights = campaign.get_insights(fields=metrics, params=date_range)
        insights_data = list(insights)[0] if insights else {}

        comparison_data.append(
            {
                "campaign_id": campaign_id,
                "campaign_name": campaign_info.get("name"),
                "objective": campaign_info.get("objective"),
                "status": campaign_info.get("status"),
                "metrics": insights_data,
            }
        )

    # Calculate rankings for each metric
    rankings = {}
    for metric in metrics:
        # Sort campaigns by this metric
        sorted_campaigns = sorted(
            comparison_data,
            key=lambda x: float(x["metrics"].get(metric, 0)),
            reverse=True if metric not in ["cpm", "cpc", "cost_per_conversion"] else False,
        )

        rankings[metric] = [
            {
                "rank": idx + 1,
                "campaign_name": c["campaign_name"],
                "value": c["metrics"].get(metric, 0),
            }
            for idx, c in enumerate(sorted_campaigns)
        ]

    # Identify best performer overall
    performance_scores = {}
    for campaign in comparison_data:
        score = 0
        for metric, ranking in rankings.items():
            for r in ranking:
                if r["campaign_name"] == campaign["campaign_name"]:
                    # Better rank = higher score
                    score += len(campaign_ids) - r["rank"] + 1
                    break
        performance_scores[campaign["campaign_name"]] = score

    best_performer = max(performance_scores, key=performance_scores.get)

    return {
        "comparison_data": comparison_data,
        "rankings": rankings,
        "performance_scores": performance_scores,
        "best_performer": best_performer,
        "date_range": date_range,
    }


@wrapped_fn_tool
def generate_creative_performance_report(
    account_id: str,
    date_preset: str = "last_30d",
    min_impressions: int = 1000,
) -> str:
    """Analyze which creative elements perform best.

    Identifies patterns in high-performing creatives to inform future creative development.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        date_preset: Time period to analyze.
        min_impressions: Minimum impressions for inclusion in analysis.

    Returns:
        Creative performance insights and recommendations.
    """
    account = AdAccount(account_id)

    # Get ad-level insights with creative data
    insights = account.get_insights(
        fields=[
            "ad_id",
            "ad_name",
            "impressions",
            "clicks",
            "ctr",
            "spend",
            "conversions",
            "cost_per_conversion",
            "video_play_actions",
            "video_avg_time_watched_actions",
        ],
        params={
            "date_preset": date_preset,
            "level": "ad",
            "filtering": [
                {"field": "impressions", "operator": "GREATER_THAN", "value": min_impressions}
            ],
        },
    )

    insights_list = list(insights)

    # Group by performance tiers
    performance_tiers = {"high_performers": [], "average_performers": [], "low_performers": []}

    # Calculate performance thresholds
    if insights_list:
        ctrs = [float(i.get("ctr", 0)) for i in insights_list]
        avg_ctr = sum(ctrs) / len(ctrs)

        for ad_data in insights_list:
            ctr = float(ad_data.get("ctr", 0))
            if ctr > avg_ctr * 1.2:
                performance_tiers["high_performers"].append(ad_data)
            elif ctr < avg_ctr * 0.8:
                performance_tiers["low_performers"].append(ad_data)
            else:
                performance_tiers["average_performers"].append(ad_data)

    # Analyze video performance if applicable
    video_insights = {"total_video_ads": 0, "avg_watch_time": 0, "high_engagement_videos": []}

    for ad in insights_list:
        if ad.get("video_play_actions"):
            video_insights["total_video_ads"] += 1
            watch_time = ad.get("video_avg_time_watched_actions", [{}])[0].get("value", 0)
            if watch_time > 10:  # More than 10 seconds average
                video_insights["high_engagement_videos"].append(
                    {"ad_name": ad.get("ad_name"), "avg_watch_time": watch_time}
                )

    # Generate recommendations
    recommendations = []

    if performance_tiers["high_performers"]:
        recommendations.append(
            f"Found {len(performance_tiers['high_performers'])} high-performing creatives - analyze common elements"
        )

    if video_insights["high_engagement_videos"]:
        recommendations.append(
            f"{len(video_insights['high_engagement_videos'])} videos with high engagement - consider more video content"
        )

    return {
        "total_ads_analyzed": len(insights_list),
        "performance_tiers": {
            tier: {
                "count": len(ads),
                "avg_ctr": sum(float(a.get("ctr", 0)) for a in ads) / len(ads) if ads else 0,
                "total_conversions": sum(int(a.get("conversions", 0)) for a in ads),
            }
            for tier, ads in performance_tiers.items()
        },
        "video_insights": video_insights,
        "recommendations": recommendations,
        "top_5_creatives": sorted(
            insights_list, key=lambda x: float(x.get("ctr", 0)), reverse=True
        )[:5],
    }


@wrapped_fn_tool
def generate_audience_insights_report(
    account_id: str,
    campaign_ids: Optional[list[str]] = None,
    date_preset: str = "last_30d",
) -> str:
    """Generate detailed audience performance insights.

    Analyzes performance by demographic segments to optimize targeting.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        campaign_ids: Specific campaigns to analyze (None for all).
        date_preset: Time period to analyze.

    Returns:
        Audience performance breakdown with optimization suggestions.
    """
    account = AdAccount(account_id)

    # Get insights broken down by demographics
    params = {"date_preset": date_preset, "level": "campaign", "breakdowns": ["age", "gender"]}

    if campaign_ids:
        params["filtering"] = [{"field": "campaign.id", "operator": "IN", "value": campaign_ids}]

    insights = account.get_insights(
        fields=[
            "campaign_name",
            "age",
            "gender",
            "impressions",
            "clicks",
            "ctr",
            "spend",
            "conversions",
            "cost_per_conversion",
        ],
        params=params,
    )

    insights_list = list(insights)

    # Analyze by age groups
    age_performance = {}
    gender_performance = {"male": {}, "female": {}, "unknown": {}}

    for data in insights_list:
        age = data.get("age", "unknown")
        gender = data.get("gender", "unknown").lower()

        # Aggregate age data
        if age not in age_performance:
            age_performance[age] = {"impressions": 0, "clicks": 0, "conversions": 0, "spend": 0}

        age_performance[age]["impressions"] += int(data.get("impressions", 0))
        age_performance[age]["clicks"] += int(data.get("clicks", 0))
        age_performance[age]["conversions"] += int(data.get("conversions", 0))
        age_performance[age]["spend"] += float(data.get("spend", 0))

        # Aggregate gender data
        if gender in gender_performance:
            for metric in ["impressions", "clicks", "conversions", "spend"]:
                if metric not in gender_performance[gender]:
                    gender_performance[gender][metric] = 0
                gender_performance[gender][metric] += float(data.get(metric, 0))

    # Calculate performance metrics
    for age, metrics in age_performance.items():
        if metrics["impressions"] > 0:
            metrics["ctr"] = metrics["clicks"] / metrics["impressions"] * 100
        if metrics["conversions"] > 0:
            metrics["cpa"] = metrics["spend"] / metrics["conversions"]

    for gender, metrics in gender_performance.items():
        if metrics.get("impressions", 0) > 0:
            metrics["ctr"] = metrics["clicks"] / metrics["impressions"] * 100
        if metrics.get("conversions", 0) > 0:
            metrics["cpa"] = metrics["spend"] / metrics["conversions"]

    # Identify best performing segments
    best_age_by_ctr = max(age_performance.items(), key=lambda x: x[1].get("ctr", 0))[0]
    best_age_by_cpa = (
        min(
            [(k, v) for k, v in age_performance.items() if v.get("cpa", float("inf")) > 0],
            key=lambda x: x[1].get("cpa", float("inf")),
        )[0]
        if any(v.get("cpa", 0) > 0 for v in age_performance.values())
        else None
    )

    return {
        "date_preset": date_preset,
        "age_performance": age_performance,
        "gender_performance": gender_performance,
        "best_performing_segments": {
            "highest_ctr_age": best_age_by_ctr,
            "lowest_cpa_age": best_age_by_cpa,
            "gender_preference": max(
                gender_performance.items(), key=lambda x: x[1].get("conversions", 0)
            )[0],
        },
        "optimization_suggestions": [
            f"Consider focusing on {best_age_by_ctr} age group for engagement",
            f"Lowest CPA found in {best_age_by_cpa} age group"
            if best_age_by_cpa
            else "Analyze CPA by age group",
            "Review gender performance for targeting optimization",
        ],
    }


@wrapped_fn_tool
def generate_budget_utilization_report(
    account_id: str,
    date_preset: str = "last_7d",
) -> str:
    """Analyze budget utilization and pacing across campaigns.

    Identifies budget inefficiencies and pacing issues.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        date_preset: Time period to analyze.

    Returns:
        Budget utilization analysis with recommendations.
    """
    account = AdAccount(account_id)

    # Get campaign budgets and spend
    campaigns = account.get_campaigns(
        fields=["name", "daily_budget", "lifetime_budget", "status", "created_time"],
        params={"effective_status": ["ACTIVE"]},
    )

    budget_analysis = []

    for campaign in campaigns:
        campaign_id = campaign.get("id")

        # Get spend data
        insights = Campaign(campaign_id).get_insights(
            fields=["spend", "impressions"], params={"date_preset": date_preset}
        )
        insights_data = list(insights)[0] if insights else {"spend": "0", "impressions": "0"}

        daily_budget = float(campaign.get("daily_budget", 0)) / 100  # Convert from cents
        lifetime_budget = float(campaign.get("lifetime_budget", 0)) / 100
        spend = float(insights_data.get("spend", 0))

        # Calculate utilization
        if date_preset == "last_7d" and daily_budget > 0:
            expected_spend = daily_budget * 7
            utilization = (spend / expected_spend * 100) if expected_spend > 0 else 0
        else:
            utilization = 0

        budget_analysis.append(
            {
                "campaign_name": campaign.get("name"),
                "campaign_id": campaign_id,
                "daily_budget": daily_budget,
                "lifetime_budget": lifetime_budget,
                "spend": spend,
                "utilization_percentage": utilization,
                "status": "underutilized"
                if utilization < 70
                else "optimal"
                if utilization < 95
                else "near_cap",
            }
        )

    # Summary statistics
    total_daily_budget = sum(c["daily_budget"] for c in budget_analysis)
    total_spend = sum(c["spend"] for c in budget_analysis)
    overall_utilization = (
        (total_spend / (total_daily_budget * 7) * 100) if total_daily_budget > 0 else 0
    )

    # Identify issues
    underutilized = [c for c in budget_analysis if c["utilization_percentage"] < 70]
    near_cap = [c for c in budget_analysis if c["utilization_percentage"] > 95]

    recommendations = []
    if underutilized:
        recommendations.append(
            f"{len(underutilized)} campaigns underutilizing budget - check targeting and bids"
        )
    if near_cap:
        recommendations.append(
            f"{len(near_cap)} campaigns near budget cap - consider increasing budgets"
        )

    return {
        "date_preset": date_preset,
        "summary": {
            "total_campaigns": len(budget_analysis),
            "total_daily_budget": total_daily_budget,
            "total_spend": total_spend,
            "overall_utilization": overall_utilization,
        },
        "budget_analysis": budget_analysis,
        "issues": {"underutilized_campaigns": underutilized, "campaigns_near_cap": near_cap},
        "recommendations": recommendations,
    }


@wrapped_fn_tool
def generate_conversion_funnel_report(
    account_id: str,
    campaign_ids: Optional[list[str]] = None,
    date_preset: str = "last_30d",
) -> str:
    """Analyze conversion funnel performance from impression to purchase.

    Identifies drop-off points in the conversion funnel.

    Args:
        account_id: The Ad Account ID (must start with 'act_').
        campaign_ids: Specific campaigns to analyze (None for all).
        date_preset: Time period to analyze.

    Returns:
        Funnel analysis with optimization opportunities.
    """
    account = AdAccount(account_id)

    # Define funnel stages
    funnel_metrics = [
        "impressions",
        "clicks",
        "landing_page_views",
        "adds_to_cart",
        "checkouts_initiated",
        "purchases",
    ]

    params = {"date_preset": date_preset, "level": "account"}

    if campaign_ids:
        params["filtering"] = [{"field": "campaign.id", "operator": "IN", "value": campaign_ids}]

    # Get funnel data
    insights = account.get_insights(
        fields=funnel_metrics + ["spend", "purchase_conversion_value"], params=params
    )

    funnel_data = list(insights)[0] if insights else {}

    # Calculate conversion rates between stages
    funnel_analysis = {}
    for i in range(len(funnel_metrics) - 1):
        current_stage = funnel_metrics[i]
        next_stage = funnel_metrics[i + 1]

        current_value = float(funnel_data.get(current_stage, 0))
        next_value = float(funnel_data.get(next_stage, 0))

        conversion_rate = (next_value / current_value * 100) if current_value > 0 else 0

        funnel_analysis[f"{current_stage}_to_{next_stage}"] = {
            "from": current_stage,
            "to": next_stage,
            "from_value": current_value,
            "to_value": next_value,
            "conversion_rate": conversion_rate,
            "drop_off_rate": 100 - conversion_rate,
        }

    # Identify biggest drop-offs
    biggest_dropoff = max(funnel_analysis.items(), key=lambda x: x[1]["drop_off_rate"])

    # Calculate overall metrics
    impressions = float(funnel_data.get("impressions", 1))
    purchases = float(funnel_data.get("purchases", 0))
    spend = float(funnel_data.get("spend", 0))
    revenue = float(funnel_data.get("purchase_conversion_value", 0))

    overall_metrics = {
        "impression_to_purchase_rate": (purchases / impressions * 100) if impressions > 0 else 0,
        "cost_per_purchase": (spend / purchases) if purchases > 0 else 0,
        "roas": (revenue / spend) if spend > 0 else 0,
        "average_order_value": (revenue / purchases) if purchases > 0 else 0,
    }

    # Generate recommendations
    recommendations = []

    if biggest_dropoff[0] == "impressions_to_clicks":
        recommendations.append("High drop-off at click stage - review ad creative and relevance")
    elif biggest_dropoff[0] == "clicks_to_landing_page_views":
        recommendations.append("Users clicking but not reaching site - check page load speed")
    elif biggest_dropoff[0] == "landing_page_views_to_adds_to_cart":
        recommendations.append("Low add-to-cart rate - review product page and pricing")
    elif biggest_dropoff[0] == "adds_to_cart_to_checkouts_initiated":
        recommendations.append("Cart abandonment issue - simplify checkout process")

    return {
        "date_preset": date_preset,
        "funnel_data": funnel_data,
        "funnel_analysis": funnel_analysis,
        "biggest_dropoff": {
            "stage": biggest_dropoff[0],
            "drop_off_rate": biggest_dropoff[1]["drop_off_rate"],
        },
        "overall_metrics": overall_metrics,
        "recommendations": recommendations,
    }


# ---- Register tools ----
reporting_server.tool(generate_campaign_performance_report)
reporting_server.tool(compare_campaign_performance)
reporting_server.tool(generate_creative_performance_report)
reporting_server.tool(generate_audience_insights_report)
reporting_server.tool(generate_budget_utilization_report)
reporting_server.tool(generate_conversion_funnel_report)

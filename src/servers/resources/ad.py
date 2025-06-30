"""Streamlined Ad MCP Server - Core Operations Only."""

from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.generated.models.ad_models import AdFields
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAd"
instructions = """
Ad MCP Server for Facebook Business API - Core Operations.

For common workflows, use the universal server or workflow servers.
This server provides essential operations that handle 80% of use cases.

Use `run_any_ad_fn` for any operations not covered here.
"""

ad_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_ad(
    ad_id: str,
    fields: list[str] = [],
) -> str:
    """Get an Ad object by ID.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve. Available fields include:
            - name: Ad name
            - status: Current status (ACTIVE, PAUSED, DELETED, ARCHIVED)
            - effective_status: Actual delivery status (see AdEffectiveStatus)
            - adset_id: Parent ad set ID
            - campaign_id: Parent campaign ID
            - creative: Associated creative object
            - bid_amount: Bid amount if using manual bidding
            - created_time/updated_time: Timestamps
            See AdFields for all available fields.
    """
    return Ad(ad_id).api_get(fields=fields)


@wrapped_fn_tool
def update_ad(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Update an Ad object.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to return after update.
        params: Parameters to update. Common updates:
            - name: Change ad name
            - status: ACTIVE or PAUSED (see AdStatus enum)
            - creative: Change creative by providing new creative ID
            - tracking_specs: Update tracking pixels
            - adlabels: Add or update ad labels for organization
            Note: Most targeting and optimization settings are at ad set level.
    """
    return Ad(ad_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad(
    ad_id: str,
) -> str:
    """Delete an Ad.

    Args:
        ad_id: The ID of the Ad to delete.
    """
    return Ad(ad_id).api_delete()


# ---- Creative Management (1) ----
@wrapped_fn_tool
def get_ad_creatives(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get ad creatives for this ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Fields to retrieve:
            - name: Creative name
            - object_story_spec: Post/link specification
            - title: Ad title text
            - body: Ad body text
            - image_url: URL of the ad image
            - video_id: ID of video if video ad
            - call_to_action_type: Button text (LEARN_MORE, SHOP_NOW, etc.)
            - link_url: Destination URL
        params: Query parameters.
    """
    return Ad(ad_id).get_ad_creatives(fields=fields, params=params)


# ---- Performance Analysis (1) ----
@wrapped_fn_tool
def get_insights(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get insights (performance data) for this ad.

    Args:
        ad_id: The ID of the Ad.
        fields: Metrics to retrieve. Common metrics:
            - impressions: Number of times ad was shown
            - reach: Unique people who saw the ad
            - frequency: Average times each person saw ad
            - clicks: All clicks (link clicks + other)
            - unique_clicks: Unique people who clicked
            - spend: Amount spent on this ad
            - cpm/cpc/ctr: Cost and performance rates
            - conversions: Conversions by type
            - video_avg_time_watched_actions: Video metrics
            - cost_per_action_type: Cost per conversion type
        params: Query parameters:
            - date_preset: last_7d, last_30d, lifetime (see AdDatePreset)
            - breakdowns: ['age', 'gender', 'placement', 'impression_device']
            - use_unified_attribution_setting: true for cross-device attribution
    """
    return Ad(ad_id).get_insights(fields=fields, params=params)


# ---- Dynamic Fallback (1) ----
@wrapped_fn_tool
def run_any_ad_fn(
    ad_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically call any method on the Ad object.

    Use this for operations not covered by the core tools above.
    Example: run_any_ad_fn('123', 'get_previews', [], {'ad_format': 'DESKTOP_FEED_STANDARD'})

    Args:
        ad_id: The ID of the Ad.
        fn: Method name to call on Ad object.
        args: Positional arguments for the method.
        kwargs: Keyword arguments for the method.
    """
    ad = Ad(ad_id)
    if not hasattr(ad, fn):
        return f"Ad does not have method '{fn}'. Check the Facebook Business SDK documentation."
    f = getattr(ad, fn)
    if not callable(f):
        return f"{fn} is not a callable method on Ad."
    return str(f(*args, **kwargs))


# ---- Register tools ----
ad_server.tool(get_ad)
ad_server.tool(update_ad)
ad_server.tool(delete_ad)
ad_server.tool(get_ad_creatives)
ad_server.tool(get_insights)
ad_server.tool(run_any_ad_fn)

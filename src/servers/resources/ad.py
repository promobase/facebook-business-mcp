"""Streamlined Ad MCP Server - Core Operations Only."""

from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

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
        fields: Fields to retrieve (e.g., ['name', 'status', 'adset_id', 'creative']).
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
        params: Parameters to update (e.g., {'name': 'New Name', 'status': 'PAUSED'}).
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
        fields: Fields to retrieve (e.g., ['name', 'object_story_spec', 'image_url']).
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
        fields: Metrics to retrieve (e.g., ['impressions', 'clicks', 'spend', 'cpm', 'ctr']).
        params: Query parameters (e.g., {'date_preset': 'last_7d', 'breakdowns': ['age', 'gender']}).
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

"""Streamlined AdSet MCP Server - Core Operations Only."""

from typing import Any

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdSet"
instructions = """
AdSet MCP Server for Facebook Business API - Core Operations.

For common workflows, use the universal server or workflow servers.
This server provides essential operations that handle 80% of use cases.

Use `run_any_adset_fn` for any operations not covered here.
"""

adset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@wrapped_fn_tool
def get_adset(
    adset_id: str,
    fields: list[str] = [],
) -> str:
    """Get an AdSet object by ID.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve (e.g., ['name', 'status', 'daily_budget', 'targeting']).
    """
    return AdSet(adset_id).api_get(fields=fields)


@wrapped_fn_tool
def update_adset(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Update an AdSet object.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to return after update.
        params: Parameters to update (e.g., {'name': 'New Name', 'daily_budget': 5000}).
    """
    return AdSet(adset_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_adset(
    adset_id: str,
) -> str:
    """Delete an AdSet.

    Args:
        adset_id: The ID of the AdSet to delete.
    """
    return AdSet(adset_id).api_delete()


# ---- Child Resource Access (1) ----
@wrapped_fn_tool
def get_ads(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get ads for this ad set.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve (e.g., ['name', 'status', 'creative']).
        params: Query parameters (e.g., {'limit': 100, 'effective_status': ['ACTIVE']}).
    """
    return AdSet(adset_id).get_ads(fields=fields, params=params)


# ---- Performance Analysis (2) ----
@wrapped_fn_tool
def get_insights(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get insights (performance data) for this ad set.

    Args:
        adset_id: The ID of the AdSet.
        fields: Metrics to retrieve (e.g., ['impressions', 'clicks', 'spend', 'cpm', 'ctr']).
        params: Query parameters (e.g., {'date_preset': 'last_7d', 'breakdowns': ['age', 'gender']}).
    """
    return AdSet(adset_id).get_insights(fields=fields, params=params)


@wrapped_fn_tool
def get_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    """Get delivery estimate for this ad set.

    Shows estimated daily results including reach, impressions, and spend.
    Useful for understanding ad set potential before launch.

    Args:
        adset_id: The ID of the AdSet.
        fields: Fields to retrieve.
        params: Estimation parameters.
    """
    return AdSet(adset_id).get_delivery_estimate(fields=fields, params=params)


# ---- Dynamic Fallback (1) ----
@wrapped_fn_tool
def run_any_adset_fn(
    adset_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically call any method on the AdSet object.

    Use this for operations not covered by the core tools above.
    Example: run_any_adset_fn('123', 'get_targeting_sentence_lines', [], {})

    Args:
        adset_id: The ID of the AdSet.
        fn: Method name to call on AdSet object.
        args: Positional arguments for the method.
        kwargs: Keyword arguments for the method.
    """
    adset = AdSet(adset_id)
    if not hasattr(adset, fn):
        return f"AdSet does not have method '{fn}'. Check the Facebook Business SDK documentation."
    f = getattr(adset, fn)
    if not callable(f):
        return f"{fn} is not a callable method on AdSet."
    return str(f(*args, **kwargs))


# ---- Register tools ----
adset_server.tool(get_adset)
adset_server.tool(update_adset)
adset_server.tool(delete_adset)
adset_server.tool(get_ads)
adset_server.tool(get_insights)
adset_server.tool(get_delivery_estimate)
adset_server.tool(run_any_adset_fn)

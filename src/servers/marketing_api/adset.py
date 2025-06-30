"""AdSet MCP Server using Facebook Business SDK."""

import inspect
from typing import Any

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
    wrapped_fn_tool,
)

#  ---- constants ----
server_name = "FacebookAdSet"
instructions = """
This is the AdSet MCP Server for managing Facebook Ad Sets. You have specific methods that wrap around the AdSet object.

If the tools are not available to you, use the `get_usage_on_adset` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_adset_fn.` tool to call any method on the AdSet object.
"""

adset_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


#  ---- Core API methods ----
@wrapped_fn_tool
def get_adset(
    adset_id: str,
    fields: list[str] = [],
) -> str:
    return AdSet(adset_id).api_get(fields=fields)


@wrapped_fn_tool
def update_adset(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_adset(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).api_delete(fields=fields, params=params)


#  ---- Ad management ----
@wrapped_fn_tool
def get_ads(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_ads(fields=fields, params=params)


#  ---- Creative management ----
@wrapped_fn_tool
def get_ad_creatives(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_ad_creatives(fields=fields, params=params)


#  ---- Insights and estimates ----
@wrapped_fn_tool
def get_insights(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    is_async: bool = False,
) -> str:
    return AdSet(adset_id).get_insights(fields=fields, params=params, is_async=is_async)


@wrapped_fn_tool
def get_insights_async(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_insights_async(fields=fields, params=params)


@wrapped_fn_tool
def get_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_delivery_estimate(fields=fields, params=params)


@wrapped_fn_tool
def get_message_delivery_estimate(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_message_delivery_estimate(fields=fields, params=params)


#  ---- Targeting ----
@wrapped_fn_tool
def get_targeting_sentence_lines(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_targeting_sentence_lines(fields=fields, params=params)


#  ---- Activities and studies ----
@wrapped_fn_tool
def get_activities(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_activities(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_studies(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_ad_studies(fields=fields, params=params)


#  ---- Advanced features ----
@wrapped_fn_tool
def create_ad_label(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).create_ad_label(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad_labels(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).delete_ad_labels(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_rules_governed(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_ad_rules_governed(fields=fields, params=params)


@wrapped_fn_tool
def get_async_ad_requests(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_async_ad_requests(fields=fields, params=params)


@wrapped_fn_tool
def create_budget_schedule(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).create_budget_schedule(fields=fields, params=params)


@wrapped_fn_tool
def get_copies(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).get_copies(fields=fields, params=params)


@wrapped_fn_tool
def create_copy(
    adset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdSet(adset_id).create_copy(fields=fields, params=params)


#  ---- Dynamic tools ----
@log_execution
@handle_facebook_errors
def get_usage_on_adset(
    fn: str | None = None,
) -> str:
    """ALWAYS use this tool first.
    Provides info on how to use the tools and methods available. This includes examples.
    Optionally, you can pass in a method name and you will see the src code for usage of that method.
    """
    field_enum_info: dict = AdSet._get_field_enum_info()
    methods = list_callable_methods(AdSet)

    usage = f"""
    This is the AdSet wrapper on Facebook Business Python SDK. 
    You can use the {run_any_adset_fn.__name__} tool to call any methods, here is the docstring for it: {run_any_adset_fn.__doc__}

    Available methods:
    methods: {methods}
    here are the ALL field types possible. NOTE that for each operation, you only need a subset. refer to the methods' src code for details.
    field_types: {AdSet._field_types}
    field_enum_info: {field_enum_info}

    Examples:
    here are some code examples. The underlying is graph API. it relies on fields & params.

    adset = AdSet(..)
    adset.get_ads(fields=[..], params=..) // get ads
    adset.get_insights(fields=[..], params=..) // get insights
    adset.get_delivery_estimate(fields=[..], params=..) // get delivery estimate
    adset.api_update(fields=[..], params=..) // update ad set
    """

    if fn:
        # append method src
        if hasattr(AdSet, fn):
            method = getattr(AdSet, fn)
            if callable(method):
                usage += f"\n\nHere is the source code for {fn}:\n{safe_getsource(method)}"
            else:
                usage += f"\n\n{fn} is not a callable method on AdSet."
    return usage


@log_execution
@handle_facebook_errors
def run_any_adset_fn(
    adset_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically calls a method on the AdSet object.
    takes in an adset_id, method name (fn), and optional args/kwargs.
    it will be called like this:
    ```adset = AdSet(adset_id)
    result = getattr(adset, fn)(*args, **kwargs)
    ```
    """
    adset = AdSet(adset_id)
    if not hasattr(adset, fn):
        return f"AdSet does not have method '{fn}'. use the {get_usage_on_adset.__name__} tool to see available methods & usage."
    f = getattr(adset, fn)
    if not callable(f):
        return f"{fn} is not a callable method on AdSet."
    return str(f(*args, **kwargs))


# ---- tool docstrings ----

fields_src = inspect.getsource(AdSet.Field)

# Core API methods
get_adset.__doc__ = f"""Get an AdSet object by ID.
adset_id: The ID of the AdSet
fields: {fields_src}

Source code:
{safe_getsource(AdSet.api_get)}
"""

update_adset.__doc__ = f"""Update an AdSet object.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Update parameters

Source code:
{safe_getsource(AdSet.api_update)}
"""

delete_adset.__doc__ = f"""Delete an AdSet.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Deletion parameters

Source code:
{safe_getsource(AdSet.api_delete)}
"""

# Ad management
get_ads.__doc__ = f"""Get ads for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_ads)}
"""

# Creative management
get_ad_creatives.__doc__ = f"""Get ad creatives for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_ad_creatives)}
"""

# Insights and estimates
get_insights.__doc__ = f"""Get insights for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Insights query parameters
is_async: Whether to run asynchronously

Source code:
{safe_getsource(AdSet.get_insights)}
"""

get_insights_async.__doc__ = f"""Get insights asynchronously for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Insights query parameters

Source code:
{safe_getsource(AdSet.get_insights_async)}
"""

get_delivery_estimate.__doc__ = f"""Get delivery estimate for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Estimation parameters

Source code:
{safe_getsource(AdSet.get_delivery_estimate)}
"""

get_message_delivery_estimate.__doc__ = f"""Get message delivery estimate for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Estimation parameters

Source code:
{safe_getsource(AdSet.get_message_delivery_estimate)}
"""

# Targeting
get_targeting_sentence_lines.__doc__ = f"""Get targeting sentence lines for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_targeting_sentence_lines)}
"""

# Activities and studies
get_activities.__doc__ = f"""Get activities for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_activities)}
"""

get_ad_studies.__doc__ = f"""Get ad studies for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_ad_studies)}
"""

# Advanced features
create_ad_label.__doc__ = f"""Create an ad label for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Label creation parameters

Source code:
{safe_getsource(AdSet.create_ad_label)}
"""

delete_ad_labels.__doc__ = f"""Delete ad labels from this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Label deletion parameters

Source code:
{safe_getsource(AdSet.delete_ad_labels)}
"""

get_ad_rules_governed.__doc__ = f"""Get ad rules that govern this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_ad_rules_governed)}
"""

get_async_ad_requests.__doc__ = f"""Get async ad requests for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_async_ad_requests)}
"""

create_budget_schedule.__doc__ = f"""Create budget schedule for this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Budget schedule parameters

Source code:
{safe_getsource(AdSet.create_budget_schedule)}
"""

get_copies.__doc__ = f"""Get copies of this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdSet.get_copies)}
"""

create_copy.__doc__ = f"""Create a copy of this ad set.
adset_id: The ID of the AdSet
fields: Fields to retrieve
params: Copy parameters

Source code:
{safe_getsource(AdSet.create_copy)}
"""

# ---- register tools ----
# Core tools
adset_server.tool(get_usage_on_adset)
adset_server.tool(run_any_adset_fn)

# Core API methods
adset_server.tool(get_adset)
adset_server.tool(update_adset)
adset_server.tool(delete_adset)

# Ad management
adset_server.tool(get_ads)

# Creative management
adset_server.tool(get_ad_creatives)

# Insights and estimates
adset_server.tool(get_insights)
adset_server.tool(get_insights_async)
adset_server.tool(get_delivery_estimate)
adset_server.tool(get_message_delivery_estimate)

# Targeting
adset_server.tool(get_targeting_sentence_lines)

# Activities and studies
adset_server.tool(get_activities)
adset_server.tool(get_ad_studies)

# Advanced features
adset_server.tool(create_ad_label)
adset_server.tool(delete_ad_labels)
adset_server.tool(get_ad_rules_governed)
adset_server.tool(get_async_ad_requests)
adset_server.tool(create_budget_schedule)
adset_server.tool(get_copies)
adset_server.tool(create_copy)

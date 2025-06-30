"""Ad MCP Server using Facebook Business SDK."""

import inspect
from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
    wrapped_fn_tool,
)

#  ---- constants ----
server_name = "FacebookAd"
instructions = """
This is the Ad MCP Server for managing Facebook Ads. You have specific methods that wrap around the Ad object.

If the tools are not available to you, use the `get_usage_on_ad` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_ad_fn.` tool to call any method on the Ad object.
"""

ad_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


#  ---- Core API methods ----
@wrapped_fn_tool
def get_ad(
    ad_id: str,
    fields: list[str] = [],
) -> str:
    return Ad(ad_id).api_get(fields=fields)


@wrapped_fn_tool
def update_ad(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).api_delete(fields=fields, params=params)


#  ---- Creative management ----
@wrapped_fn_tool
def get_ad_creatives(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_ad_creatives(fields=fields, params=params)


#  ---- Insights ----
@wrapped_fn_tool
def get_insights(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    is_async: bool = False,
) -> str:
    return Ad(ad_id).get_insights(fields=fields, params=params, is_async=is_async)


@wrapped_fn_tool
def get_insights_async(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_insights_async(fields=fields, params=params)


#  ---- Preview and targeting ----
@wrapped_fn_tool
def get_previews(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_previews(fields=fields, params=params)


@wrapped_fn_tool
def get_targeting_sentence_lines(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_targeting_sentence_lines(fields=fields, params=params)


#  ---- Lead generation ----
@wrapped_fn_tool
def get_leads(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_leads(fields=fields, params=params)


#  ---- Advanced features ----
@wrapped_fn_tool
def create_ad_label(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).create_ad_label(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_rules_governed(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_ad_rules_governed(fields=fields, params=params)


@wrapped_fn_tool
def get_copies(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).get_copies(fields=fields, params=params)


@wrapped_fn_tool
def create_copy(
    ad_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Ad(ad_id).create_copy(fields=fields, params=params)


#  ---- Dynamic tools ----
@log_execution
@handle_facebook_errors
def get_usage_on_ad(
    fn: str | None = None,
) -> str:
    """ALWAYS use this tool first.
    Provides info on how to use the tools and methods available. This includes examples.
    Optionally, you can pass in a method name and you will see the src code for usage of that method.
    """
    field_enum_info: dict = Ad._get_field_enum_info()
    methods = list_callable_methods(Ad)

    usage = f"""
    This is the Ad wrapper on Facebook Business Python SDK. 
    You can use the {run_any_ad_fn.__name__} tool to call any methods, here is the docstring for it: {run_any_ad_fn.__doc__}

    Available methods:
    methods: {methods}
    here are the ALL field types possible. NOTE that for each operation, you only need a subset. refer to the methods' src code for details.
    field_types: {Ad._field_types}
    field_enum_info: {field_enum_info}

    Examples:
    here are some code examples. The underlying is graph API. it relies on fields & params.

    ad = Ad(..)
    ad.get_ad_creatives(fields=[..], params=..) // get ad creatives
    ad.get_insights(fields=[..], params=..) // get insights
    ad.get_previews(fields=[..], params=..) // get ad previews
    ad.api_update(fields=[..], params=..) // update ad
    """

    if fn:
        # append method src
        if hasattr(Ad, fn):
            method = getattr(Ad, fn)
            if callable(method):
                usage += f"\n\nHere is the source code for {fn}:\n{safe_getsource(method)}"
            else:
                usage += f"\n\n{fn} is not a callable method on Ad."
    return usage


@log_execution
@handle_facebook_errors
def run_any_ad_fn(
    ad_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically calls a method on the Ad object.
    takes in an ad_id, method name (fn), and optional args/kwargs.
    it will be called like this:
    ```ad = Ad(ad_id)
    result = getattr(ad, fn)(*args, **kwargs)
    ```
    """
    ad = Ad(ad_id)
    if not hasattr(ad, fn):
        return f"Ad does not have method '{fn}'. use the {get_usage_on_ad.__name__} tool to see available methods & usage."
    f = getattr(ad, fn)
    if not callable(f):
        return f"{fn} is not a callable method on Ad."
    return str(f(*args, **kwargs))


# ---- tool docstrings ----

fields_src = inspect.getsource(Ad.Field)

# Core API methods
get_ad.__doc__ = f"""Get an Ad object by ID.
ad_id: The ID of the Ad
fields: {fields_src}

Source code:
{safe_getsource(Ad.api_get)}
"""

update_ad.__doc__ = f"""Update an Ad object.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Update parameters

Source code:
{safe_getsource(Ad.api_update)}
"""

delete_ad.__doc__ = f"""Delete an Ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Deletion parameters

Source code:
{safe_getsource(Ad.api_delete)}
"""

# Creative management
get_ad_creatives.__doc__ = f"""Get ad creatives for this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Ad.get_ad_creatives)}
"""

# Insights
get_insights.__doc__ = f"""Get insights for this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Insights query parameters
is_async: Whether to run asynchronously

Source code:
{safe_getsource(Ad.get_insights)}
"""

get_insights_async.__doc__ = f"""Get insights asynchronously for this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Insights query parameters

Source code:
{safe_getsource(Ad.get_insights_async)}
"""

# Preview and targeting
get_previews.__doc__ = f"""Get previews for this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Preview parameters

Source code:
{safe_getsource(Ad.get_previews)}
"""

get_targeting_sentence_lines.__doc__ = f"""Get targeting sentence lines for this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Ad.get_targeting_sentence_lines)}
"""

# Lead generation
get_leads.__doc__ = f"""Get leads generated by this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Ad.get_leads)}
"""

# Advanced features
create_ad_label.__doc__ = f"""Create an ad label for this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Label creation parameters

Source code:
{safe_getsource(Ad.create_ad_label)}
"""

get_ad_rules_governed.__doc__ = f"""Get ad rules that govern this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Ad.get_ad_rules_governed)}
"""

get_copies.__doc__ = f"""Get copies of this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Ad.get_copies)}
"""

create_copy.__doc__ = f"""Create a copy of this ad.
ad_id: The ID of the Ad
fields: Fields to retrieve
params: Copy parameters

Source code:
{safe_getsource(Ad.create_copy)}
"""

# ---- register tools ----
# Core tools
ad_server.tool(get_usage_on_ad)
ad_server.tool(run_any_ad_fn)

# Core API methods
ad_server.tool(get_ad)
ad_server.tool(update_ad)
ad_server.tool(delete_ad)

# Creative management
ad_server.tool(get_ad_creatives)

# Insights
ad_server.tool(get_insights)
ad_server.tool(get_insights_async)

# Preview and targeting
ad_server.tool(get_previews)
ad_server.tool(get_targeting_sentence_lines)

# Lead generation
ad_server.tool(get_leads)

# Advanced features
ad_server.tool(create_ad_label)
ad_server.tool(get_ad_rules_governed)
ad_server.tool(get_copies)
ad_server.tool(create_copy)

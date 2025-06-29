"""Ad MCP Server using Facebook Business SDK."""

from typing import Any

from facebook_business.adobjects.ad import Ad
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
)

#  ---- constants ----
server_name = "FacebookAd"
instructions = """
This is the Ad MCP Server for managing Facebook Ads.
always use the `get_usage_on_ad` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_ad_fn.` tool to call any method on the Ad object.
"""

ad_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


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


# ---- register tools ----
ad_server.tool(run_any_ad_fn)
ad_server.tool(get_usage_on_ad)
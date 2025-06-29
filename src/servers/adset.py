"""AdSet MCP Server using Facebook Business SDK."""

from typing import Any

from facebook_business.adobjects.adset import AdSet
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
)

#  ---- constants ----
server_name = "FacebookAdSet"
instructions = """
This is the AdSet MCP Server for managing Facebook Ad Sets.
always use the `get_usage_on_adset` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_adset_fn.` tool to call any method on the AdSet object.
"""

adset_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


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


# ---- register tools ----
adset_server.tool(run_any_adset_fn)
adset_server.tool(get_usage_on_adset)
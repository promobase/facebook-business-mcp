"""Simplified Ad Account MCP Server using Facebook Business SDK."""

from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
)

#  ---- constants ----
server_name = "FacebookAdAccount"
instructions = """
This is the AdAccount MCP Server for managing Facebook Ad Accounts.
always use the `get_usage_on_ad_account` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_ad_account_fn.` tool to call any method on the AdAccount object.
"""

ad_account_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


@log_execution
@handle_facebook_errors
def get_usage_on_ad_account(
    fn: str | None = None,
) -> str:
    """ALWAYS use this tool first.
    Provides info on how to use the tools and methods available. This includes examples.
    Optionally, you can pass in a metod name and you will see the src code for usage of that method.
    """
    field_enum_info: dict = AdAccount._get_field_enum_info()
    methods = list_callable_methods(AdAccount)

    usage = f"""
    This is the AdAccount wrapper on Facebook Business Python SDK. 
    You can use the {run_any_ad_account_fn.__name__} tool to call any methods, here is the docstring for it: {run_any_ad_account_fn.__doc__}

    Available methods:
    methods: {methods}
    here are the ALL field types possible. NOTE that for each operation, you only need a subset. refer to the methods' src code for details.
    field_types: {AdAccount._field_types}
    field_enum_info: {field_enum_info}

    Examples:
    here are some code examples. The underlying is graph API. it relies on fields & params.

    account = AdAccount(..)
    account.get_campaigns(fields=[..], params=..) // get campaigns
    account.get_ads(fields=[..], params=..) // get ads
    """

    if fn:
        # append method src
        if hasattr(AdAccount, fn):
            method = getattr(AdAccount, fn)
            if callable(method):
                usage += f"\n\nHere is the source code for {fn}:\n{safe_getsource(method)}"
            else:
                usage += f"\n\n{fn} is not a callable method on AdAccount."
    return usage


@log_execution
@handle_facebook_errors
def run_any_ad_account_fn(
    account_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically calls a method on the AdAccount object.
    takes in an account_id, method name (fn), and optional args/kwargs.
    it will be called like this:
    ```account = AdAccount(account_id)
    result = getattr(account, fn)(*args, **kwargs)
    ```
    """
    account = AdAccount(account_id)
    if not hasattr(account, fn):
        return f"AdAccount does not have method '{fn}'. use the {get_usage_on_ad_account.__name__} tool to see available methods & usage."
    f = getattr(account, fn)
    if not callable(f):
        return f"{fn} is not a callable method on AdAccount."
    return str(f(*args, **kwargs))


# ---- register tools ----
ad_account_server.tool(run_any_ad_account_fn)
ad_account_server.tool(get_usage_on_ad_account)

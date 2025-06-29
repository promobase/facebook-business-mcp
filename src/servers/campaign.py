"""Campaign MCP Server using Facebook Business SDK."""

from typing import Any

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
)

#  ---- constants ----
server_name = "FacebookCampaign"
instructions = """
This is the Campaign MCP Server for managing Facebook Campaigns.
always use the `get_usage_on_campaign` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_campaign_fn.` tool to call any method on the Campaign object.
"""

campaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


@log_execution
@handle_facebook_errors
def get_usage_on_campaign(
    fn: str | None = None,
) -> str:
    """ALWAYS use this tool first.
    Provides info on how to use the tools and methods available. This includes examples.
    Optionally, you can pass in a method name and you will see the src code for usage of that method.
    """
    field_enum_info: dict = Campaign._get_field_enum_info()
    methods = list_callable_methods(Campaign)

    usage = f"""
    This is the Campaign wrapper on Facebook Business Python SDK. 
    You can use the {run_any_campaign_fn.__name__} tool to call any methods, here is the docstring for it: {run_any_campaign_fn.__doc__}

    Available methods:
    methods: {methods}
    here are the ALL field types possible. NOTE that for each operation, you only need a subset. refer to the methods' src code for details.
    field_types: {Campaign._field_types}
    field_enum_info: {field_enum_info}

    Examples:
    here are some code examples. The underlying is graph API. it relies on fields & params.

    campaign = Campaign(..)
    campaign.get_ad_sets(fields=[..], params=..) // get ad sets
    campaign.get_ads(fields=[..], params=..) // get ads
    campaign.get_insights(fields=[..], params=..) // get insights
    campaign.api_update(fields=[..], params=..) // update campaign
    """

    if fn:
        # append method src
        if hasattr(Campaign, fn):
            method = getattr(Campaign, fn)
            if callable(method):
                usage += f"\n\nHere is the source code for {fn}:\n{safe_getsource(method)}"
            else:
                usage += f"\n\n{fn} is not a callable method on Campaign."
    return usage


@log_execution
@handle_facebook_errors
def run_any_campaign_fn(
    campaign_id: str,
    fn: str,
    args: list[str] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically calls a method on the Campaign object.
    takes in a campaign_id, method name (fn), and optional args/kwargs.
    it will be called like this:
    ```campaign = Campaign(campaign_id)
    result = getattr(campaign, fn)(*args, **kwargs)
    ```
    """
    campaign = Campaign(campaign_id)
    if not hasattr(campaign, fn):
        return f"Campaign does not have method '{fn}'. use the {get_usage_on_campaign.__name__} tool to see available methods & usage."
    f = getattr(campaign, fn)
    if not callable(f):
        return f"{fn} is not a callable method on Campaign."
    return str(f(*args, **kwargs))


# ---- register tools ----
campaign_server.tool(run_any_campaign_fn)
campaign_server.tool(get_usage_on_campaign)
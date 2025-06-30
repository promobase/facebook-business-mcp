"""Campaign MCP Server using Facebook Business SDK."""

import inspect
from typing import Any

from facebook_business.adobjects.campaign import Campaign
from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
    wrapped_fn_tool,
)

#  ---- constants ----
server_name = "FacebookCampaign"
instructions = """
This is the Campaign MCP Server for managing Facebook Campaigns. You have specific methods that wrap around the Campaign object.

If the tools are not available to you, use the `get_usage_on_campaign` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_campaign_fn.` tool to call any method on the Campaign object.
"""

campaign_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


#  ---- Core API methods ----
@wrapped_fn_tool
def get_campaign(
    campaign_id: str,
    fields: list[str] = [],
) -> str:
    return Campaign(campaign_id).api_get(fields=fields)


@wrapped_fn_tool
def update_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).api_update(fields=fields, params=params)


@wrapped_fn_tool
def delete_campaign(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).api_delete(fields=fields, params=params)


#  ---- Ad Set management ----
@wrapped_fn_tool
def get_ad_sets(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).get_ad_sets(fields=fields, params=params)


#  ---- Ad management ----
@wrapped_fn_tool
def get_ads(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).get_ads(fields=fields, params=params)


#  ---- Insights ----
@wrapped_fn_tool
def get_insights(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    is_async: bool = False,
) -> str:
    return Campaign(campaign_id).get_insights(fields=fields, params=params, is_async=is_async)


@wrapped_fn_tool
def get_insights_async(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).get_insights_async(fields=fields, params=params)


#  ---- Advanced features ----
@wrapped_fn_tool
def create_ad_label(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).create_ad_label(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_studies(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).get_ad_studies(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_rules_governed(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).get_ad_rules_governed(fields=fields, params=params)


@wrapped_fn_tool
def create_budget_schedule(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).create_budget_schedule(fields=fields, params=params)


@wrapped_fn_tool
def get_copies(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).get_copies(fields=fields, params=params)


@wrapped_fn_tool
def create_copy(
    campaign_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return Campaign(campaign_id).create_copy(fields=fields, params=params)


#  ---- Dynamic tools ----
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


# ---- tool docstrings ----

fields_src = inspect.getsource(Campaign.Field)

# Core API methods
get_campaign.__doc__ = f"""Get a Campaign object by ID.
campaign_id: The ID of the Campaign
fields: {fields_src}

Source code:
{safe_getsource(Campaign.api_get)}
"""

update_campaign.__doc__ = f"""Update a Campaign object.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Update parameters

Source code:
{safe_getsource(Campaign.api_update)}
"""

delete_campaign.__doc__ = f"""Delete a Campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Deletion parameters

Source code:
{safe_getsource(Campaign.api_delete)}
"""

# Ad Set management
get_ad_sets.__doc__ = f"""Get ad sets for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Campaign.get_ad_sets)}
"""

# Ad management
get_ads.__doc__ = f"""Get ads for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Campaign.get_ads)}
"""

# Insights
get_insights.__doc__ = f"""Get insights for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Insights query parameters
is_async: Whether to run asynchronously

Source code:
{safe_getsource(Campaign.get_insights)}
"""

get_insights_async.__doc__ = f"""Get insights asynchronously for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Insights query parameters

Source code:
{safe_getsource(Campaign.get_insights_async)}
"""

# Advanced features
create_ad_label.__doc__ = f"""Create an ad label for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Label creation parameters

Source code:
{safe_getsource(Campaign.create_ad_label)}
"""

get_ad_studies.__doc__ = f"""Get ad studies for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Campaign.get_ad_studies)}
"""

get_ad_rules_governed.__doc__ = f"""Get ad rules that govern this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Campaign.get_ad_rules_governed)}
"""

create_budget_schedule.__doc__ = f"""Create budget schedule for this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Budget schedule parameters

Source code:
{safe_getsource(Campaign.create_budget_schedule)}
"""

get_copies.__doc__ = f"""Get copies of this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(Campaign.get_copies)}
"""

create_copy.__doc__ = f"""Create a copy of this campaign.
campaign_id: The ID of the Campaign
fields: Fields to retrieve
params: Copy parameters

Source code:
{safe_getsource(Campaign.create_copy)}
"""

# ---- register tools ----
# Core tools
campaign_server.tool(get_usage_on_campaign)
campaign_server.tool(run_any_campaign_fn)

# Core API methods
campaign_server.tool(get_campaign)
campaign_server.tool(update_campaign)
campaign_server.tool(delete_campaign)

# Ad Set management
campaign_server.tool(get_ad_sets)

# Ad management
campaign_server.tool(get_ads)

# Insights
campaign_server.tool(get_insights)
campaign_server.tool(get_insights_async)

# Advanced features
campaign_server.tool(create_ad_label)
campaign_server.tool(get_ad_studies)
campaign_server.tool(get_ad_rules_governed)
campaign_server.tool(create_budget_schedule)
campaign_server.tool(get_copies)
campaign_server.tool(create_copy)

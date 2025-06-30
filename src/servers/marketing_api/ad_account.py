"""Simplified Ad Account MCP Server using Facebook Business SDK."""

import inspect
from typing import Any

from facebook_business.adobjects.adaccount import AdAccount
from fastmcp import FastMCP

from src.utils import (
    list_callable_methods,
    safe_getsource,
    wrapped_fn_tool,
)

#  ---- constants ----
server_name = "FacebookAdAccount"
instructions = """
This is the AdAccount MCP Server for managing Facebook Ad Accounts. You have the specific methods that wraps around the AdAccount object.

If the tools are not available to you, use the `get_usage_on_ad_account` tool first to understand how to use the methods and fields available.
Then, you can use the `run_any_ad_account_fn.` tool to call any method on the AdAccount object.
"""

ad_account_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


#  ---- Core API methods ----
@wrapped_fn_tool
def get_ad_account(
    ad_account_id: str,
    fields: list[str] = [],
) -> str:
    account = AdAccount(ad_account_id)
    return account.api_get(fields=fields)


@wrapped_fn_tool
def update_ad_account(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).api_update(fields=fields, params=params)


#  ---- Campaign management ----
@wrapped_fn_tool
def get_campaigns(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def create_campaign(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_campaign(fields=fields, params=params)


@wrapped_fn_tool
def delete_campaigns(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_campaigns(fields=fields, params=params)


@wrapped_fn_tool
def get_campaigns_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_campaigns_by_labels(fields=fields, params=params)


#  ---- Ad Set management ----
@wrapped_fn_tool
def get_ad_sets(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_sets(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_set(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_set(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_sets_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_sets_by_labels(fields=fields, params=params)


#  ---- Ad management ----
@wrapped_fn_tool
def get_ads(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ads(fields=fields, params=params)


@wrapped_fn_tool
def create_ad(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad(fields=fields, params=params)


@wrapped_fn_tool
def get_ads_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ads_by_labels(fields=fields, params=params)


#  ---- Creative management ----
@wrapped_fn_tool
def get_ad_creatives(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_creatives(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_creative(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_creative(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_creatives_by_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_creatives_by_labels(fields=fields, params=params)


#  ---- Image management ----
@wrapped_fn_tool
def get_ad_images(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_images(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_image(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_image(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad_images(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_ad_images(fields=fields, params=params)


#  ---- Video management ----
@wrapped_fn_tool
def get_ad_videos(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_videos(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_video(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_video(fields=fields, params=params)


@wrapped_fn_tool
def delete_ad_videos(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_ad_videos(fields=fields, params=params)


#  ---- Custom Audience management ----
@wrapped_fn_tool
def get_custom_audiences(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_custom_audiences(fields=fields, params=params)


@wrapped_fn_tool
def create_custom_audience(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_custom_audience(fields=fields, params=params)


#  ---- Insights and reporting ----
@wrapped_fn_tool
def get_insights(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
    is_async: bool = False,
) -> str:
    return AdAccount(ad_account_id).get_insights(fields=fields, params=params, is_async=is_async)


@wrapped_fn_tool
def get_insights_async(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_insights_async(fields=fields, params=params)


#  ---- Targeting tools ----
@wrapped_fn_tool
def get_targeting_browse(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_targeting_browse(fields=fields, params=params)


@wrapped_fn_tool
def get_targeting_search(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_targeting_search(fields=fields, params=params)


@wrapped_fn_tool
def get_targeting_suggestions(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_targeting_suggestions(fields=fields, params=params)


@wrapped_fn_tool
def get_reach_estimate(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_reach_estimate(fields=fields, params=params)


@wrapped_fn_tool
def get_delivery_estimate(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_delivery_estimate(fields=fields, params=params)


#  ---- Pixel management ----
@wrapped_fn_tool
def get_ads_pixels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ads_pixels(fields=fields, params=params)


@wrapped_fn_tool
def create_ads_pixel(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ads_pixel(fields=fields, params=params)


#  ---- User management ----
@wrapped_fn_tool
def get_users(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_users(fields=fields, params=params)


@wrapped_fn_tool
def get_assigned_users(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_assigned_users(fields=fields, params=params)


@wrapped_fn_tool
def create_assigned_user(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_assigned_user(fields=fields, params=params)


@wrapped_fn_tool
def delete_assigned_users(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).delete_assigned_users(fields=fields, params=params)


# ---- dynamic tools ----
@wrapped_fn_tool
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


@wrapped_fn_tool
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


#  ---- Labels and Rules ----
@wrapped_fn_tool
def get_ad_labels(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_labels(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_label(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_label(fields=fields, params=params)


@wrapped_fn_tool
def get_ad_rules_library(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_ad_rules_library(fields=fields, params=params)


@wrapped_fn_tool
def create_ad_rules_library(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_ad_rules_library(fields=fields, params=params)


#  ---- Instagram and Pages ----
@wrapped_fn_tool
def get_instagram_accounts(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_instagram_accounts(fields=fields, params=params)


@wrapped_fn_tool
def get_connected_instagram_accounts(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_connected_instagram_accounts(fields=fields, params=params)


@wrapped_fn_tool
def get_promote_pages(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_promote_pages(fields=fields, params=params)


#  ---- Applications ----
@wrapped_fn_tool
def get_applications(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_applications(fields=fields, params=params)


@wrapped_fn_tool
def get_advertisable_applications(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_advertisable_applications(fields=fields, params=params)


#  ---- Advanced features ----
@wrapped_fn_tool
def get_saved_audiences(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_saved_audiences(fields=fields, params=params)


@wrapped_fn_tool
def get_custom_conversions(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_custom_conversions(fields=fields, params=params)


@wrapped_fn_tool
def create_custom_conversion(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).create_custom_conversion(fields=fields, params=params)


@wrapped_fn_tool
def get_activities(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_activities(fields=fields, params=params)


@wrapped_fn_tool
def get_minimum_budgets(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_minimum_budgets(fields=fields, params=params)


@wrapped_fn_tool
def get_broad_targeting_categories(
    ad_account_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> str:
    return AdAccount(ad_account_id).get_broad_targeting_categories(fields=fields, params=params)


# ---- tool docstrings ----

fields_src = inspect.getsource(AdAccount.Field)

# Core API methods
get_ad_account.__doc__ = f"""Gets an AdAccount object by ID.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: {fields_src}

Source code:
{safe_getsource(AdAccount.api_get)}
"""

update_ad_account.__doc__ = f"""Updates an AdAccount object.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: {fields_src}

Source code:
{safe_getsource(AdAccount.api_update)}
"""

# Campaign management
get_campaigns.__doc__ = f"""Get campaigns for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_campaigns)}
"""

create_campaign.__doc__ = f"""Create a new campaign in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Campaign creation parameters

Source code:
{safe_getsource(AdAccount.create_campaign)}
"""

delete_campaigns.__doc__ = f"""Delete campaigns from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Deletion parameters

Source code:
{safe_getsource(AdAccount.delete_campaigns)}
"""

get_campaigns_by_labels.__doc__ = f"""Get campaigns filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_campaigns_by_labels)}
"""

# Ad Set management
get_ad_sets.__doc__ = f"""Get ad sets for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_sets)}
"""

create_ad_set.__doc__ = f"""Create a new ad set in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Ad set creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_set)}
"""

get_ad_sets_by_labels.__doc__ = f"""Get ad sets filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_ad_sets_by_labels)}
"""

# Ad management
get_ads.__doc__ = f"""Get ads for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ads)}
"""

create_ad.__doc__ = f"""Create a new ad in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Ad creation parameters

Source code:
{safe_getsource(AdAccount.create_ad)}
"""

get_ads_by_labels.__doc__ = f"""Get ads filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_ads_by_labels)}
"""

# Creative management
get_ad_creatives.__doc__ = f"""Get ad creatives for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_creatives)}
"""

create_ad_creative.__doc__ = f"""Create a new ad creative in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Creative creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_creative)}
"""

get_ad_creatives_by_labels.__doc__ = f"""Get ad creatives filtered by labels.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters including label filters

Source code:
{safe_getsource(AdAccount.get_ad_creatives_by_labels)}
"""

# Image management
get_ad_images.__doc__ = f"""Get ad images for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_images)}
"""

create_ad_image.__doc__ = f"""Upload a new ad image to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Image upload parameters

Source code:
{safe_getsource(AdAccount.create_ad_image)}
"""

delete_ad_images.__doc__ = f"""Delete ad images from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Image deletion parameters

Source code:
{safe_getsource(AdAccount.delete_ad_images)}
"""

# Video management
get_ad_videos.__doc__ = f"""Get ad videos for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_videos)}
"""

create_ad_video.__doc__ = f"""Upload a new ad video to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Video upload parameters

Source code:
{safe_getsource(AdAccount.create_ad_video)}
"""

delete_ad_videos.__doc__ = f"""Delete ad videos from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Video deletion parameters

Source code:
{safe_getsource(AdAccount.delete_ad_videos)}
"""

# Custom Audience management
get_custom_audiences.__doc__ = f"""Get custom audiences for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_custom_audiences)}
"""

create_custom_audience.__doc__ = f"""Create a new custom audience in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Custom audience creation parameters

Source code:
{safe_getsource(AdAccount.create_custom_audience)}
"""

# Insights and reporting
get_insights.__doc__ = f"""Get insights for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Insights query parameters
is_async: Whether to run asynchronously

Source code:
{safe_getsource(AdAccount.get_insights)}
"""

get_insights_async.__doc__ = f"""Get insights asynchronously for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Insights query parameters

Source code:
{safe_getsource(AdAccount.get_insights_async)}
"""

# Targeting tools
get_targeting_browse.__doc__ = f"""Browse targeting options for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Browse parameters

Source code:
{safe_getsource(AdAccount.get_targeting_browse)}
"""

get_targeting_search.__doc__ = f"""Search targeting options for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Search parameters

Source code:
{safe_getsource(AdAccount.get_targeting_search)}
"""

get_targeting_suggestions.__doc__ = f"""Get targeting suggestions for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Suggestion parameters

Source code:
{safe_getsource(AdAccount.get_targeting_suggestions)}
"""

get_reach_estimate.__doc__ = f"""Get reach estimate for targeting.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Targeting parameters

Source code:
{safe_getsource(AdAccount.get_reach_estimate)}
"""

get_delivery_estimate.__doc__ = f"""Get delivery estimate for ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Estimation parameters

Source code:
{safe_getsource(AdAccount.get_delivery_estimate)}
"""

# Pixel management
get_ads_pixels.__doc__ = f"""Get Facebook pixels for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ads_pixels)}
"""

create_ads_pixel.__doc__ = f"""Create a new Facebook pixel for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Pixel creation parameters

Source code:
{safe_getsource(AdAccount.create_ads_pixel)}
"""

# User management
get_users.__doc__ = f"""Get users with access to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_users)}
"""

get_assigned_users.__doc__ = f"""Get assigned users for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_assigned_users)}
"""

create_assigned_user.__doc__ = f"""Assign a user to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: User assignment parameters

Source code:
{safe_getsource(AdAccount.create_assigned_user)}
"""

delete_assigned_users.__doc__ = f"""Remove assigned users from this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: User removal parameters

Source code:
{safe_getsource(AdAccount.delete_assigned_users)}
"""

# Labels and Rules
get_ad_labels.__doc__ = f"""Get ad labels for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_labels)}
"""

create_ad_label.__doc__ = f"""Create a new ad label in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Label creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_label)}
"""

get_ad_rules_library.__doc__ = f"""Get ad rules library for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_ad_rules_library)}
"""

create_ad_rules_library.__doc__ = f"""Create new ad rules in this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Rule creation parameters

Source code:
{safe_getsource(AdAccount.create_ad_rules_library)}
"""

# Instagram and Pages
get_instagram_accounts.__doc__ = f"""Get Instagram accounts connected to this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_instagram_accounts)}
"""

get_connected_instagram_accounts.__doc__ = f"""Get connected Instagram accounts for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_connected_instagram_accounts)}
"""

get_promote_pages.__doc__ = f"""Get pages that can be promoted by this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_promote_pages)}
"""

# Applications
get_applications.__doc__ = f"""Get applications associated with this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_applications)}
"""

get_advertisable_applications.__doc__ = f"""Get advertisable applications for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_advertisable_applications)}
"""

# Advanced features
get_saved_audiences.__doc__ = f"""Get saved audiences for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_saved_audiences)}
"""

get_custom_conversions.__doc__ = f"""Get custom conversions for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_custom_conversions)}
"""

create_custom_conversion.__doc__ = f"""Create a new custom conversion for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Custom conversion creation parameters

Source code:
{safe_getsource(AdAccount.create_custom_conversion)}
"""

get_activities.__doc__ = f"""Get activities for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_activities)}
"""

get_minimum_budgets.__doc__ = f"""Get minimum budget requirements for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_minimum_budgets)}
"""

get_broad_targeting_categories.__doc__ = f"""Get broad targeting categories for this ad account.
ad_account_id: The ID of the Ad Account. ALWAYS start with 'act_' prefix.
fields: Fields to retrieve
params: Query parameters

Source code:
{safe_getsource(AdAccount.get_broad_targeting_categories)}
"""

# ---- register tools ----
# Core tools
ad_account_server.tool(get_usage_on_ad_account)
ad_account_server.tool(run_any_ad_account_fn)

# Core API methods
ad_account_server.tool(get_ad_account)
ad_account_server.tool(update_ad_account)

# Campaign management
ad_account_server.tool(get_campaigns)
ad_account_server.tool(create_campaign)
ad_account_server.tool(delete_campaigns)
ad_account_server.tool(get_campaigns_by_labels)

# Ad Set management
ad_account_server.tool(get_ad_sets)
ad_account_server.tool(create_ad_set)
ad_account_server.tool(get_ad_sets_by_labels)

# Ad management
ad_account_server.tool(get_ads)
ad_account_server.tool(create_ad)
ad_account_server.tool(get_ads_by_labels)

# Creative management
ad_account_server.tool(get_ad_creatives)
ad_account_server.tool(create_ad_creative)
ad_account_server.tool(get_ad_creatives_by_labels)

# Image management
ad_account_server.tool(get_ad_images)
ad_account_server.tool(create_ad_image)
ad_account_server.tool(delete_ad_images)

# Video management
ad_account_server.tool(get_ad_videos)
ad_account_server.tool(create_ad_video)
ad_account_server.tool(delete_ad_videos)

# Custom Audience management
ad_account_server.tool(get_custom_audiences)
ad_account_server.tool(create_custom_audience)

# Insights and reporting
ad_account_server.tool(get_insights)
ad_account_server.tool(get_insights_async)

# Targeting tools
ad_account_server.tool(get_targeting_browse)
ad_account_server.tool(get_targeting_search)
ad_account_server.tool(get_targeting_suggestions)
ad_account_server.tool(get_reach_estimate)
ad_account_server.tool(get_delivery_estimate)

# Pixel management
ad_account_server.tool(get_ads_pixels)
ad_account_server.tool(create_ads_pixel)

# User management
ad_account_server.tool(get_users)
ad_account_server.tool(get_assigned_users)
ad_account_server.tool(create_assigned_user)
ad_account_server.tool(delete_assigned_users)

# Labels and Rules
ad_account_server.tool(get_ad_labels)
ad_account_server.tool(create_ad_label)
ad_account_server.tool(get_ad_rules_library)
ad_account_server.tool(create_ad_rules_library)

# Instagram and Pages
ad_account_server.tool(get_instagram_accounts)
ad_account_server.tool(get_connected_instagram_accounts)
ad_account_server.tool(get_promote_pages)

# Applications
ad_account_server.tool(get_applications)
ad_account_server.tool(get_advertisable_applications)

# Advanced features
ad_account_server.tool(get_saved_audiences)
ad_account_server.tool(get_custom_conversions)
ad_account_server.tool(create_custom_conversion)
ad_account_server.tool(get_activities)
ad_account_server.tool(get_minimum_budgets)
ad_account_server.tool(get_broad_targeting_categories)

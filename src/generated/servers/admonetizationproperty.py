"""AdMonetizationProperty MCP Server with typed wrappers."""

from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
from fastmcp import FastMCP

from src.generated.models.admonetizationproperty import (
    AdMonetizationPropertyCreateAdNetworkAnalyticParams,
    AdMonetizationPropertyField,
    AdMonetizationPropertyGetAdNetworkAnalyticsParams,
    AdMonetizationPropertyGetAdNetworkAnalyticsResultsParams,
)
from src.generated.models.adnetworkanalyticsasyncqueryresult import (
    AdNetworkAnalyticsAsyncQueryResultField,
)
from src.generated.models.adnetworkanalyticssyncqueryresult import (
    AdNetworkAnalyticsSyncQueryResultField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdMonetizationProperty"
instructions = """
AdMonetizationProperty MCP Server for Facebook Business API.

Provides typed access to all AdMonetizationProperty operations.
"""

admonetizationproperty_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@admonetizationproperty_server.tool
@wrapped_fn_tool
def get_admonetizationproperty(
    admonetizationproperty_id: str,
    fields: list[AdMonetizationPropertyField] = [],
) -> str:
    """Get a AdMonetizationProperty object by ID.

    Args:
        admonetizationproperty_id: The ID of the AdMonetizationProperty.
        fields: Fields to retrieve. Available fields: See AdMonetizationPropertyField type.
    """
    obj = AdMonetizationProperty(admonetizationproperty_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (3) ----
@admonetizationproperty_server.tool
@wrapped_fn_tool
def get_ad_network_analytics(
    admonetizationproperty_id: str,
    fields: list[AdNetworkAnalyticsSyncQueryResultField] = [],
    params: AdMonetizationPropertyGetAdNetworkAnalyticsParams | dict = {},
):
    """Get Ad Network Analytics for this AdMonetizationProperty.

    Args:
        admonetizationproperty_id: The ID of the AdMonetizationProperty.
        fields: Fields to retrieve. Available fields: See AdNetworkAnalyticsSyncQueryResultField type.
        params: Query parameters. Available params: See AdMonetizationPropertyGetAdNetworkAnalyticsParams type.
    """
    return AdMonetizationProperty(admonetizationproperty_id).get_ad_network_analytics(
        fields=fields, params=params
    )


@admonetizationproperty_server.tool
@wrapped_fn_tool
def create_ad_network_analytic(
    admonetizationproperty_id: str,
    fields: list[str] = [],
    params: AdMonetizationPropertyCreateAdNetworkAnalyticParams | dict = {},
):
    """Create Ad Network Analytic for this AdMonetizationProperty.

    Args:
        admonetizationproperty_id: The ID of the AdMonetizationProperty.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdMonetizationPropertyCreateAdNetworkAnalyticParams type.
    """
    return AdMonetizationProperty(admonetizationproperty_id).create_ad_network_analytic(
        fields=fields, params=params
    )


@admonetizationproperty_server.tool
@wrapped_fn_tool
def get_ad_network_analytics_results(
    admonetizationproperty_id: str,
    fields: list[AdNetworkAnalyticsAsyncQueryResultField] = [],
    params: AdMonetizationPropertyGetAdNetworkAnalyticsResultsParams | dict = {},
):
    """Get Ad Network Analytics Results for this AdMonetizationProperty.

    Args:
        admonetizationproperty_id: The ID of the AdMonetizationProperty.
        fields: Fields to retrieve. Available fields: See AdNetworkAnalyticsAsyncQueryResultField type.
        params: Query parameters. Available params: See AdMonetizationPropertyGetAdNetworkAnalyticsResultsParams type.
    """
    return AdMonetizationProperty(admonetizationproperty_id).get_ad_network_analytics_results(
        fields=fields, params=params
    )

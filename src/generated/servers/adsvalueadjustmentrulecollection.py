"""AdsValueAdjustmentRuleCollection MCP Server with typed wrappers."""

from facebook_business.adobjects.adsvalueadjustmentrulecollection import (
    AdsValueAdjustmentRuleCollection,
)
from fastmcp import FastMCP

from src.generated.models.adsvalueadjustmentrulecollection import (
    AdsValueAdjustmentRuleCollectionField,
    AdsValueAdjustmentRuleCollectionUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdsValueAdjustmentRuleCollection"
instructions = """
AdsValueAdjustmentRuleCollection MCP Server for Facebook Business API.

Provides typed access to all AdsValueAdjustmentRuleCollection operations.
"""

adsvalueadjustmentrulecollection_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@adsvalueadjustmentrulecollection_server.tool
@wrapped_fn_tool
def get_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[AdsValueAdjustmentRuleCollectionField] = [],
) -> str:
    """Get a AdsValueAdjustmentRuleCollection object by ID.

    Args:
        adsvalueadjustmentrulecollection_id: The ID of the AdsValueAdjustmentRuleCollection.
        fields: Fields to retrieve. Available fields: See AdsValueAdjustmentRuleCollectionField type.
    """
    obj = AdsValueAdjustmentRuleCollection(adsvalueadjustmentrulecollection_id)
    return obj.api_get(fields=fields)


@adsvalueadjustmentrulecollection_server.tool
@wrapped_fn_tool
def update_adsvalueadjustmentrulecollection(
    adsvalueadjustmentrulecollection_id: str,
    fields: list[AdsValueAdjustmentRuleCollectionField] = [],
    params: AdsValueAdjustmentRuleCollectionUpdateParams | dict = {},
) -> str:
    """Update a AdsValueAdjustmentRuleCollection object.

    Args:
        adsvalueadjustmentrulecollection_id: The ID of the AdsValueAdjustmentRuleCollection.
        fields: Fields to return after update. Available fields: See AdsValueAdjustmentRuleCollectionField type.
        params: Parameters to update. Available params: See AdsValueAdjustmentRuleCollectionUpdateParams type.
    """
    return AdsValueAdjustmentRuleCollection(adsvalueadjustmentrulecollection_id).api_update(
        fields=fields, params=params
    )

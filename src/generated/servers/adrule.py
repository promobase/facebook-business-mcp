"""AdRule MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adrule import AdRule
from fastmcp import FastMCP

from src.generated.models.adrule import AdRuleField, AdRuleGetHistoryParams, AdRuleUpdateParams
from src.generated.models.adrulehistory import AdRuleHistoryField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdRule"
instructions = """
AdRule MCP Server for Facebook Business API.

Provides typed access to all AdRule operations.
"""

adrule_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adrule_server.tool
@wrapped_fn_tool
def get_adrule(
    adrule_id: str,
    fields: list[AdRuleField] = [],
) -> str:
    """Get a AdRule object by ID.

    Args:
        adrule_id: The ID of the AdRule.
        fields: Fields to retrieve. Available fields: See AdRuleField type.
    """
    obj = AdRule(adrule_id)
    return obj.api_get(fields=fields)


@adrule_server.tool
@wrapped_fn_tool
def update_adrule(
    adrule_id: str,
    fields: list[AdRuleField] = [],
    params: AdRuleUpdateParams | dict = {},
) -> str:
    """Update a AdRule object.

    Args:
        adrule_id: The ID of the AdRule.
        fields: Fields to return after update. Available fields: See AdRuleField type.
        params: Parameters to update. Available params: See AdRuleUpdateParams type.
    """
    return AdRule(adrule_id).api_update(fields=fields, params=params)


@adrule_server.tool
@wrapped_fn_tool
def delete_adrule(
    adrule_id: str,
) -> str:
    """Delete a AdRule object.

    Args:
        adrule_id: The ID of the AdRule.
    """
    return AdRule(adrule_id).api_delete()


# ---- Edge Methods (1) ----
@adrule_server.tool
@wrapped_fn_tool
def get_history(
    adrule_id: str,
    fields: list[AdRuleHistoryField] = [],
    params: AdRuleGetHistoryParams | dict = {},
):
    """Get History for this AdRule.

    Args:
        adrule_id: The ID of the AdRule.
        fields: Fields to retrieve. Available fields: See AdRuleHistoryField type.
        params: Query parameters. Available params: See AdRuleGetHistoryParams type.
    """
    return AdRule(adrule_id).get_history(fields=fields, params=params)

"""ExtendedCreditAllocationConfig MCP Server with typed wrappers."""

from facebook_business.adobjects.extendedcreditallocationconfig import (
    ExtendedCreditAllocationConfig,
)
from fastmcp import FastMCP

from src.generated.models.extendedcreditallocationconfig import (
    ExtendedCreditAllocationConfigField,
    ExtendedCreditAllocationConfigUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookExtendedCreditAllocationConfig"
instructions = """
ExtendedCreditAllocationConfig MCP Server for Facebook Business API.

Provides typed access to all ExtendedCreditAllocationConfig operations.
"""

extendedcreditallocationconfig_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@extendedcreditallocationconfig_server.tool
@wrapped_fn_tool
def get_extendedcreditallocationconfig(
    extendedcreditallocationconfig_id: str,
    fields: list[ExtendedCreditAllocationConfigField] = [],
) -> str:
    """Get a ExtendedCreditAllocationConfig object by ID.

    Args:
        extendedcreditallocationconfig_id: The ID of the ExtendedCreditAllocationConfig.
        fields: Fields to retrieve. Available fields: See ExtendedCreditAllocationConfigField type.
    """
    obj = ExtendedCreditAllocationConfig(extendedcreditallocationconfig_id)
    return obj.api_get(fields=fields)


@extendedcreditallocationconfig_server.tool
@wrapped_fn_tool
def update_extendedcreditallocationconfig(
    extendedcreditallocationconfig_id: str,
    fields: list[ExtendedCreditAllocationConfigField] = [],
    params: ExtendedCreditAllocationConfigUpdateParams | dict = {},
) -> str:
    """Update a ExtendedCreditAllocationConfig object.

    Args:
        extendedcreditallocationconfig_id: The ID of the ExtendedCreditAllocationConfig.
        fields: Fields to return after update. Available fields: See ExtendedCreditAllocationConfigField type.
        params: Parameters to update. Available params: See ExtendedCreditAllocationConfigUpdateParams type.
    """
    return ExtendedCreditAllocationConfig(extendedcreditallocationconfig_id).api_update(
        fields=fields, params=params
    )


@extendedcreditallocationconfig_server.tool
@wrapped_fn_tool
def delete_extendedcreditallocationconfig(
    extendedcreditallocationconfig_id: str,
) -> str:
    """Delete a ExtendedCreditAllocationConfig object.

    Args:
        extendedcreditallocationconfig_id: The ID of the ExtendedCreditAllocationConfig.
    """
    return ExtendedCreditAllocationConfig(extendedcreditallocationconfig_id).api_delete()

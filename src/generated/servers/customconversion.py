"""CustomConversion MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.customconversion import CustomConversion
from fastmcp import FastMCP

from src.generated.models.customconversion import (
    CustomConversionField,
    CustomConversionGetStatsParams,
    CustomConversionUpdateParams,
)
from src.generated.models.customconversionstatsresult import CustomConversionStatsResultField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookCustomConversion"
instructions = """
CustomConversion MCP Server for Facebook Business API.

Provides typed access to all CustomConversion operations.
"""

customconversion_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@customconversion_server.tool
@wrapped_fn_tool
def get_customconversion(
    customconversion_id: str,
    fields: list[CustomConversionField] = [],
) -> str:
    """Get a CustomConversion object by ID.

    Args:
        customconversion_id: The ID of the CustomConversion.
        fields: Fields to retrieve. Available fields: See CustomConversionField type.
    """
    obj = CustomConversion(customconversion_id)
    return obj.api_get(fields=fields)


@customconversion_server.tool
@wrapped_fn_tool
def update_customconversion(
    customconversion_id: str,
    fields: list[CustomConversionField] = [],
    params: CustomConversionUpdateParams | dict = {},
) -> str:
    """Update a CustomConversion object.

    Args:
        customconversion_id: The ID of the CustomConversion.
        fields: Fields to return after update. Available fields: See CustomConversionField type.
        params: Parameters to update. Available params: See CustomConversionUpdateParams type.
    """
    return CustomConversion(customconversion_id).api_update(fields=fields, params=params)


@customconversion_server.tool
@wrapped_fn_tool
def delete_customconversion(
    customconversion_id: str,
) -> str:
    """Delete a CustomConversion object.

    Args:
        customconversion_id: The ID of the CustomConversion.
    """
    return CustomConversion(customconversion_id).api_delete()


# ---- Edge Methods (1) ----
@customconversion_server.tool
@wrapped_fn_tool
def get_stats(
    customconversion_id: str,
    fields: list[CustomConversionStatsResultField] = [],
    params: CustomConversionGetStatsParams | dict = {},
):
    """Get Stats for this CustomConversion.

    Args:
        customconversion_id: The ID of the CustomConversion.
        fields: Fields to retrieve. Available fields: See CustomConversionStatsResultField type.
        params: Query parameters. Available params: See CustomConversionGetStatsParams type.
    """
    return CustomConversion(customconversion_id).get_stats(fields=fields, params=params)

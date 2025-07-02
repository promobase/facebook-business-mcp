"""AdStudy MCP Server with typed wrappers."""

from facebook_business.adobjects.adstudy import AdStudy
from fastmcp import FastMCP

from src.generated.models.adstudy import (
    AdStudyCreateCheckPointParams,
    AdStudyCreateInstanceParams,
    AdStudyField,
    AdStudyUpdateParams,
)
from src.generated.models.privateliftstudyinstance import PrivateLiftStudyInstanceField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdStudy"
instructions = """
AdStudy MCP Server for Facebook Business API.

Provides typed access to all AdStudy operations.
"""

adstudy_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adstudy_server.tool
@wrapped_fn_tool
def get_adstudy(
    adstudy_id: str,
    fields: list[AdStudyField] = [],
) -> str:
    """Get a AdStudy object by ID.

    Args:
        adstudy_id: The ID of the AdStudy.
        fields: Fields to retrieve. Available fields: See AdStudyField type.
    """
    obj = AdStudy(adstudy_id)
    return obj.api_get(fields=fields)


@adstudy_server.tool
@wrapped_fn_tool
def update_adstudy(
    adstudy_id: str,
    fields: list[AdStudyField] = [],
    params: AdStudyUpdateParams | dict = {},
) -> str:
    """Update a AdStudy object.

    Args:
        adstudy_id: The ID of the AdStudy.
        fields: Fields to return after update. Available fields: See AdStudyField type.
        params: Parameters to update. Available params: See AdStudyUpdateParams type.
    """
    return AdStudy(adstudy_id).api_update(fields=fields, params=params)


@adstudy_server.tool
@wrapped_fn_tool
def delete_adstudy(
    adstudy_id: str,
) -> str:
    """Delete a AdStudy object.

    Args:
        adstudy_id: The ID of the AdStudy.
    """
    return AdStudy(adstudy_id).api_delete()


# ---- Edge Methods (2) ----
@adstudy_server.tool
@wrapped_fn_tool
def create_check_point(
    adstudy_id: str,
    fields: list[str] = [],
    params: AdStudyCreateCheckPointParams | dict = {},
):
    """Create Check Point for this AdStudy.

    Args:
        adstudy_id: The ID of the AdStudy.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdStudyCreateCheckPointParams type.
    """
    return AdStudy(adstudy_id).create_check_point(fields=fields, params=params)


@adstudy_server.tool
@wrapped_fn_tool
def create_instance(
    adstudy_id: str,
    fields: list[str] = [],
    params: AdStudyCreateInstanceParams | dict = {},
):
    """Create Instance for this AdStudy.

    Args:
        adstudy_id: The ID of the AdStudy.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See AdStudyCreateInstanceParams type.
    """
    return AdStudy(adstudy_id).create_instance(fields=fields, params=params)

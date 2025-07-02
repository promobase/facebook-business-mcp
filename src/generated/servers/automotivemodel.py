"""AutomotiveModel MCP Server with typed wrappers."""

from facebook_business.adobjects.automotivemodel import AutomotiveModel
from fastmcp import FastMCP

from src.generated.models.automotivemodel import (
    AutomotiveModelField,
    AutomotiveModelGetOverrideDetailsParams,
)
from src.generated.models.overridedetails import OverrideDetailsField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAutomotiveModel"
instructions = """
AutomotiveModel MCP Server for Facebook Business API.

Provides typed access to all AutomotiveModel operations.
"""

automotivemodel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@automotivemodel_server.tool
@wrapped_fn_tool
def get_automotivemodel(
    automotivemodel_id: str,
    fields: list[AutomotiveModelField] = [],
) -> str:
    """Get a AutomotiveModel object by ID.

    Args:
        automotivemodel_id: The ID of the AutomotiveModel.
        fields: Fields to retrieve. Available fields: See AutomotiveModelField type.
    """
    obj = AutomotiveModel(automotivemodel_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@automotivemodel_server.tool
@wrapped_fn_tool
def get_override_details(
    automotivemodel_id: str,
    fields: list[OverrideDetailsField] = [],
    params: AutomotiveModelGetOverrideDetailsParams | dict = {},
):
    """Get Override Details for this AutomotiveModel.

    Args:
        automotivemodel_id: The ID of the AutomotiveModel.
        fields: Fields to retrieve. Available fields: See OverrideDetailsField type.
        params: Query parameters. Available params: See AutomotiveModelGetOverrideDetailsParams type.
    """
    return AutomotiveModel(automotivemodel_id).get_override_details(fields=fields, params=params)

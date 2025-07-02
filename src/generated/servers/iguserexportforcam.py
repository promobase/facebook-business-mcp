"""IGUserExportForCAM MCP Server with typed wrappers."""

from facebook_business.adobjects.iguserexportforcam import IGUserExportForCAM
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.iguserexportforcam import (
    IGUserExportForCAMField,
    IGUserExportForCAMGetInsightsParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGUserExportForCAM"
instructions = """
IGUserExportForCAM MCP Server for Facebook Business API.

Provides typed access to all IGUserExportForCAM operations.
"""

iguserexportforcam_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@iguserexportforcam_server.tool
@wrapped_fn_tool
def get_iguserexportforcam(
    iguserexportforcam_id: str,
    fields: list[IGUserExportForCAMField] = [],
) -> str:
    """Get a IGUserExportForCAM object by ID.

    Args:
        iguserexportforcam_id: The ID of the IGUserExportForCAM.
        fields: Fields to retrieve. Available fields: See IGUserExportForCAMField type.
    """
    obj = IGUserExportForCAM(iguserexportforcam_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@iguserexportforcam_server.tool
@wrapped_fn_tool
def get_insights(
    iguserexportforcam_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: IGUserExportForCAMGetInsightsParams | dict = {},
):
    """Get Insights for this IGUserExportForCAM.

    Args:
        iguserexportforcam_id: The ID of the IGUserExportForCAM.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See IGUserExportForCAMGetInsightsParams type.
    """
    return IGUserExportForCAM(iguserexportforcam_id).get_insights(fields=fields, params=params)

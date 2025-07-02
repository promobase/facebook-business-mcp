"""OffsiteSignalContainerBusinessObject MCP Server with typed wrappers."""

from facebook_business.adobjects.offsitesignalcontainerbusinessobject import (
    OffsiteSignalContainerBusinessObject,
)
from fastmcp import FastMCP

from src.generated.models.offsitesignalcontainerbusinessobject import (
    OffsiteSignalContainerBusinessObjectField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookOffsiteSignalContainerBusinessObject"
instructions = """
OffsiteSignalContainerBusinessObject MCP Server for Facebook Business API.

Provides typed access to all OffsiteSignalContainerBusinessObject operations.
"""

offsitesignalcontainerbusinessobject_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@offsitesignalcontainerbusinessobject_server.tool
@wrapped_fn_tool
def get_offsitesignalcontainerbusinessobject(
    offsitesignalcontainerbusinessobject_id: str,
    fields: list[OffsiteSignalContainerBusinessObjectField] = [],
) -> str:
    """Get a OffsiteSignalContainerBusinessObject object by ID.

    Args:
        offsitesignalcontainerbusinessobject_id: The ID of the OffsiteSignalContainerBusinessObject.
        fields: Fields to retrieve. Available fields: See OffsiteSignalContainerBusinessObjectField type.
    """
    obj = OffsiteSignalContainerBusinessObject(offsitesignalcontainerbusinessobject_id)
    return obj.api_get(fields=fields)

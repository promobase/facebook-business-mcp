"""AdAsyncRequestSet MCP Server with typed wrappers."""

from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
from fastmcp import FastMCP

from src.generated.models.adasyncrequest import AdAsyncRequestField
from src.generated.models.adasyncrequestset import (
    AdAsyncRequestSetField,
    AdAsyncRequestSetGetRequestsParams,
    AdAsyncRequestSetUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdAsyncRequestSet"
instructions = """
AdAsyncRequestSet MCP Server for Facebook Business API.

Provides typed access to all AdAsyncRequestSet operations.
"""

adasyncrequestset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (3) ----
@adasyncrequestset_server.tool
@wrapped_fn_tool
def get_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[AdAsyncRequestSetField] = [],
) -> str:
    """Get a AdAsyncRequestSet object by ID.

    Args:
        adasyncrequestset_id: The ID of the AdAsyncRequestSet.
        fields: Fields to retrieve. Available fields: See AdAsyncRequestSetField type.
    """
    obj = AdAsyncRequestSet(adasyncrequestset_id)
    return obj.api_get(fields=fields)


@adasyncrequestset_server.tool
@wrapped_fn_tool
def update_adasyncrequestset(
    adasyncrequestset_id: str,
    fields: list[AdAsyncRequestSetField] = [],
    params: AdAsyncRequestSetUpdateParams | dict = {},
) -> str:
    """Update a AdAsyncRequestSet object.

    Args:
        adasyncrequestset_id: The ID of the AdAsyncRequestSet.
        fields: Fields to return after update. Available fields: See AdAsyncRequestSetField type.
        params: Parameters to update. Available params: See AdAsyncRequestSetUpdateParams type.
    """
    return AdAsyncRequestSet(adasyncrequestset_id).api_update(fields=fields, params=params)


@adasyncrequestset_server.tool
@wrapped_fn_tool
def delete_adasyncrequestset(
    adasyncrequestset_id: str,
) -> str:
    """Delete a AdAsyncRequestSet object.

    Args:
        adasyncrequestset_id: The ID of the AdAsyncRequestSet.
    """
    return AdAsyncRequestSet(adasyncrequestset_id).api_delete()


# ---- Edge Methods (1) ----
@adasyncrequestset_server.tool
@wrapped_fn_tool
def get_requests(
    adasyncrequestset_id: str,
    fields: list[AdAsyncRequestField] = [],
    params: AdAsyncRequestSetGetRequestsParams | dict = {},
):
    """Get Requests for this AdAsyncRequestSet.

    Args:
        adasyncrequestset_id: The ID of the AdAsyncRequestSet.
        fields: Fields to retrieve. Available fields: See AdAsyncRequestField type.
        params: Query parameters. Available params: See AdAsyncRequestSetGetRequestsParams type.
    """
    return AdAsyncRequestSet(adasyncrequestset_id).get_requests(fields=fields, params=params)

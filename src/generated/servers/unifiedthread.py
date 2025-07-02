"""UnifiedThread MCP Server with typed wrappers."""

from facebook_business.adobjects.unifiedthread import UnifiedThread
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.unifiedthread import UnifiedThreadField, UnifiedThreadGetMessagesParams
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookUnifiedThread"
instructions = """
UnifiedThread MCP Server for Facebook Business API.

Provides typed access to all UnifiedThread operations.
"""

unifiedthread_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@unifiedthread_server.tool
@wrapped_fn_tool
def get_unifiedthread(
    unifiedthread_id: str,
    fields: list[UnifiedThreadField] = [],
) -> str:
    """Get a UnifiedThread object by ID.

    Args:
        unifiedthread_id: The ID of the UnifiedThread.
        fields: Fields to retrieve. Available fields: See UnifiedThreadField type.
    """
    obj = UnifiedThread(unifiedthread_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (1) ----
@unifiedthread_server.tool
@wrapped_fn_tool
def get_messages(
    unifiedthread_id: str,
    fields: list[AbstractCrudObjectField] = [],
    params: UnifiedThreadGetMessagesParams | dict = {},
):
    """Get Messages for this UnifiedThread.

    Args:
        unifiedthread_id: The ID of the UnifiedThread.
        fields: Fields to retrieve. Available fields: See AbstractCrudObjectField type.
        params: Query parameters. Available params: See UnifiedThreadGetMessagesParams type.
    """
    return UnifiedThread(unifiedthread_id).get_messages(fields=fields, params=params)

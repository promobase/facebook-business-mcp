"""BizInboxOffsiteEmailAccount MCP Server with typed wrappers."""

from facebook_business.adobjects.bizinboxoffsiteemailaccount import BizInboxOffsiteEmailAccount
from fastmcp import FastMCP

from src.generated.models.bizinboxoffsiteemailaccount import BizInboxOffsiteEmailAccountField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBizInboxOffsiteEmailAccount"
instructions = """
BizInboxOffsiteEmailAccount MCP Server for Facebook Business API.

Provides typed access to all BizInboxOffsiteEmailAccount operations.
"""

bizinboxoffsiteemailaccount_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@bizinboxoffsiteemailaccount_server.tool
@wrapped_fn_tool
def get_bizinboxoffsiteemailaccount(
    bizinboxoffsiteemailaccount_id: str,
    fields: list[BizInboxOffsiteEmailAccountField] = [],
) -> str:
    """Get a BizInboxOffsiteEmailAccount object by ID.

    Args:
        bizinboxoffsiteemailaccount_id: The ID of the BizInboxOffsiteEmailAccount.
        fields: Fields to retrieve. Available fields: See BizInboxOffsiteEmailAccountField type.
    """
    obj = BizInboxOffsiteEmailAccount(bizinboxoffsiteemailaccount_id)
    return obj.api_get(fields=fields)

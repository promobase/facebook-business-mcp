"""AdRuleExecutionSpec MCP Server with typed wrappers."""

from facebook_business.adobjects.adruleexecutionspec import AdRuleExecutionSpec
from fastmcp import FastMCP

from src.generated.models.adruleexecutionspec import AdRuleExecutionSpecField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdRuleExecutionSpec"
instructions = """
AdRuleExecutionSpec MCP Server for Facebook Business API.

Provides typed access to all AdRuleExecutionSpec operations.
"""

adruleexecutionspec_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adruleexecutionspec_server.tool
@wrapped_fn_tool
def get_adruleexecutionspec(
    adruleexecutionspec_id: str,
    fields: list[AdRuleExecutionSpecField] = [],
) -> str:
    """Get a AdRuleExecutionSpec object by ID.

    Args:
        adruleexecutionspec_id: The ID of the AdRuleExecutionSpec.
        fields: Fields to retrieve. Available fields: See AdRuleExecutionSpecField type.
    """
    obj = AdRuleExecutionSpec(adruleexecutionspec_id)
    return obj.api_get(fields=fields)

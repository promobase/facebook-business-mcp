"""AdRuleEvaluationSpec MCP Server with typed wrappers."""

from facebook_business.adobjects.adruleevaluationspec import AdRuleEvaluationSpec
from fastmcp import FastMCP

from src.generated.models.adruleevaluationspec import AdRuleEvaluationSpecField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdRuleEvaluationSpec"
instructions = """
AdRuleEvaluationSpec MCP Server for Facebook Business API.

Provides typed access to all AdRuleEvaluationSpec operations.
"""

adruleevaluationspec_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@adruleevaluationspec_server.tool
@wrapped_fn_tool
def get_adruleevaluationspec(
    adruleevaluationspec_id: str,
    fields: list[AdRuleEvaluationSpecField] = [],
) -> str:
    """Get a AdRuleEvaluationSpec object by ID.

    Args:
        adruleevaluationspec_id: The ID of the AdRuleEvaluationSpec.
        fields: Fields to retrieve. Available fields: See AdRuleEvaluationSpecField type.
    """
    obj = AdRuleEvaluationSpec(adruleevaluationspec_id)
    return obj.api_get(fields=fields)

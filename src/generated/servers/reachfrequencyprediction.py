"""ReachFrequencyPrediction MCP Server with typed wrappers."""

from facebook_business.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
from fastmcp import FastMCP

from src.generated.models.reachfrequencyprediction import ReachFrequencyPredictionField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookReachFrequencyPrediction"
instructions = """
ReachFrequencyPrediction MCP Server for Facebook Business API.

Provides typed access to all ReachFrequencyPrediction operations.
"""

reachfrequencyprediction_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@reachfrequencyprediction_server.tool
@wrapped_fn_tool
def get_reachfrequencyprediction(
    reachfrequencyprediction_id: str,
    fields: list[ReachFrequencyPredictionField] = [],
) -> str:
    """Get a ReachFrequencyPrediction object by ID.

    Args:
        reachfrequencyprediction_id: The ID of the ReachFrequencyPrediction.
        fields: Fields to retrieve. Available fields: See ReachFrequencyPredictionField type.
    """
    obj = ReachFrequencyPrediction(reachfrequencyprediction_id)
    return obj.api_get(fields=fields)

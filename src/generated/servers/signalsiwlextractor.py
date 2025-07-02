"""SignalsIWLExtractor MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.signalsiwlextractor import SignalsIWLExtractor
from fastmcp import FastMCP

from src.generated.models.signalsiwlextractor import SignalsIWLExtractorField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookSignalsIWLExtractor"
instructions = """
SignalsIWLExtractor MCP Server for Facebook Business API.

Provides typed access to all SignalsIWLExtractor operations.
"""

signalsiwlextractor_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@signalsiwlextractor_server.tool
@wrapped_fn_tool
def get_signalsiwlextractor(
    signalsiwlextractor_id: str,
    fields: list[SignalsIWLExtractorField] = [],
) -> str:
    """Get a SignalsIWLExtractor object by ID.

    Args:
        signalsiwlextractor_id: The ID of the SignalsIWLExtractor.
        fields: Fields to retrieve. Available fields: See SignalsIWLExtractorField type.
    """
    obj = SignalsIWLExtractor(signalsiwlextractor_id)
    return obj.api_get(fields=fields)

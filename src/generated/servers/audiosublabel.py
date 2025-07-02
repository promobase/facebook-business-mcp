"""AudioSubLabel MCP Server with typed wrappers."""

from facebook_business.adobjects.audiosublabel import AudioSubLabel
from fastmcp import FastMCP

from src.generated.models.audiosublabel import AudioSubLabelField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAudioSubLabel"
instructions = """
AudioSubLabel MCP Server for Facebook Business API.

Provides typed access to all AudioSubLabel operations.
"""

audiosublabel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@audiosublabel_server.tool
@wrapped_fn_tool
def get_audiosublabel(
    audiosublabel_id: str,
    fields: list[AudioSubLabelField] = [],
) -> str:
    """Get a AudioSubLabel object by ID.

    Args:
        audiosublabel_id: The ID of the AudioSubLabel.
        fields: Fields to retrieve. Available fields: See AudioSubLabelField type.
    """
    obj = AudioSubLabel(audiosublabel_id)
    return obj.api_get(fields=fields)

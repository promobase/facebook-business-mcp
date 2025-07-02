"""LiveVideoInputStream MCP Server with typed wrappers."""

from facebook_business.adobjects.livevideoinputstream import LiveVideoInputStream
from fastmcp import FastMCP

from src.generated.models.livevideoinputstream import LiveVideoInputStreamField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookLiveVideoInputStream"
instructions = """
LiveVideoInputStream MCP Server for Facebook Business API.

Provides typed access to all LiveVideoInputStream operations.
"""

livevideoinputstream_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@livevideoinputstream_server.tool
@wrapped_fn_tool
def get_livevideoinputstream(
    livevideoinputstream_id: str,
    fields: list[LiveVideoInputStreamField] = [],
) -> str:
    """Get a LiveVideoInputStream object by ID.

    Args:
        livevideoinputstream_id: The ID of the LiveVideoInputStream.
        fields: Fields to retrieve. Available fields: See LiveVideoInputStreamField type.
    """
    obj = LiveVideoInputStream(livevideoinputstream_id)
    return obj.api_get(fields=fields)

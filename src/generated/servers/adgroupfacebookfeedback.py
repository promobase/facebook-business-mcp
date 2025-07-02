"""AdgroupFacebookFeedback MCP Server with typed wrappers."""

from __future__ import annotations

from facebook_business.adobjects.adgroupfacebookfeedback import AdgroupFacebookFeedback
from fastmcp import FastMCP

from src.generated.models.adgroupfacebookfeedback import (
    AdgroupFacebookFeedbackField,
    AdgroupFacebookFeedbackGetCommentsParams,
)
from src.generated.models.comment import CommentField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAdgroupFacebookFeedback"
instructions = """
AdgroupFacebookFeedback MCP Server for Facebook Business API.

Provides typed access to all AdgroupFacebookFeedback operations.
"""

adgroupfacebookfeedback_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- Edge Methods (1) ----
@adgroupfacebookfeedback_server.tool
@wrapped_fn_tool
def get_comments(
    adgroupfacebookfeedback_id: str,
    fields: list[CommentField] = [],
    params: AdgroupFacebookFeedbackGetCommentsParams | dict = {},
):
    """Get Comments for this AdgroupFacebookFeedback.

    Args:
        adgroupfacebookfeedback_id: The ID of the AdgroupFacebookFeedback.
        fields: Fields to retrieve. Available fields: See CommentField type.
        params: Query parameters. Available params: See AdgroupFacebookFeedbackGetCommentsParams type.
    """
    return AdgroupFacebookFeedback(adgroupfacebookfeedback_id).get_comments(
        fields=fields, params=params
    )

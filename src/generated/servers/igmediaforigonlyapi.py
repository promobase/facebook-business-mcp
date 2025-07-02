"""IGMediaForIGOnlyAPI MCP Server with typed wrappers."""

from facebook_business.adobjects.igmediaforigonlyapi import IGMediaForIGOnlyAPI
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.igmediaforigonlyapi import (
    IGMediaForIGOnlyAPICreateCommentParams,
    IGMediaForIGOnlyAPIField,
    IGMediaForIGOnlyAPIGetInsightsParams,
    IGMediaForIGOnlyAPIUpdateParams,
)
from src.generated.models.insightsresult import InsightsResultField
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookIGMediaForIGOnlyAPI"
instructions = """
IGMediaForIGOnlyAPI MCP Server for Facebook Business API.

Provides typed access to all IGMediaForIGOnlyAPI operations.
"""

igmediaforigonlyapi_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def get_igmediaforigonlyapi(
    igmediaforigonlyapi_id: str,
    fields: list[IGMediaForIGOnlyAPIField] = [],
) -> str:
    """Get a IGMediaForIGOnlyAPI object by ID.

    Args:
        igmediaforigonlyapi_id: The ID of the IGMediaForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See IGMediaForIGOnlyAPIField type.
    """
    obj = IGMediaForIGOnlyAPI(igmediaforigonlyapi_id)
    return obj.api_get(fields=fields)


@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def update_igmediaforigonlyapi(
    igmediaforigonlyapi_id: str,
    fields: list[IGMediaForIGOnlyAPIField] = [],
    params: IGMediaForIGOnlyAPIUpdateParams | dict = {},
) -> str:
    """Update a IGMediaForIGOnlyAPI object.

    Args:
        igmediaforigonlyapi_id: The ID of the IGMediaForIGOnlyAPI.
        fields: Fields to return after update. Available fields: See IGMediaForIGOnlyAPIField type.
        params: Parameters to update. Available params: See IGMediaForIGOnlyAPIUpdateParams type.
    """
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).api_update(fields=fields, params=params)


# ---- Edge Methods (2) ----
@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def create_comment(
    igmediaforigonlyapi_id: str,
    fields: list[str] = [],
    params: IGMediaForIGOnlyAPICreateCommentParams | dict = {},
):
    """Create Comment for this IGMediaForIGOnlyAPI.

    Args:
        igmediaforigonlyapi_id: The ID of the IGMediaForIGOnlyAPI.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See IGMediaForIGOnlyAPICreateCommentParams type.
    """
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).create_comment(fields=fields, params=params)


@igmediaforigonlyapi_server.tool
@wrapped_fn_tool
def get_insights(
    igmediaforigonlyapi_id: str,
    fields: list[InsightsResultField] = [],
    params: IGMediaForIGOnlyAPIGetInsightsParams | dict = {},
):
    """Get Insights for this IGMediaForIGOnlyAPI.

    Args:
        igmediaforigonlyapi_id: The ID of the IGMediaForIGOnlyAPI.
        fields: Fields to retrieve. Available fields: See InsightsResultField type.
        params: Query parameters. Available params: See IGMediaForIGOnlyAPIGetInsightsParams type.
    """
    return IGMediaForIGOnlyAPI(igmediaforigonlyapi_id).get_insights(fields=fields, params=params)

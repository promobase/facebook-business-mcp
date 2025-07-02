"""AutomotiveModel MCP Server."""

from typing import Any

from facebook_business.adobjects.automotivemodel import AutomotiveModel
from fastmcp import FastMCP

from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookAutomotiveModel"
instructions = """
AutomotiveModel MCP Server for Facebook Business API.

Provides typed access to all AutomotiveModel operations.
"""

automotivemodel_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@automotivemodel_server.tool
@wrapped_fn_tool
def get_automotivemodel(
    automotivemodel_id: str,
    fields: list[str] = [],
) -> str:
    obj = AutomotiveModel(automotivemodel_id)
    return obj.api_get(fields=fields)


# ---- Edge Methods (3) ----
@automotivemodel_server.tool
@wrapped_fn_tool
def get_channels_to_integrity_status(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AutomotiveModel(automotivemodel_id).get_channels_to_integrity_status(
        fields=fields, params=params
    )


@automotivemodel_server.tool
@wrapped_fn_tool
def get_override_details(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AutomotiveModel(automotivemodel_id).get_override_details(fields=fields, params=params)


@automotivemodel_server.tool
@wrapped_fn_tool
def get_videos_metadata(
    automotivemodel_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
):
    return AutomotiveModel(automotivemodel_id).get_videos_metadata(fields=fields, params=params)

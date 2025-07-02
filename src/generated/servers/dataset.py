"""
Auto-generated MCP server for Facebook Dataset.
DO NOT EDIT MANUALLY.
"""

from typing import Any, Optional

from facebook_business.adobjects.dataset import Dataset
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("facebook-dataset")


# CRUD Operations


@mcp.tool()
async def api_create_dataset(
    dataset_id: str,
    parent_id: Optional[Any] = None,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Dataset(fbid=dataset_id).api_create(
        parent_id=parent_id,
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_delete_dataset(
    dataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Dataset(fbid=dataset_id).api_delete(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_get_dataset(
    dataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Dataset(fbid=dataset_id).api_get(
        fields=fields,
        params=params,
    )

    return result


@mcp.tool()
async def api_update_dataset(
    dataset_id: str,
    fields: list[str] = [],
    params: dict[str, Any] = {},
) -> dict[str, Any]:
    result = Dataset(fbid=dataset_id).api_update(
        fields=fields,
        params=params,
    )

    return result


# Export the server
dataset_server = mcp

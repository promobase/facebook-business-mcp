"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adasyncrequestset import AdAsyncRequestSetFields


# Field literal type
AdAsyncRequestField = Literal[
    "async_request_set",
    "created_time",
    "id",
    "input",
    "result",
    "scope_object_id",
    "status",
    "type",
    "updated_time",
]


class AdAsyncRequestFields(BaseModel):
    """Pydantic model for AdAsyncRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    async_request_set: AdAsyncRequestSetFields = Field(None, alias="async_request_set")
    created_time: datetime = Field(None, alias="created_time")
    id: str = Field(None, alias="id")
    input: dict[str, Any] = Field(None, alias="input")
    result: dict[str, Any] = Field(None, alias="result")
    scope_object_id: str = Field(None, alias="scope_object_id")
    status: str = Field(None, alias="status")
    type: str = Field(None, alias="type")
    updated_time: datetime = Field(None, alias="updated_time")

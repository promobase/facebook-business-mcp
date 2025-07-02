"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessRequestField = Literal[
    "accessor",
    "creation_time",
    "id",
    "object_id",
    "object_type",
    "permitted_tasks",
    "request_status",
    "request_type",
    "requestor",
]


class BusinessRequestFields(BaseModel):
    """Pydantic model for BusinessRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    accessor: BusinessFields = Field(None, alias="accessor")
    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    object_id: str = Field(None, alias="object_id")
    object_type: str = Field(None, alias="object_type")
    permitted_tasks: list[str] = Field(None, alias="permitted_tasks")
    request_status: str = Field(None, alias="request_status")
    request_type: str = Field(None, alias="request_type")
    requestor: str = Field(None, alias="requestor")

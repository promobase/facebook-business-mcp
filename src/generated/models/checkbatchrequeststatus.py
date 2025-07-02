"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CheckBatchRequestStatusField = Literal[
    "errors",
    "errors_total_count",
    "handle",
    "ids_of_invalid_requests",
    "status",
    "warnings",
    "warnings_total_count",
]


class CheckBatchRequestStatusFields(BaseModel):
    """Pydantic model for CheckBatchRequestStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    errors: list[dict[str, Any]] = Field(None, alias="errors")
    errors_total_count: int = Field(None, alias="errors_total_count")
    handle: str = Field(None, alias="handle")
    ids_of_invalid_requests: list[str] = Field(None, alias="ids_of_invalid_requests")
    status: str = Field(None, alias="status")
    warnings: list[dict[str, Any]] = Field(None, alias="warnings")
    warnings_total_count: int = Field(None, alias="warnings_total_count")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ProductFeedUploadError_severity(str, Enum):
    """ProductFeedUploadError_severity enum values."""

    fatal = "fatal"
    warning = "warning"


# Field literal type
ProductFeedUploadErrorField = Literal[
    "affected_surfaces", "description", "error_type", "id", "severity", "summary", "total_count"
]


class ProductFeedUploadErrorFields(BaseModel):
    """Pydantic model for ProductFeedUploadError fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    affected_surfaces: list[dict[str, Any]] = Field(None, alias="affected_surfaces")
    description: str = Field(None, alias="description")
    error_type: str = Field(None, alias="error_type")
    id: str = Field(None, alias="id")
    severity: dict[str, Any] = Field(None, alias="severity")
    summary: str = Field(None, alias="summary")
    total_count: int = Field(None, alias="total_count")

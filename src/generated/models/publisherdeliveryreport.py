"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PublisherDeliveryReportField = Literal[
    "content_types", "estimated_impressions", "name", "status", "url"
]


class PublisherDeliveryReportFields(BaseModel):
    """Pydantic model for PublisherDeliveryReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    content_types: list[str] = Field(None, alias="content_types")
    estimated_impressions: int = Field(None, alias="estimated_impressions")
    name: str = Field(None, alias="name")
    status: str = Field(None, alias="status")
    url: str = Field(None, alias="url")

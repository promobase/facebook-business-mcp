"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ContentDeliveryReportField = Literal[
    "content_id",
    "content_name",
    "content_url",
    "creator_id",
    "creator_name",
    "creator_url",
    "estimated_impressions",
]


class ContentDeliveryReportFields(BaseModel):
    """Pydantic model for ContentDeliveryReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    content_id: str = Field(None, alias="content_id")
    content_name: str = Field(None, alias="content_name")
    content_url: str = Field(None, alias="content_url")
    creator_id: str = Field(None, alias="creator_id")
    creator_name: str = Field(None, alias="creator_name")
    creator_url: str = Field(None, alias="creator_url")
    estimated_impressions: int = Field(None, alias="estimated_impressions")

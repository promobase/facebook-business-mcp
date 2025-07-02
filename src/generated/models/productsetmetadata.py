"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductSetMetadataField = Literal[
    "cover_image_url", "description", "external_url", "integrity_review_status"
]


class ProductSetMetadataFields(BaseModel):
    """Pydantic model for ProductSetMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    cover_image_url: str = Field(None, alias="cover_image_url")
    description: str = Field(None, alias="description")
    external_url: str = Field(None, alias="external_url")
    integrity_review_status: str = Field(None, alias="integrity_review_status")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LeadGenThankYouPageGatedFileField = Literal["file_cdn_url", "file_name", "file_size_bytes", "id"]


class LeadGenThankYouPageGatedFileFields(BaseModel):
    """Pydantic model for LeadGenThankYouPageGatedFile fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    file_cdn_url: str = Field(None, alias="file_cdn_url")
    file_name: str = Field(None, alias="file_name")
    file_size_bytes: int = Field(None, alias="file_size_bytes")
    id: str = Field(None, alias="id")

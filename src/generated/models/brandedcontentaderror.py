"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BrandedContentAdErrorField = Literal[
    "blame_field_spec",
    "error_code",
    "error_description",
    "error_message",
    "error_placement",
    "error_severity",
    "help_center_id",
]


class BrandedContentAdErrorFields(BaseModel):
    """Pydantic model for BrandedContentAdError fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    blame_field_spec: list[str] = Field(None, alias="blame_field_spec")
    error_code: int = Field(None, alias="error_code")
    error_description: str = Field(None, alias="error_description")
    error_message: str = Field(None, alias="error_message")
    error_placement: str = Field(None, alias="error_placement")
    error_severity: str = Field(None, alias="error_severity")
    help_center_id: int = Field(None, alias="help_center_id")

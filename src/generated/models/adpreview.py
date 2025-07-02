"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdPreviewField = Literal["body", "transformation_spec"]


class AdPreviewFields(BaseModel):
    """Pydantic model for AdPreview fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    body: str = Field(None, alias="body")
    transformation_spec: dict[str, Any] = Field(None, alias="transformation_spec")

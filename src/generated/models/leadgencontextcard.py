"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .photo import PhotoFields


# Field literal type
LeadGenContextCardField = Literal["button_text", "content", "cover_photo", "id", "style", "title"]


class LeadGenContextCardFields(BaseModel):
    """Pydantic model for LeadGenContextCard fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    button_text: str = Field(None, alias="button_text")
    content: list[str] = Field(None, alias="content")
    cover_photo: PhotoFields = Field(None, alias="cover_photo")
    id: str = Field(None, alias="id")
    style: str = Field(None, alias="style")
    title: str = Field(None, alias="title")

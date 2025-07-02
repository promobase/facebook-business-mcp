"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativetemplateurlspec import AdCreativeTemplateURLSpecFields


# Field literal type
AdCustomizationRuleSpecField = Literal[
    "caption",
    "customization_spec",
    "description",
    "image_hash",
    "link",
    "message",
    "name",
    "priority",
    "template_url_spec",
    "video_id",
]


class AdCustomizationRuleSpecFields(BaseModel):
    """Pydantic model for AdCustomizationRuleSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    caption: str = Field(None, alias="caption")
    customization_spec: dict[str, Any] = Field(None, alias="customization_spec")
    description: str = Field(None, alias="description")
    image_hash: str = Field(None, alias="image_hash")
    link: str = Field(None, alias="link")
    message: str = Field(None, alias="message")
    name: str = Field(None, alias="name")
    priority: int = Field(None, alias="priority")
    template_url_spec: AdCreativeTemplateURLSpecFields = Field(None, alias="template_url_spec")
    video_id: int = Field(None, alias="video_id")

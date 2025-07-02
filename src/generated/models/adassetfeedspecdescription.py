"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields


# Field literal type
AdAssetFeedSpecDescriptionField = Literal["adlabels", "text", "url_tags"]


class AdAssetFeedSpecDescriptionFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecDescription fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adlabels: list[AdAssetFeedSpecAssetLabelFields] = Field(None, alias="adlabels")
    text: str = Field(None, alias="text")
    url_tags: str = Field(None, alias="url_tags")

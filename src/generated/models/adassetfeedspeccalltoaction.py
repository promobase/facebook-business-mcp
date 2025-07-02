"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields
    from .adcreativelinkdatacalltoactionvalue import AdCreativeLinkDataCallToActionValueFields


# Field literal type
AdAssetFeedSpecCallToActionField = Literal["adlabels", "type", "value"]


class AdAssetFeedSpecCallToActionFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecCallToAction fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adlabels: list[AdAssetFeedSpecAssetLabelFields] = Field(None, alias="adlabels")
    type: str = Field(None, alias="type")
    value: AdCreativeLinkDataCallToActionValueFields = Field(None, alias="value")

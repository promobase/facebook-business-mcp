"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .androidapplink import AndroidAppLinkFields
    from .iosapplink import IosAppLinkFields


# Field literal type
AdCreativeLinkDataAppLinkSpecField = Literal["android", "ios", "ipad", "iphone"]


class AdCreativeLinkDataAppLinkSpecFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataAppLinkSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    android: list[AndroidAppLinkFields] = Field(None, alias="android")
    ios: list[IosAppLinkFields] = Field(None, alias="ios")
    ipad: list[IosAppLinkFields] = Field(None, alias="ipad")
    iphone: list[IosAppLinkFields] = Field(None, alias="iphone")

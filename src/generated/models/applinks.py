"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .androidapplink import AndroidAppLinkFields
    from .iosapplink import IosAppLinkFields
    from .webapplink import WebAppLinkFields
    from .windowsapplink import WindowsAppLinkFields
    from .windowsphoneapplink import WindowsPhoneAppLinkFields


# Field literal type
AppLinksField = Literal[
    "android", "id", "ios", "ipad", "iphone", "web", "windows", "windows_phone", "windows_universal"
]


class AppLinksFields(BaseModel):
    """Pydantic model for AppLinks fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    android: list[AndroidAppLinkFields] = Field(None, alias="android")
    id: str = Field(None, alias="id")
    ios: list[IosAppLinkFields] = Field(None, alias="ios")
    ipad: list[IosAppLinkFields] = Field(None, alias="ipad")
    iphone: list[IosAppLinkFields] = Field(None, alias="iphone")
    web: WebAppLinkFields = Field(None, alias="web")
    windows: list[WindowsAppLinkFields] = Field(None, alias="windows")
    windows_phone: list[WindowsPhoneAppLinkFields] = Field(None, alias="windows_phone")
    windows_universal: list[WindowsAppLinkFields] = Field(None, alias="windows_universal")

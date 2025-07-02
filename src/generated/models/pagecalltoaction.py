"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .page import PageFields


# Field literal type
PageCallToActionField = Literal[
    "android_app",
    "android_deeplink",
    "android_destination_type",
    "android_package_name",
    "android_url",
    "created_time",
    "email_address",
    "from",
    "id",
    "intl_number_with_plus",
    "iphone_app",
    "iphone_deeplink",
    "iphone_destination_type",
    "iphone_url",
    "status",
    "type",
    "updated_time",
    "web_destination_type",
    "web_url",
]


class PageCallToActionFields(BaseModel):
    """Pydantic model for PageCallToAction fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    android_app: ApplicationFields = Field(None, alias="android_app")
    android_deeplink: str = Field(None, alias="android_deeplink")
    android_destination_type: str = Field(None, alias="android_destination_type")
    android_package_name: str = Field(None, alias="android_package_name")
    android_url: str = Field(None, alias="android_url")
    created_time: datetime = Field(None, alias="created_time")
    email_address: str = Field(None, alias="email_address")
    from_: PageFields = Field(None, alias="from")
    id: str = Field(None, alias="id")
    intl_number_with_plus: str = Field(None, alias="intl_number_with_plus")
    iphone_app: ApplicationFields = Field(None, alias="iphone_app")
    iphone_deeplink: str = Field(None, alias="iphone_deeplink")
    iphone_destination_type: str = Field(None, alias="iphone_destination_type")
    iphone_url: str = Field(None, alias="iphone_url")
    status: str = Field(None, alias="status")
    type: str = Field(None, alias="type")
    updated_time: datetime = Field(None, alias="updated_time")
    web_destination_type: str = Field(None, alias="web_destination_type")
    web_url: str = Field(None, alias="web_url")

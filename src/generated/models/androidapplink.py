"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AndroidAppLinkField = Literal["app_name", "class", "package", "url"]


class AndroidAppLinkFields(BaseModel):
    """Pydantic model for AndroidAppLink fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_name: str = Field(None, alias="app_name")
    class_: str = Field(None, alias="class")
    package: str = Field(None, alias="package")
    url: str = Field(None, alias="url")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields


# Field literal type
TabField = Literal[
    "application",
    "custom_image_url",
    "custom_name",
    "id",
    "image_url",
    "is_non_connection_landing_tab",
    "is_permanent",
    "link",
    "name",
    "position",
]


class TabFields(BaseModel):
    """Pydantic model for Tab fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    application: ApplicationFields = Field(None, alias="application")
    custom_image_url: str = Field(None, alias="custom_image_url")
    custom_name: str = Field(None, alias="custom_name")
    id: str = Field(None, alias="id")
    image_url: str = Field(None, alias="image_url")
    is_non_connection_landing_tab: bool = Field(None, alias="is_non_connection_landing_tab")
    is_permanent: bool = Field(None, alias="is_permanent")
    link: str = Field(None, alias="link")
    name: str = Field(None, alias="name")
    position: int = Field(None, alias="position")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields


# Field literal type
HotelRoomField = Literal[
    "applinks",
    "base_price",
    "currency",
    "description",
    "id",
    "images",
    "margin_level",
    "name",
    "room_id",
    "sale_price",
    "url",
]


class HotelRoomFields(BaseModel):
    """Pydantic model for HotelRoom fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    base_price: str = Field(None, alias="base_price")
    currency: str = Field(None, alias="currency")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    images: list[str] = Field(None, alias="images")
    margin_level: str = Field(None, alias="margin_level")
    name: str = Field(None, alias="name")
    room_id: str = Field(None, alias="room_id")
    sale_price: str = Field(None, alias="sale_price")
    url: str = Field(None, alias="url")

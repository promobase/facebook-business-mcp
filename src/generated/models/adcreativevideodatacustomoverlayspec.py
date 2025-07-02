"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdCreativeVideoDataCustomOverlaySpec_background_opacity(str, Enum):
    """AdCreativeVideoDataCustomOverlaySpec_background_opacity enum values."""

    half = "half"
    solid = "solid"


class AdCreativeVideoDataCustomOverlaySpec_option(str, Enum):
    """AdCreativeVideoDataCustomOverlaySpec_option enum values."""

    bank_transfer = "bank_transfer"
    boleto = "boleto"
    cash_on_delivery = "cash_on_delivery"
    discount_with_boleto = "discount_with_boleto"
    fast_delivery = "fast_delivery"
    free_shipping = "free_shipping"
    home_delivery = "home_delivery"
    inventory = "inventory"
    pay_at_hotel = "pay_at_hotel"
    pay_on_arrival = "pay_on_arrival"


class AdCreativeVideoDataCustomOverlaySpec_position(str, Enum):
    """AdCreativeVideoDataCustomOverlaySpec_position enum values."""

    middle_center = "middle_center"
    middle_left = "middle_left"
    middle_right = "middle_right"
    top_center = "top_center"
    top_left = "top_left"
    top_right = "top_right"


class AdCreativeVideoDataCustomOverlaySpec_template(str, Enum):
    """AdCreativeVideoDataCustomOverlaySpec_template enum values."""

    rectangle_with_text = "rectangle_with_text"


# Field literal type
AdCreativeVideoDataCustomOverlaySpecField = Literal[
    "background_color",
    "background_opacity",
    "duration",
    "float_with_margin",
    "full_width",
    "option",
    "position",
    "start",
    "template",
    "text_color",
]


class AdCreativeVideoDataCustomOverlaySpecFields(BaseModel):
    """Pydantic model for AdCreativeVideoDataCustomOverlaySpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    background_color: str = Field(None, alias="background_color")
    background_opacity: dict[str, Any] = Field(None, alias="background_opacity")
    duration: int = Field(None, alias="duration")
    float_with_margin: bool = Field(None, alias="float_with_margin")
    full_width: bool = Field(None, alias="full_width")
    option: dict[str, Any] = Field(None, alias="option")
    position: dict[str, Any] = Field(None, alias="position")
    start: int = Field(None, alias="start")
    template: dict[str, Any] = Field(None, alias="template")
    text_color: str = Field(None, alias="text_color")

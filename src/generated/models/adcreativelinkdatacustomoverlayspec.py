"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdCreativeLinkDataCustomOverlaySpec_background_color(str, Enum):
    """AdCreativeLinkDataCustomOverlaySpec_background_color enum values."""

    background_000000 = "background_000000"
    background_0090ff = "background_0090ff"
    background_00af4c = "background_00af4c"
    background_595959 = "background_595959"
    background_755dde = "background_755dde"
    background_e50900 = "background_e50900"
    background_f23474 = "background_f23474"
    background_f78400 = "background_f78400"
    background_ffffff = "background_ffffff"


class AdCreativeLinkDataCustomOverlaySpec_font(str, Enum):
    """AdCreativeLinkDataCustomOverlaySpec_font enum values."""

    droid_serif_regular = "droid_serif_regular"
    lato_regular = "lato_regular"
    noto_sans_regular = "noto_sans_regular"
    nunito_sans_bold = "nunito_sans_bold"
    open_sans_bold = "open_sans_bold"
    pt_serif_bold = "pt_serif_bold"
    roboto_condensed_regular = "roboto_condensed_regular"
    roboto_medium = "roboto_medium"


class AdCreativeLinkDataCustomOverlaySpec_option(str, Enum):
    """AdCreativeLinkDataCustomOverlaySpec_option enum values."""

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


class AdCreativeLinkDataCustomOverlaySpec_position(str, Enum):
    """AdCreativeLinkDataCustomOverlaySpec_position enum values."""

    bottom_left = "bottom_left"
    bottom_right = "bottom_right"
    top_left = "top_left"
    top_right = "top_right"


class AdCreativeLinkDataCustomOverlaySpec_template(str, Enum):
    """AdCreativeLinkDataCustomOverlaySpec_template enum values."""

    pill_with_text = "pill_with_text"


class AdCreativeLinkDataCustomOverlaySpec_text_color(str, Enum):
    """AdCreativeLinkDataCustomOverlaySpec_text_color enum values."""

    text_000000 = "text_000000"
    text_007ad0 = "text_007ad0"
    text_009c2a = "text_009c2a"
    text_646464 = "text_646464"
    text_755dde = "text_755dde"
    text_c91b00 = "text_c91b00"
    text_f23474 = "text_f23474"
    text_f78400 = "text_f78400"
    text_ffffff = "text_ffffff"


# Field literal type
AdCreativeLinkDataCustomOverlaySpecField = Literal[
    "background_color",
    "float_with_margin",
    "font",
    "option",
    "position",
    "render_with_icon",
    "template",
    "text_color",
]


class AdCreativeLinkDataCustomOverlaySpecFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataCustomOverlaySpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    background_color: dict[str, Any] = Field(None, alias="background_color")
    float_with_margin: bool = Field(None, alias="float_with_margin")
    font: dict[str, Any] = Field(None, alias="font")
    option: dict[str, Any] = Field(None, alias="option")
    position: dict[str, Any] = Field(None, alias="position")
    render_with_icon: bool = Field(None, alias="render_with_icon")
    template: dict[str, Any] = Field(None, alias="template")
    text_color: dict[str, Any] = Field(None, alias="text_color")

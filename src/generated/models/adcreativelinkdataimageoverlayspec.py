"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdCreativeLinkDataImageOverlaySpec_custom_text_type(str, Enum):
    """AdCreativeLinkDataImageOverlaySpec_custom_text_type enum values."""

    free_shipping = "free_shipping"
    popular = "popular"
    sale = "sale"


class AdCreativeLinkDataImageOverlaySpec_overlay_template(str, Enum):
    """AdCreativeLinkDataImageOverlaySpec_overlay_template enum values."""

    circle_with_text = "circle_with_text"
    pill_with_text = "pill_with_text"
    triangle_with_text = "triangle_with_text"


class AdCreativeLinkDataImageOverlaySpec_position(str, Enum):
    """AdCreativeLinkDataImageOverlaySpec_position enum values."""

    bottom_left = "bottom_left"
    bottom_right = "bottom_right"
    top_left = "top_left"
    top_right = "top_right"


class AdCreativeLinkDataImageOverlaySpec_text_font(str, Enum):
    """AdCreativeLinkDataImageOverlaySpec_text_font enum values."""

    droid_serif_regular = "droid_serif_regular"
    dynads_hybrid_bold = "dynads_hybrid_bold"
    lato_regular = "lato_regular"
    noto_sans_regular = "noto_sans_regular"
    nunito_sans_bold = "nunito_sans_bold"
    open_sans_bold = "open_sans_bold"
    open_sans_condensed_bold = "open_sans_condensed_bold"
    pt_serif_bold = "pt_serif_bold"
    roboto_condensed_regular = "roboto_condensed_regular"
    roboto_medium = "roboto_medium"


class AdCreativeLinkDataImageOverlaySpec_text_type(str, Enum):
    """AdCreativeLinkDataImageOverlaySpec_text_type enum values."""

    automated_personalize = "automated_personalize"
    custom = "custom"
    disclaimer = "disclaimer"
    from_price = "from_price"
    guest_rating = "guest_rating"
    percentage_off = "percentage_off"
    price = "price"
    star_rating = "star_rating"
    strikethrough_price = "strikethrough_price"
    sustainable = "sustainable"


class AdCreativeLinkDataImageOverlaySpec_theme_color(str, Enum):
    """AdCreativeLinkDataImageOverlaySpec_theme_color enum values."""

    background_000000_text_ffffff = "background_000000_text_ffffff"
    background_0090ff_text_ffffff = "background_0090ff_text_ffffff"
    background_00af4c_text_ffffff = "background_00af4c_text_ffffff"
    background_595959_text_ffffff = "background_595959_text_ffffff"
    background_755dde_text_ffffff = "background_755dde_text_ffffff"
    background_e50900_text_ffffff = "background_e50900_text_ffffff"
    background_f23474_text_ffffff = "background_f23474_text_ffffff"
    background_f78400_text_ffffff = "background_f78400_text_ffffff"
    background_ffffff_text_000000 = "background_ffffff_text_000000"
    background_ffffff_text_007ad0 = "background_ffffff_text_007ad0"
    background_ffffff_text_009c2a = "background_ffffff_text_009c2a"
    background_ffffff_text_646464 = "background_ffffff_text_646464"
    background_ffffff_text_755dde = "background_ffffff_text_755dde"
    background_ffffff_text_c91b00 = "background_ffffff_text_c91b00"
    background_ffffff_text_f23474 = "background_ffffff_text_f23474"
    background_ffffff_text_f78400 = "background_ffffff_text_f78400"


# Field literal type
AdCreativeLinkDataImageOverlaySpecField = Literal[
    "custom_text_type",
    "float_with_margin",
    "overlay_template",
    "position",
    "text_font",
    "text_template_tags",
    "text_type",
    "theme_color",
]


class AdCreativeLinkDataImageOverlaySpecFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataImageOverlaySpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_text_type: dict[str, Any] = Field(None, alias="custom_text_type")
    float_with_margin: bool = Field(None, alias="float_with_margin")
    overlay_template: dict[str, Any] = Field(None, alias="overlay_template")
    position: dict[str, Any] = Field(None, alias="position")
    text_font: dict[str, Any] = Field(None, alias="text_font")
    text_template_tags: list[str] = Field(None, alias="text_template_tags")
    text_type: dict[str, Any] = Field(None, alias="text_type")
    theme_color: dict[str, Any] = Field(None, alias="theme_color")

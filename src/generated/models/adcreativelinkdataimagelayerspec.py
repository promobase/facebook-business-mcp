"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdCreativeLinkDataImageLayerSpec_blending_mode(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_blending_mode enum values."""

    lighten = "lighten"
    multiply = "multiply"
    normal = "normal"


class AdCreativeLinkDataImageLayerSpec_frame_source(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_frame_source enum values."""

    custom = "custom"


class AdCreativeLinkDataImageLayerSpec_image_source(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_image_source enum values."""

    catalog = "catalog"


class AdCreativeLinkDataImageLayerSpec_layer_type(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_layer_type enum values."""

    frame_overlay = "frame_overlay"
    image = "image"
    text_overlay = "text_overlay"


class AdCreativeLinkDataImageLayerSpec_overlay_position(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_overlay_position enum values."""

    bottom = "bottom"
    bottom_left = "bottom_left"
    bottom_right = "bottom_right"
    center = "center"
    left = "left"
    right = "right"
    top = "top"
    top_left = "top_left"
    top_right = "top_right"


class AdCreativeLinkDataImageLayerSpec_overlay_shape(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_overlay_shape enum values."""

    circle = "circle"
    none = "none"
    pill = "pill"
    rectangle = "rectangle"
    triangle = "triangle"


class AdCreativeLinkDataImageLayerSpec_text_font(str, Enum):
    """AdCreativeLinkDataImageLayerSpec_text_font enum values."""

    droid_serif_regular = "droid_serif_regular"
    lato_regular = "lato_regular"
    noto_sans_regular = "noto_sans_regular"
    nunito_sans_bold = "nunito_sans_bold"
    open_sans_bold = "open_sans_bold"
    open_sans_condensed_bold = "open_sans_condensed_bold"
    pt_serif_bold = "pt_serif_bold"
    roboto_condensed_regular = "roboto_condensed_regular"
    roboto_medium = "roboto_medium"


# Field literal type
AdCreativeLinkDataImageLayerSpecField = Literal[
    "blending_mode",
    "content",
    "frame_auto_show_enroll_status",
    "frame_image_hash",
    "frame_source",
    "image_source",
    "layer_type",
    "opacity",
    "overlay_position",
    "overlay_shape",
    "scale",
    "shape_color",
    "text_color",
    "text_font",
]


class AdCreativeLinkDataImageLayerSpecFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataImageLayerSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    blending_mode: dict[str, Any] = Field(None, alias="blending_mode")
    content: dict[str, Any] = Field(None, alias="content")
    frame_auto_show_enroll_status: str = Field(None, alias="frame_auto_show_enroll_status")
    frame_image_hash: str = Field(None, alias="frame_image_hash")
    frame_source: dict[str, Any] = Field(None, alias="frame_source")
    image_source: dict[str, Any] = Field(None, alias="image_source")
    layer_type: dict[str, Any] = Field(None, alias="layer_type")
    opacity: int = Field(None, alias="opacity")
    overlay_position: dict[str, Any] = Field(None, alias="overlay_position")
    overlay_shape: dict[str, Any] = Field(None, alias="overlay_shape")
    scale: int = Field(None, alias="scale")
    shape_color: str = Field(None, alias="shape_color")
    text_color: str = Field(None, alias="text_color")
    text_font: dict[str, Any] = Field(None, alias="text_font")

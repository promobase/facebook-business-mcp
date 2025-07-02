"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .dynamicpostchildattachment import DynamicPostChildAttachmentFields


class rtbdynamicpostcomments_filter_enum_param(str, Enum):
    """rtbdynamicpostcomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


class rtbdynamicpostcomments_order_enum_param(str, Enum):
    """rtbdynamicpostcomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class rtbdynamicpostcomments_live_filter_enum_param(str, Enum):
    """rtbdynamicpostcomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


# Field literal type
RTBDynamicPostField = Literal[
    "child_attachments",
    "created",
    "description",
    "id",
    "image_url",
    "link",
    "message",
    "owner_id",
    "place_id",
    "product_id",
    "title",
]


class RTBDynamicPostFields(BaseModel):
    """Pydantic model for RTBDynamicPost fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    child_attachments: list[DynamicPostChildAttachmentFields] = Field(
        None, alias="child_attachments"
    )
    created: datetime = Field(None, alias="created")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    image_url: str = Field(None, alias="image_url")
    link: str = Field(None, alias="link")
    message: str = Field(None, alias="message")
    owner_id: str = Field(None, alias="owner_id")
    place_id: str = Field(None, alias="place_id")
    product_id: str = Field(None, alias="product_id")
    title: str = Field(None, alias="title")


class RTBDynamicPostGetCommentsParams(BaseModel):
    """Parameters for RTBDynamicPost.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: rtbdynamicpostcomments_filter_enum_param | None = Field(
        None, description="filter parameter"
    )
    live_filter: rtbdynamicpostcomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: rtbdynamicpostcomments_order_enum_param | None = Field(
        None, description="order parameter"
    )
    since: datetime | None = Field(None, description="since parameter")

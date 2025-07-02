"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields
    from .profile import ProfileFields


# Field literal type
MediaCopyrightAttributionField = Literal[
    "attribution_ig_target_id",
    "attribution_target_email_address",
    "attribution_target_id",
    "attribution_target_name",
    "attribution_type",
    "attribution_uri",
    "copyright_count",
    "creation_time",
    "creator",
    "id",
    "is_enabled",
    "link_title",
    "match_count",
    "owner",
    "status",
    "title",
]


class MediaCopyrightAttributionFields(BaseModel):
    """Pydantic model for MediaCopyrightAttribution fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attribution_ig_target_id: str = Field(None, alias="attribution_ig_target_id")
    attribution_target_email_address: str = Field(None, alias="attribution_target_email_address")
    attribution_target_id: str = Field(None, alias="attribution_target_id")
    attribution_target_name: str = Field(None, alias="attribution_target_name")
    attribution_type: str = Field(None, alias="attribution_type")
    attribution_uri: str = Field(None, alias="attribution_uri")
    copyright_count: int = Field(None, alias="copyright_count")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: ProfileFields = Field(None, alias="creator")
    id: str = Field(None, alias="id")
    is_enabled: bool = Field(None, alias="is_enabled")
    link_title: str = Field(None, alias="link_title")
    match_count: int = Field(None, alias="match_count")
    owner: PageFields = Field(None, alias="owner")
    status: str = Field(None, alias="status")
    title: str = Field(None, alias="title")

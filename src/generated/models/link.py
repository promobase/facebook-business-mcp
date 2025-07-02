"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .privacy import PrivacyFields


class linkcomments_comment_privacy_value_enum_param(str, Enum):
    """linkcomments_comment_privacy_value_enum_param enum values."""

    DECLINED_BY_ADMIN_ASSISTANT = "DECLINED_BY_ADMIN_ASSISTANT"
    DEFAULT_PRIVACY = "DEFAULT_PRIVACY"
    FRIENDS_AND_POST_OWNER = "FRIENDS_AND_POST_OWNER"
    FRIENDS_ONLY = "FRIENDS_ONLY"
    GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE = "GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE"
    OWNER_OR_COMMENTER = "OWNER_OR_COMMENTER"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    REMOVED_BY_ADMIN_ASSISTANT = "REMOVED_BY_ADMIN_ASSISTANT"
    SIDE_CONVERSATION = "SIDE_CONVERSATION"
    SIDE_CONVERSATION_AND_POST_OWNER = "SIDE_CONVERSATION_AND_POST_OWNER"
    SPOTLIGHT_TAB = "SPOTLIGHT_TAB"


# Field literal type
LinkField = Literal[
    "caption",
    "created_time",
    "description",
    "from",
    "icon",
    "id",
    "link",
    "message",
    "multi_share_optimized",
    "name",
    "privacy",
    "via",
]


class LinkFields(BaseModel):
    """Pydantic model for Link fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    caption: str = Field(None, alias="caption")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    from_: dict[str, Any] = Field(None, alias="from")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    link: str = Field(None, alias="link")
    message: str = Field(None, alias="message")
    multi_share_optimized: bool = Field(None, alias="multi_share_optimized")
    name: str = Field(None, alias="name")
    privacy: PrivacyFields = Field(None, alias="privacy")
    via: dict[str, Any] = Field(None, alias="via")


class LinkCreateCommentParams(BaseModel):
    """Parameters for Link.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    attachment_id: str | None = Field(None, description="attachment_id parameter")
    attachment_share_url: str | None = Field(None, description="attachment_share_url parameter")
    attachment_url: str | None = Field(None, description="attachment_url parameter")
    comment_privacy_value: linkcomments_comment_privacy_value_enum_param | None = Field(
        None, description="comment_privacy_value parameter"
    )
    facepile_mentioned_ids: list[str] | None = Field(
        None, description="facepile_mentioned_ids parameter"
    )
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    is_offline: bool | None = Field(None, description="is_offline parameter")
    message: str | None = Field(None, description="message parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    object_id: str | None = Field(None, description="object_id parameter")
    parent_comment_id: dict[str, Any] | None = Field(
        None, description="parent_comment_id parameter"
    )
    text: str | None = Field(None, description="text parameter")
    tracking: str | None = Field(None, description="tracking parameter")

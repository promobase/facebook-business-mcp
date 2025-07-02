"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .entityattextrange import EntityAtTextRangeFields
    from .user import UserFields


class commentcomments_filter_enum_param(str, Enum):
    """commentcomments_filter_enum_param enum values."""

    stream = "stream"
    toplevel = "toplevel"


class commentcomments_order_enum_param(str, Enum):
    """commentcomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


class commentreactions_type_enum_param(str, Enum):
    """commentreactions_type_enum_param enum values."""

    ANGRY = "ANGRY"
    CARE = "CARE"
    FIRE = "FIRE"
    HAHA = "HAHA"
    HUNDRED = "HUNDRED"
    LIKE = "LIKE"
    LOVE = "LOVE"
    NONE = "NONE"
    PRIDE = "PRIDE"
    SAD = "SAD"
    THANKFUL = "THANKFUL"
    WOW = "WOW"


class commentcomments_live_filter_enum_param(str, Enum):
    """commentcomments_live_filter_enum_param enum values."""

    filter_low_quality = "filter_low_quality"
    no_filter = "no_filter"


class commentcomments_comment_privacy_value_enum_param(str, Enum):
    """commentcomments_comment_privacy_value_enum_param enum values."""

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
CommentField = Literal[
    "admin_creator",
    "application",
    "attachment",
    "can_comment",
    "can_hide",
    "can_like",
    "can_remove",
    "can_reply_privately",
    "comment_count",
    "created_time",
    "from",
    "id",
    "is_hidden",
    "is_private",
    "like_count",
    "live_broadcast_timestamp",
    "message",
    "message_tags",
    "object",
    "parent",
    "permalink_url",
    "private_reply_conversation",
    "user_likes",
]


class CommentFields(BaseModel):
    """Pydantic model for Comment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    admin_creator: UserFields = Field(None, alias="admin_creator")
    application: ApplicationFields = Field(None, alias="application")
    attachment: dict[str, Any] = Field(None, alias="attachment")
    can_comment: bool = Field(None, alias="can_comment")
    can_hide: bool = Field(None, alias="can_hide")
    can_like: bool = Field(None, alias="can_like")
    can_remove: bool = Field(None, alias="can_remove")
    can_reply_privately: bool = Field(None, alias="can_reply_privately")
    comment_count: int = Field(None, alias="comment_count")
    created_time: datetime = Field(None, alias="created_time")
    from_: dict[str, Any] = Field(None, alias="from")
    id: str = Field(None, alias="id")
    is_hidden: bool = Field(None, alias="is_hidden")
    is_private: bool = Field(None, alias="is_private")
    like_count: int = Field(None, alias="like_count")
    live_broadcast_timestamp: int = Field(None, alias="live_broadcast_timestamp")
    message: str = Field(None, alias="message")
    message_tags: list[EntityAtTextRangeFields] = Field(None, alias="message_tags")
    object: dict[str, Any] = Field(None, alias="object")
    parent: CommentFields = Field(None, alias="parent")
    permalink_url: str = Field(None, alias="permalink_url")
    private_reply_conversation: dict[str, Any] = Field(None, alias="private_reply_conversation")
    user_likes: bool = Field(None, alias="user_likes")


class CommentGetCommentsParams(BaseModel):
    """Parameters for Comment.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    filter: commentcomments_filter_enum_param | None = Field(None, description="filter parameter")
    live_filter: commentcomments_live_filter_enum_param | None = Field(
        None, description="live_filter parameter"
    )
    order: commentcomments_order_enum_param | None = Field(None, description="order parameter")
    since: datetime | None = Field(None, description="since parameter")


class CommentCreateCommentParams(BaseModel):
    """Parameters for Comment.create_comment()."""

    model_config = ConfigDict(extra="forbid")
    attachment_id: str | None = Field(None, description="attachment_id parameter")
    attachment_share_url: str | None = Field(None, description="attachment_share_url parameter")
    attachment_url: str | None = Field(None, description="attachment_url parameter")
    comment_privacy_value: commentcomments_comment_privacy_value_enum_param | None = Field(
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


class CommentDeleteLikesParams(BaseModel):
    """Parameters for Comment.delete_likes()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class CommentCreateLikeParams(BaseModel):
    """Parameters for Comment.create_like()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    tracking: str | None = Field(None, description="tracking parameter")


class CommentGetReactionsParams(BaseModel):
    """Parameters for Comment.get_reactions()."""

    model_config = ConfigDict(extra="forbid")
    type: commentreactions_type_enum_param | None = Field(None, description="type parameter")

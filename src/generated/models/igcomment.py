"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .igcommentfromuser import IGCommentFromUserFields
    from .igmedia import IGMediaFields
    from .iguser import IGUserFields


# Field literal type
IGCommentField = Literal[
    "from",
    "hidden",
    "id",
    "legacy_instagram_comment_id",
    "like_count",
    "media",
    "parent_id",
    "text",
    "timestamp",
    "user",
    "username",
]


class IGCommentFields(BaseModel):
    """Pydantic model for IGComment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    from_: IGCommentFromUserFields = Field(None, alias="from")
    hidden: bool = Field(None, alias="hidden")
    id: str = Field(None, alias="id")
    legacy_instagram_comment_id: str = Field(None, alias="legacy_instagram_comment_id")
    like_count: int = Field(None, alias="like_count")
    media: IGMediaFields = Field(None, alias="media")
    parent_id: str = Field(None, alias="parent_id")
    text: str = Field(None, alias="text")
    timestamp: datetime = Field(None, alias="timestamp")
    user: IGUserFields = Field(None, alias="user")
    username: str = Field(None, alias="username")


class IGCommentCreateReplieParams(BaseModel):
    """Parameters for IGComment.create_replie()."""

    model_config = ConfigDict(extra="forbid")
    message: str | None = Field(None, description="message parameter")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .post import PostFields


# Field literal type
EntWithSponsorField = Literal[
    "id", "owner_linked_instagram_user_v1_id", "owner_picture", "post_id", "post_info"
]


class EntWithSponsorFields(BaseModel):
    """Pydantic model for EntWithSponsor fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    owner_linked_instagram_user_v1_id: str = Field(None, alias="owner_linked_instagram_user_v1_id")
    owner_picture: str = Field(None, alias="owner_picture")
    post_id: str = Field(None, alias="post_id")
    post_info: PostFields = Field(None, alias="post_info")

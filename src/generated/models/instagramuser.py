"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .shop import ShopFields


# Field literal type
InstagramUserField = Literal[
    "follow_count",
    "followed_by_count",
    "has_profile_picture",
    "id",
    "ig_user_id",
    "is_private",
    "is_published",
    "media_count",
    "mini_shop_storefront",
    "owner_business",
    "profile_pic",
    "username",
]


class InstagramUserFields(BaseModel):
    """Pydantic model for InstagramUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    follow_count: int = Field(None, alias="follow_count")
    followed_by_count: int = Field(None, alias="followed_by_count")
    has_profile_picture: bool = Field(None, alias="has_profile_picture")
    id: str = Field(None, alias="id")
    ig_user_id: str = Field(None, alias="ig_user_id")
    is_private: bool = Field(None, alias="is_private")
    is_published: bool = Field(None, alias="is_published")
    media_count: int = Field(None, alias="media_count")
    mini_shop_storefront: ShopFields = Field(None, alias="mini_shop_storefront")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    profile_pic: str = Field(None, alias="profile_pic")
    username: str = Field(None, alias="username")


class InstagramUserGetAuthorizedAdaccountsParams(BaseModel):
    """Parameters for InstagramUser.get_authorized_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")

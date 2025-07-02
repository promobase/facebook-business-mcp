"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profilepicturesource import ProfilePictureSourceFields


class Profile_profile_type(str, Enum):
    """Profile_profile_type enum values."""

    application = "application"
    event = "event"
    group = "group"
    page = "page"
    user = "user"


class profilepicture_type_enum_param(str, Enum):
    """profilepicture_type_enum_param enum values."""

    album = "album"
    large = "large"
    normal = "normal"
    small = "small"
    square = "square"


# Field literal type
ProfileField = Literal[
    "can_post",
    "id",
    "link",
    "name",
    "pic",
    "pic_crop",
    "pic_large",
    "pic_small",
    "pic_square",
    "profile_type",
    "username",
]


class ProfileFields(BaseModel):
    """Pydantic model for Profile fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_post: bool = Field(None, alias="can_post")
    id: str = Field(None, alias="id")
    link: str = Field(None, alias="link")
    name: str = Field(None, alias="name")
    pic: str = Field(None, alias="pic")
    pic_crop: ProfilePictureSourceFields = Field(None, alias="pic_crop")
    pic_large: str = Field(None, alias="pic_large")
    pic_small: str = Field(None, alias="pic_small")
    pic_square: str = Field(None, alias="pic_square")
    profile_type: dict[str, Any] = Field(None, alias="profile_type")
    username: str = Field(None, alias="username")


class ProfileGetPictureParams(BaseModel):
    """Parameters for Profile.get_picture()."""

    model_config = ConfigDict(extra="forbid")
    height: int | None = Field(None, description="height parameter")
    redirect: bool | None = Field(None, description="redirect parameter")
    type: profilepicture_type_enum_param | None = Field(None, description="type parameter")
    width: int | None = Field(None, description="width parameter")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
RobotField = Literal[
    "bringup_vars",
    "configurations",
    "data_center",
    "id",
    "init_pos",
    "last_pos",
    "meetup_link_hash",
    "suite",
    "target_map_image_uri",
    "target_os_image_uri",
    "target_sw_image_uri",
    "user",
]


class RobotFields(BaseModel):
    """Pydantic model for Robot fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bringup_vars: list[dict[str, str]] = Field(None, alias="bringup_vars")
    configurations: list[dict[str, str]] = Field(None, alias="configurations")
    data_center: str = Field(None, alias="data_center")
    id: str = Field(None, alias="id")
    init_pos: list[dict[str, float]] = Field(None, alias="init_pos")
    last_pos: list[dict[str, float]] = Field(None, alias="last_pos")
    meetup_link_hash: str = Field(None, alias="meetup_link_hash")
    suite: str = Field(None, alias="suite")
    target_map_image_uri: str = Field(None, alias="target_map_image_uri")
    target_os_image_uri: str = Field(None, alias="target_os_image_uri")
    target_sw_image_uri: str = Field(None, alias="target_sw_image_uri")
    user: UserFields = Field(None, alias="user")

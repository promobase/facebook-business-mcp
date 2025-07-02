"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGCommentFromUserField = Literal["id", "self_ig_scoped_id", "username"]


class IGCommentFromUserFields(BaseModel):
    """Pydantic model for IGCommentFromUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    self_ig_scoped_id: str = Field(None, alias="self_ig_scoped_id")
    username: str = Field(None, alias="username")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ThreadsUserField = Literal["threads_user_id", "threads_user_profile_pic"]


class ThreadsUserFields(BaseModel):
    """Pydantic model for ThreadsUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    threads_user_id: str = Field(None, alias="threads_user_id")
    threads_user_profile_pic: str = Field(None, alias="threads_user_profile_pic")

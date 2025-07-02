"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
AssignedUserField = Literal["business", "id", "name", "user_type"]


class AssignedUserFields(BaseModel):
    """Pydantic model for AssignedUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    user_type: str = Field(None, alias="user_type")

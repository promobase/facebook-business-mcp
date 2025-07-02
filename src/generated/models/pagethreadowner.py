"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageThreadOwnerField = Literal["thread_owner"]


class PageThreadOwnerFields(BaseModel):
    """Pydantic model for PageThreadOwner fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    thread_owner: dict[str, Any] = Field(None, alias="thread_owner")

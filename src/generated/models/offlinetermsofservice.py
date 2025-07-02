"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
OfflineTermsOfServiceField = Literal["accept_time", "id", "signed_by_user"]


class OfflineTermsOfServiceFields(BaseModel):
    """Pydantic model for OfflineTermsOfService fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    accept_time: int = Field(None, alias="accept_time")
    id: str = Field(None, alias="id")
    signed_by_user: UserFields = Field(None, alias="signed_by_user")

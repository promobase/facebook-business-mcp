"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PersonalAdsPersonaField = Literal["email", "first_name", "id", "last_name", "pending_email"]


class PersonalAdsPersonaFields(BaseModel):
    """Pydantic model for PersonalAdsPersona fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    email: str = Field(None, alias="email")
    first_name: str = Field(None, alias="first_name")
    id: str = Field(None, alias="id")
    last_name: str = Field(None, alias="last_name")
    pending_email: str = Field(None, alias="pending_email")

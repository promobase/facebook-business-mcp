"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AvatarField = Literal["id"]


class AvatarFields(BaseModel):
    """Pydantic model for Avatar fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")


class AvatarGetModelsParams(BaseModel):
    """Parameters for Avatar.get_models()."""

    model_config = ConfigDict(extra="forbid")
    client_name: str | None = Field(None, description="client_name parameter")
    client_version: str | None = Field(None, description="client_version parameter")
    config_id: str | None = Field(None, description="config_id parameter")
    force_generate: bool | None = Field(None, description="force_generate parameter")
    platform: str | None = Field(None, description="platform parameter")
    profile: str | None = Field(None, description="profile parameter")
    sdk_version: str | None = Field(None, description="sdk_version parameter")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGAccessTokenForIGOnlyAPIField = Literal["access_token", "expires_in", "token_type"]


class IGAccessTokenForIGOnlyAPIFields(BaseModel):
    """Pydantic model for IGAccessTokenForIGOnlyAPI fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    access_token: str = Field(None, alias="access_token")
    expires_in: int = Field(None, alias="expires_in")
    token_type: str = Field(None, alias="token_type")

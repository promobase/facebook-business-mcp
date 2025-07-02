"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessAgreementField = Literal["id", "request_status"]


class BusinessAgreementFields(BaseModel):
    """Pydantic model for BusinessAgreement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    request_status: str = Field(None, alias="request_status")

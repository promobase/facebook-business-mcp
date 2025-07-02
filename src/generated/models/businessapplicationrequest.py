"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields


# Field literal type
BusinessApplicationRequestField = Literal["application", "id"]


class BusinessApplicationRequestFields(BaseModel):
    """Pydantic model for BusinessApplicationRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    application: ApplicationFields = Field(None, alias="application")
    id: str = Field(None, alias="id")

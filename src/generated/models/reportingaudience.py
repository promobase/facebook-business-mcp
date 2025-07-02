"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .rawcustomaudience import RawCustomAudienceFields


# Field literal type
ReportingAudienceField = Literal[
    "custom_audiences", "custom_audiences_url_param_name", "custom_audiences_url_param_type"
]


class ReportingAudienceFields(BaseModel):
    """Pydantic model for ReportingAudience fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    custom_audiences: list[RawCustomAudienceFields] = Field(None, alias="custom_audiences")
    custom_audiences_url_param_name: str = Field(None, alias="custom_audiences_url_param_name")
    custom_audiences_url_param_type: str = Field(None, alias="custom_audiences_url_param_type")

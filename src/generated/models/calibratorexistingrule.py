"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CalibratorExistingRuleField = Literal[
    "7d_volume",
    "creation_source",
    "creation_time",
    "creator",
    "event_type",
    "id",
    "rule",
    "rule_type",
    "sample_urls",
    "status",
    "transforms",
]


class CalibratorExistingRuleFields(BaseModel):
    """Pydantic model for CalibratorExistingRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field_7d_volume: int = Field(None, alias="7d_volume")
    creation_source: str = Field(None, alias="creation_source")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: str = Field(None, alias="creator")
    event_type: str = Field(None, alias="event_type")
    id: str = Field(None, alias="id")
    rule: str = Field(None, alias="rule")
    rule_type: str = Field(None, alias="rule_type")
    sample_urls: list[str] = Field(None, alias="sample_urls")
    status: str = Field(None, alias="status")
    transforms: list[str] = Field(None, alias="transforms")

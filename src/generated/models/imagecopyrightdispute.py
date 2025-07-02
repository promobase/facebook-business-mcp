"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ImageCopyrightDisputeField = Literal[
    "appeal_form_data",
    "dispute_form_data",
    "expiration_time",
    "id",
    "match_id",
    "status",
    "time_appealed",
    "time_created",
    "time_updated",
]


class ImageCopyrightDisputeFields(BaseModel):
    """Pydantic model for ImageCopyrightDispute fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    appeal_form_data: str = Field(None, alias="appeal_form_data")
    dispute_form_data: str = Field(None, alias="dispute_form_data")
    expiration_time: datetime = Field(None, alias="expiration_time")
    id: str = Field(None, alias="id")
    match_id: str = Field(None, alias="match_id")
    status: str = Field(None, alias="status")
    time_appealed: datetime = Field(None, alias="time_appealed")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")

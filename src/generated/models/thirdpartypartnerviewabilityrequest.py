"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ThirdPartyPartnerViewabilityRequest_metric(str, Enum):
    """ThirdPartyPartnerViewabilityRequest_metric enum values."""

    DISPLAY_EVENT = "DISPLAY_EVENT"
    IMPRESSION = "IMPRESSION"
    VIDEO_EVENT = "VIDEO_EVENT"


class ThirdPartyPartnerViewabilityRequest_platform(str, Enum):
    """ThirdPartyPartnerViewabilityRequest_platform enum values."""

    AUDIENCE_NETWORK = "AUDIENCE_NETWORK"
    FACEBOOK = "FACEBOOK"
    INSTAGRAM = "INSTAGRAM"


class ThirdPartyPartnerViewabilityRequest_status(str, Enum):
    """ThirdPartyPartnerViewabilityRequest_status enum values."""

    CREATED = "CREATED"
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"
    SCHEDULED = "SCHEDULED"
    SUCCESS = "SUCCESS"


# Field literal type
ThirdPartyPartnerViewabilityRequestField = Literal[
    "created_time",
    "description",
    "ds",
    "hour",
    "id",
    "metric",
    "modified_time",
    "owner_instance_id",
    "platform",
    "status",
    "total_file_count",
]


class ThirdPartyPartnerViewabilityRequestFields(BaseModel):
    """Pydantic model for ThirdPartyPartnerViewabilityRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    ds: str = Field(None, alias="ds")
    hour: datetime = Field(None, alias="hour")
    id: str = Field(None, alias="id")
    metric: dict[str, Any] = Field(None, alias="metric")
    modified_time: datetime = Field(None, alias="modified_time")
    owner_instance_id: str = Field(None, alias="owner_instance_id")
    platform: dict[str, Any] = Field(None, alias="platform")
    status: dict[str, Any] = Field(None, alias="status")
    total_file_count: int = Field(None, alias="total_file_count")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PrivateLiftStudyInstanceField = Literal[
    "breakdown_key",
    "created_time",
    "feature_list",
    "id",
    "issuer_certificate",
    "latest_status_update_time",
    "run_id",
    "server_hostnames",
    "server_ips",
    "status",
    "tier",
]


class PrivateLiftStudyInstanceFields(BaseModel):
    """Pydantic model for PrivateLiftStudyInstance fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    breakdown_key: str = Field(None, alias="breakdown_key")
    created_time: datetime = Field(None, alias="created_time")
    feature_list: list[str] = Field(None, alias="feature_list")
    id: str = Field(None, alias="id")
    issuer_certificate: str = Field(None, alias="issuer_certificate")
    latest_status_update_time: datetime = Field(None, alias="latest_status_update_time")
    run_id: str = Field(None, alias="run_id")
    server_hostnames: list[str] = Field(None, alias="server_hostnames")
    server_ips: list[str] = Field(None, alias="server_ips")
    status: str = Field(None, alias="status")
    tier: str = Field(None, alias="tier")

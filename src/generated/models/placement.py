"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PlacementField = Literal[
    "audience_network_positions",
    "device_platforms",
    "effective_audience_network_positions",
    "effective_device_platforms",
    "effective_facebook_positions",
    "effective_instagram_positions",
    "effective_messenger_positions",
    "effective_oculus_positions",
    "effective_publisher_platforms",
    "effective_threads_positions",
    "effective_whatsapp_positions",
    "facebook_positions",
    "instagram_positions",
    "messenger_positions",
    "oculus_positions",
    "publisher_platforms",
    "threads_positions",
    "whatsapp_positions",
]


class PlacementFields(BaseModel):
    """Pydantic model for Placement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_network_positions: list[str] = Field(None, alias="audience_network_positions")
    device_platforms: list[dict[str, Any]] = Field(None, alias="device_platforms")
    effective_audience_network_positions: list[str] = Field(
        None, alias="effective_audience_network_positions"
    )
    effective_device_platforms: list[dict[str, Any]] = Field(
        None, alias="effective_device_platforms"
    )
    effective_facebook_positions: list[str] = Field(None, alias="effective_facebook_positions")
    effective_instagram_positions: list[str] = Field(None, alias="effective_instagram_positions")
    effective_messenger_positions: list[str] = Field(None, alias="effective_messenger_positions")
    effective_oculus_positions: list[str] = Field(None, alias="effective_oculus_positions")
    effective_publisher_platforms: list[str] = Field(None, alias="effective_publisher_platforms")
    effective_threads_positions: list[str] = Field(None, alias="effective_threads_positions")
    effective_whatsapp_positions: list[str] = Field(None, alias="effective_whatsapp_positions")
    facebook_positions: list[str] = Field(None, alias="facebook_positions")
    instagram_positions: list[str] = Field(None, alias="instagram_positions")
    messenger_positions: list[str] = Field(None, alias="messenger_positions")
    oculus_positions: list[str] = Field(None, alias="oculus_positions")
    publisher_platforms: list[str] = Field(None, alias="publisher_platforms")
    threads_positions: list[str] = Field(None, alias="threads_positions")
    whatsapp_positions: list[str] = Field(None, alias="whatsapp_positions")

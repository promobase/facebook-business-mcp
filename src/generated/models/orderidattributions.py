"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OrderIDAttributionsField = Literal[
    "app_id",
    "attribution_type",
    "attributions",
    "conversion_device",
    "dataset_id",
    "holdout_status",
    "order_id",
    "order_timestamp",
    "pixel_id",
]


class OrderIDAttributionsFields(BaseModel):
    """Pydantic model for OrderIDAttributions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: str = Field(None, alias="app_id")
    attribution_type: str = Field(None, alias="attribution_type")
    attributions: list[dict[str, Any]] = Field(None, alias="attributions")
    conversion_device: str = Field(None, alias="conversion_device")
    dataset_id: str = Field(None, alias="dataset_id")
    holdout_status: list[dict[str, Any]] = Field(None, alias="holdout_status")
    order_id: str = Field(None, alias="order_id")
    order_timestamp: datetime = Field(None, alias="order_timestamp")
    pixel_id: str = Field(None, alias="pixel_id")

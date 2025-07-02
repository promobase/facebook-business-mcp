"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
EventTicketTierField = Literal[
    "currency",
    "description",
    "end_sales_time",
    "end_show_time",
    "fee_settings",
    "id",
    "maximum_quantity",
    "metadata",
    "minimum_quantity",
    "name",
    "price",
    "priority",
    "retailer_id",
    "seating_map_image_url",
    "start_sales_time",
    "start_show_time",
    "status",
    "total_quantity",
]


class EventTicketTierFields(BaseModel):
    """Pydantic model for EventTicketTier fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    currency: str = Field(None, alias="currency")
    description: str = Field(None, alias="description")
    end_sales_time: datetime = Field(None, alias="end_sales_time")
    end_show_time: datetime = Field(None, alias="end_show_time")
    fee_settings: str = Field(None, alias="fee_settings")
    id: str = Field(None, alias="id")
    maximum_quantity: int = Field(None, alias="maximum_quantity")
    metadata: str = Field(None, alias="metadata")
    minimum_quantity: int = Field(None, alias="minimum_quantity")
    name: str = Field(None, alias="name")
    price: int = Field(None, alias="price")
    priority: int = Field(None, alias="priority")
    retailer_id: str = Field(None, alias="retailer_id")
    seating_map_image_url: str = Field(None, alias="seating_map_image_url")
    start_sales_time: datetime = Field(None, alias="start_sales_time")
    start_show_time: datetime = Field(None, alias="start_show_time")
    status: str = Field(None, alias="status")
    total_quantity: int = Field(None, alias="total_quantity")

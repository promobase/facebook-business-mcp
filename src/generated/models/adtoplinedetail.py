"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdToplineDetailField = Literal[
    "active_status",
    "ad_account_id",
    "flight_end_date",
    "flight_start_date",
    "id",
    "io_number",
    "line_number",
    "price",
    "quantity",
    "sf_detail_line_id",
    "subline_id",
    "targets",
    "time_created",
    "time_updated",
]


class AdToplineDetailFields(BaseModel):
    """Pydantic model for AdToplineDetail fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    active_status: int = Field(None, alias="active_status")
    ad_account_id: str = Field(None, alias="ad_account_id")
    flight_end_date: datetime = Field(None, alias="flight_end_date")
    flight_start_date: datetime = Field(None, alias="flight_start_date")
    id: str = Field(None, alias="id")
    io_number: int = Field(None, alias="io_number")
    line_number: int = Field(None, alias="line_number")
    price: float = Field(None, alias="price")
    quantity: float = Field(None, alias="quantity")
    sf_detail_line_id: str = Field(None, alias="sf_detail_line_id")
    subline_id: str = Field(None, alias="subline_id")
    targets: str = Field(None, alias="targets")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")

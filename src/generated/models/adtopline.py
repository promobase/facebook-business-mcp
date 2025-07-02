"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdToplineField = Literal[
    "account_id",
    "client_approval_date",
    "created_by",
    "created_date",
    "description",
    "flight_end_date",
    "flight_start_date",
    "func_cap_amount",
    "func_cap_amount_with_offset",
    "func_line_amount",
    "func_line_amount_with_offset",
    "func_price",
    "func_price_with_offset",
    "gender",
    "id",
    "impressions",
    "io_number",
    "is_bonus_line",
    "keywords",
    "last_updated_by",
    "last_updated_date",
    "line_number",
    "line_position",
    "line_type",
    "location",
    "max_age",
    "max_budget",
    "min_age",
    "price_per_trp",
    "product_type",
    "rev_assurance_approval_date",
    "targets",
    "trp_updated_time",
    "trp_value",
    "uom",
]


class AdToplineFields(BaseModel):
    """Pydantic model for AdTopline fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    client_approval_date: datetime = Field(None, alias="client_approval_date")
    created_by: str = Field(None, alias="created_by")
    created_date: datetime = Field(None, alias="created_date")
    description: str = Field(None, alias="description")
    flight_end_date: datetime = Field(None, alias="flight_end_date")
    flight_start_date: datetime = Field(None, alias="flight_start_date")
    func_cap_amount: str = Field(None, alias="func_cap_amount")
    func_cap_amount_with_offset: str = Field(None, alias="func_cap_amount_with_offset")
    func_line_amount: str = Field(None, alias="func_line_amount")
    func_line_amount_with_offset: str = Field(None, alias="func_line_amount_with_offset")
    func_price: str = Field(None, alias="func_price")
    func_price_with_offset: str = Field(None, alias="func_price_with_offset")
    gender: str = Field(None, alias="gender")
    id: str = Field(None, alias="id")
    impressions: int = Field(None, alias="impressions")
    io_number: int = Field(None, alias="io_number")
    is_bonus_line: int = Field(None, alias="is_bonus_line")
    keywords: str = Field(None, alias="keywords")
    last_updated_by: str = Field(None, alias="last_updated_by")
    last_updated_date: datetime = Field(None, alias="last_updated_date")
    line_number: int = Field(None, alias="line_number")
    line_position: int = Field(None, alias="line_position")
    line_type: str = Field(None, alias="line_type")
    location: str = Field(None, alias="location")
    max_age: str = Field(None, alias="max_age")
    max_budget: str = Field(None, alias="max_budget")
    min_age: str = Field(None, alias="min_age")
    price_per_trp: str = Field(None, alias="price_per_trp")
    product_type: str = Field(None, alias="product_type")
    rev_assurance_approval_date: datetime = Field(None, alias="rev_assurance_approval_date")
    targets: str = Field(None, alias="targets")
    trp_updated_time: int = Field(None, alias="trp_updated_time")
    trp_value: str = Field(None, alias="trp_value")
    uom: str = Field(None, alias="uom")

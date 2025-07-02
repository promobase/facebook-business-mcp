"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BrandRequestField = Literal[
    "ad_countries",
    "additional_contacts",
    "approval_level",
    "cells",
    "countries",
    "deny_reason",
    "end_time",
    "estimated_reach",
    "id",
    "is_multicell",
    "locale",
    "max_age",
    "min_age",
    "questions",
    "region",
    "request_status",
    "review_date",
    "start_time",
    "status",
    "submit_date",
    "total_budget",
]


class BrandRequestFields(BaseModel):
    """Pydantic model for BrandRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_countries: list[str] = Field(None, alias="ad_countries")
    additional_contacts: list[str] = Field(None, alias="additional_contacts")
    approval_level: int = Field(None, alias="approval_level")
    cells: list[dict[str, Any]] = Field(None, alias="cells")
    countries: list[str] = Field(None, alias="countries")
    deny_reason: str = Field(None, alias="deny_reason")
    end_time: datetime = Field(None, alias="end_time")
    estimated_reach: int = Field(None, alias="estimated_reach")
    id: str = Field(None, alias="id")
    is_multicell: bool = Field(None, alias="is_multicell")
    locale: str = Field(None, alias="locale")
    max_age: int = Field(None, alias="max_age")
    min_age: int = Field(None, alias="min_age")
    questions: list[dict[str, Any]] = Field(None, alias="questions")
    region: str = Field(None, alias="region")
    request_status: str = Field(None, alias="request_status")
    review_date: datetime = Field(None, alias="review_date")
    start_time: datetime = Field(None, alias="start_time")
    status: str = Field(None, alias="status")
    submit_date: datetime = Field(None, alias="submit_date")
    total_budget: int = Field(None, alias="total_budget")

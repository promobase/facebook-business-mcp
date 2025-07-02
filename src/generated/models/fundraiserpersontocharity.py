"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
FundraiserPersonToCharityField = Literal[
    "amount_raised",
    "charity_id",
    "currency",
    "description",
    "donations_count",
    "donors_count",
    "end_time",
    "external_amount_raised",
    "external_donations_count",
    "external_donors_count",
    "external_event_name",
    "external_event_start_time",
    "external_event_uri",
    "external_fundraiser_uri",
    "external_id",
    "goal_amount",
    "id",
    "internal_amount_raised",
    "internal_donations_count",
    "internal_donors_count",
    "name",
    "uri",
]


class FundraiserPersonToCharityFields(BaseModel):
    """Pydantic model for FundraiserPersonToCharity fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount_raised: int = Field(None, alias="amount_raised")
    charity_id: str = Field(None, alias="charity_id")
    currency: str = Field(None, alias="currency")
    description: str = Field(None, alias="description")
    donations_count: int = Field(None, alias="donations_count")
    donors_count: int = Field(None, alias="donors_count")
    end_time: datetime = Field(None, alias="end_time")
    external_amount_raised: int = Field(None, alias="external_amount_raised")
    external_donations_count: int = Field(None, alias="external_donations_count")
    external_donors_count: int = Field(None, alias="external_donors_count")
    external_event_name: str = Field(None, alias="external_event_name")
    external_event_start_time: datetime = Field(None, alias="external_event_start_time")
    external_event_uri: str = Field(None, alias="external_event_uri")
    external_fundraiser_uri: str = Field(None, alias="external_fundraiser_uri")
    external_id: str = Field(None, alias="external_id")
    goal_amount: int = Field(None, alias="goal_amount")
    id: str = Field(None, alias="id")
    internal_amount_raised: int = Field(None, alias="internal_amount_raised")
    internal_donations_count: int = Field(None, alias="internal_donations_count")
    internal_donors_count: int = Field(None, alias="internal_donors_count")
    name: str = Field(None, alias="name")
    uri: str = Field(None, alias="uri")


class FundraiserPersonToCharityCreateExternalDonationParams(BaseModel):
    """Parameters for FundraiserPersonToCharity.create_external_donation()."""

    model_config = ConfigDict(extra="forbid")
    amount_received: int | None = Field(None, description="amount_received parameter")
    currency: str | None = Field(None, description="currency parameter")
    donation_id_hash: str | None = Field(None, description="donation_id_hash parameter")
    donation_time: int | None = Field(None, description="donation_time parameter")
    donor_id_hash: str | None = Field(None, description="donor_id_hash parameter")

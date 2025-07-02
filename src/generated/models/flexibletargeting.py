"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .idname import IDNameFields


# Field literal type
FlexibleTargetingField = Literal[
    "behaviors",
    "college_years",
    "connections",
    "custom_audiences",
    "education_majors",
    "education_schools",
    "education_statuses",
    "ethnic_affinity",
    "family_statuses",
    "friends_of_connections",
    "generation",
    "home_ownership",
    "home_type",
    "home_value",
    "household_composition",
    "income",
    "industries",
    "interested_in",
    "interests",
    "life_events",
    "moms",
    "net_worth",
    "office_type",
    "politics",
    "relationship_statuses",
    "user_adclusters",
    "work_employers",
    "work_positions",
]


class FlexibleTargetingFields(BaseModel):
    """Pydantic model for FlexibleTargeting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    behaviors: list[IDNameFields] = Field(None, alias="behaviors")
    college_years: list[int] = Field(None, alias="college_years")
    connections: list[IDNameFields] = Field(None, alias="connections")
    custom_audiences: list[IDNameFields] = Field(None, alias="custom_audiences")
    education_majors: list[IDNameFields] = Field(None, alias="education_majors")
    education_schools: list[IDNameFields] = Field(None, alias="education_schools")
    education_statuses: list[int] = Field(None, alias="education_statuses")
    ethnic_affinity: list[IDNameFields] = Field(None, alias="ethnic_affinity")
    family_statuses: list[IDNameFields] = Field(None, alias="family_statuses")
    friends_of_connections: list[IDNameFields] = Field(None, alias="friends_of_connections")
    generation: list[IDNameFields] = Field(None, alias="generation")
    home_ownership: list[IDNameFields] = Field(None, alias="home_ownership")
    home_type: list[IDNameFields] = Field(None, alias="home_type")
    home_value: list[IDNameFields] = Field(None, alias="home_value")
    household_composition: list[IDNameFields] = Field(None, alias="household_composition")
    income: list[IDNameFields] = Field(None, alias="income")
    industries: list[IDNameFields] = Field(None, alias="industries")
    interested_in: list[int] = Field(None, alias="interested_in")
    interests: list[IDNameFields] = Field(None, alias="interests")
    life_events: list[IDNameFields] = Field(None, alias="life_events")
    moms: list[IDNameFields] = Field(None, alias="moms")
    net_worth: list[IDNameFields] = Field(None, alias="net_worth")
    office_type: list[IDNameFields] = Field(None, alias="office_type")
    politics: list[IDNameFields] = Field(None, alias="politics")
    relationship_statuses: list[int] = Field(None, alias="relationship_statuses")
    user_adclusters: list[IDNameFields] = Field(None, alias="user_adclusters")
    work_employers: list[IDNameFields] = Field(None, alias="work_employers")
    work_positions: list[IDNameFields] = Field(None, alias="work_positions")

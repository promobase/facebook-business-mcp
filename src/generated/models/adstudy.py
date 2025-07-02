"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .user import UserFields


# Field literal type
AdStudyField = Literal[
    "business",
    "canceled_time",
    "client_business",
    "cooldown_start_time",
    "created_by",
    "created_time",
    "description",
    "end_time",
    "id",
    "measurement_contact",
    "name",
    "observation_end_time",
    "results_first_available_date",
    "sales_contact",
    "start_time",
    "type",
    "updated_by",
    "updated_time",
]


class AdStudyFields(BaseModel):
    """Pydantic model for AdStudy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    canceled_time: datetime = Field(None, alias="canceled_time")
    client_business: BusinessFields = Field(None, alias="client_business")
    cooldown_start_time: datetime = Field(None, alias="cooldown_start_time")
    created_by: UserFields = Field(None, alias="created_by")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    end_time: datetime = Field(None, alias="end_time")
    id: str = Field(None, alias="id")
    measurement_contact: UserFields = Field(None, alias="measurement_contact")
    name: str = Field(None, alias="name")
    observation_end_time: datetime = Field(None, alias="observation_end_time")
    results_first_available_date: str = Field(None, alias="results_first_available_date")
    sales_contact: UserFields = Field(None, alias="sales_contact")
    start_time: datetime = Field(None, alias="start_time")
    type: str = Field(None, alias="type")
    updated_by: UserFields = Field(None, alias="updated_by")
    updated_time: datetime = Field(None, alias="updated_time")


class AdStudyCreateCheckpointParams(BaseModel):
    """Parameters for AdStudy.create_checkpoint()."""

    model_config = ConfigDict(extra="forbid")
    checkpoint_data: str | None = Field(None, description="checkpoint_data parameter")
    checkpoint_name: str | None = Field(None, description="checkpoint_name parameter")
    component: str | None = Field(None, description="component parameter")
    instance_id: str | None = Field(None, description="instance_id parameter")
    run_id: str | None = Field(None, description="run_id parameter")


class AdStudyCreateInstanceParams(BaseModel):
    """Parameters for AdStudy.create_instance()."""

    model_config = ConfigDict(extra="forbid")
    breakdown_key: dict[str, Any] | None = Field(None, description="breakdown_key parameter")
    run_id: str | None = Field(None, description="run_id parameter")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .user import UserFields


# Field literal type
AdProposalField = Literal[
    "ad_proposal_type_name",
    "adaccount",
    "creation_time",
    "creator",
    "delivery_interface",
    "expiration_time",
    "has_conflict",
    "id",
    "kpi_metric",
    "message",
    "name",
    "proposal_dts_template",
    "proposal_template_name",
    "recommendation",
    "review_time",
    "reviewed_by",
    "send_time",
    "status",
    "use_testing",
]


class AdProposalFields(BaseModel):
    """Pydantic model for AdProposal fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_proposal_type_name: str = Field(None, alias="ad_proposal_type_name")
    adaccount: AdAccountFields = Field(None, alias="adaccount")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: UserFields = Field(None, alias="creator")
    delivery_interface: str = Field(None, alias="delivery_interface")
    expiration_time: datetime = Field(None, alias="expiration_time")
    has_conflict: bool = Field(None, alias="has_conflict")
    id: str = Field(None, alias="id")
    kpi_metric: str = Field(None, alias="kpi_metric")
    message: str = Field(None, alias="message")
    name: str = Field(None, alias="name")
    proposal_dts_template: str = Field(None, alias="proposal_dts_template")
    proposal_template_name: str = Field(None, alias="proposal_template_name")
    recommendation: str = Field(None, alias="recommendation")
    review_time: datetime = Field(None, alias="review_time")
    reviewed_by: UserFields = Field(None, alias="reviewed_by")
    send_time: datetime = Field(None, alias="send_time")
    status: str = Field(None, alias="status")
    use_testing: bool = Field(None, alias="use_testing")

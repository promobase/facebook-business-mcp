"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class WhatsAppBusinessPartnerClientVerificationSubmission_verification_status(str, Enum):
    """WhatsAppBusinessPartnerClientVerificationSubmission_verification_status enum values."""

    APPROVED = "APPROVED"
    DISCARDED = "DISCARDED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    REVOKED = "REVOKED"


# Field literal type
WhatsAppBusinessPartnerClientVerificationSubmissionField = Literal[
    "client_business_id",
    "id",
    "rejection_reasons",
    "submitted_info",
    "submitted_time",
    "update_time",
    "verification_status",
]


class WhatsAppBusinessPartnerClientVerificationSubmissionFields(BaseModel):
    """Pydantic model for WhatsAppBusinessPartnerClientVerificationSubmission fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    client_business_id: str = Field(None, alias="client_business_id")
    id: str = Field(None, alias="id")
    rejection_reasons: list[dict[str, Any]] = Field(None, alias="rejection_reasons")
    submitted_info: dict[str, Any] = Field(None, alias="submitted_info")
    submitted_time: datetime = Field(None, alias="submitted_time")
    update_time: datetime = Field(None, alias="update_time")
    verification_status: dict[str, Any] = Field(None, alias="verification_status")

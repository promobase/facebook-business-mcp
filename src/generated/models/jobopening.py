"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields
    from .photo import PhotoFields
    from .post import PostFields


class JobOpening_job_status(str, Enum):
    """JobOpening_job_status enum values."""

    CLOSED = "CLOSED"
    DRAFT = "DRAFT"
    OPEN = "OPEN"
    PROVISIONAL = "PROVISIONAL"


class JobOpening_platform_review_status(str, Enum):
    """JobOpening_platform_review_status enum values."""

    APPROVED = "APPROVED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"


class JobOpening_type(str, Enum):
    """JobOpening_type enum values."""

    CONTRACT = "CONTRACT"
    FULL_TIME = "FULL_TIME"
    INTERNSHIP = "INTERNSHIP"
    PART_TIME = "PART_TIME"
    VOLUNTEER = "VOLUNTEER"


# Field literal type
JobOpeningField = Literal[
    "address",
    "application_callback_url",
    "created_time",
    "description",
    "errors",
    "external_company_facebook_url",
    "external_company_full_address",
    "external_company_id",
    "external_company_name",
    "external_id",
    "id",
    "job_status",
    "latitude",
    "longitude",
    "offsite_application_url",
    "page",
    "photo",
    "platform_review_status",
    "post",
    "remote_type",
    "review_rejection_reasons",
    "title",
    "type",
]


class JobOpeningFields(BaseModel):
    """Pydantic model for JobOpening fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    address: str = Field(None, alias="address")
    application_callback_url: str = Field(None, alias="application_callback_url")
    created_time: datetime = Field(None, alias="created_time")
    description: str = Field(None, alias="description")
    errors: list[str] = Field(None, alias="errors")
    external_company_facebook_url: str = Field(None, alias="external_company_facebook_url")
    external_company_full_address: str = Field(None, alias="external_company_full_address")
    external_company_id: str = Field(None, alias="external_company_id")
    external_company_name: str = Field(None, alias="external_company_name")
    external_id: str = Field(None, alias="external_id")
    id: str = Field(None, alias="id")
    job_status: dict[str, Any] = Field(None, alias="job_status")
    latitude: float = Field(None, alias="latitude")
    longitude: float = Field(None, alias="longitude")
    offsite_application_url: str = Field(None, alias="offsite_application_url")
    page: PageFields = Field(None, alias="page")
    photo: PhotoFields = Field(None, alias="photo")
    platform_review_status: dict[str, Any] = Field(None, alias="platform_review_status")
    post: PostFields = Field(None, alias="post")
    remote_type: str = Field(None, alias="remote_type")
    review_rejection_reasons: list[dict[str, Any]] = Field(None, alias="review_rejection_reasons")
    title: str = Field(None, alias="title")
    type: dict[str, Any] = Field(None, alias="type")

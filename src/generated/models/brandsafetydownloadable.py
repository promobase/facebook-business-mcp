"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BrandSafetyDownloadableField = Literal[
    "account_context_id",
    "async_job_percent_complete",
    "async_job_status",
    "file_name",
    "id",
    "request_surface",
    "url",
]


class BrandSafetyDownloadableFields(BaseModel):
    """Pydantic model for BrandSafetyDownloadable fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_context_id: str = Field(None, alias="account_context_id")
    async_job_percent_complete: int = Field(None, alias="async_job_percent_complete")
    async_job_status: str = Field(None, alias="async_job_status")
    file_name: str = Field(None, alias="file_name")
    id: str = Field(None, alias="id")
    request_surface: str = Field(None, alias="request_surface")
    url: str = Field(None, alias="url")

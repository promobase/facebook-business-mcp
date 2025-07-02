"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adasyncrequestset import AdAsyncRequestSetFields


# Field literal type
AdDraftField = Literal[
    "account_id",
    "api_version",
    "async_request_set",
    "author_id",
    "created_by",
    "draft_version",
    "id",
    "is_active",
    "name",
    "ownership_type",
    "publish_status",
    "state",
    "summary",
    "time_created",
    "time_updated",
]


class AdDraftFields(BaseModel):
    """Pydantic model for AdDraft fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    api_version: str = Field(None, alias="api_version")
    async_request_set: AdAsyncRequestSetFields = Field(None, alias="async_request_set")
    author_id: str = Field(None, alias="author_id")
    created_by: str = Field(None, alias="created_by")
    draft_version: str = Field(None, alias="draft_version")
    id: str = Field(None, alias="id")
    is_active: bool = Field(None, alias="is_active")
    name: str = Field(None, alias="name")
    ownership_type: str = Field(None, alias="ownership_type")
    publish_status: dict[str, Any] = Field(None, alias="publish_status")
    state: str = Field(None, alias="state")
    summary: str = Field(None, alias="summary")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")

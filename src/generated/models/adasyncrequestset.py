"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adasyncrequestsetnotificationresult import AdAsyncRequestSetNotificationResultFields


class AdAsyncRequestSet_notification_mode(str, Enum):
    """AdAsyncRequestSet_notification_mode enum values."""

    OFF = "OFF"
    ON_COMPLETE = "ON_COMPLETE"


class adasyncrequestsetrequests_statuses_enum_param(str, Enum):
    """adasyncrequestsetrequests_statuses_enum_param enum values."""

    CANCELED = "CANCELED"
    CANCELED_DEPENDENCY = "CANCELED_DEPENDENCY"
    ERROR = "ERROR"
    ERROR_CONFLICTS = "ERROR_CONFLICTS"
    ERROR_DEPENDENCY = "ERROR_DEPENDENCY"
    INITIAL = "INITIAL"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING_DEPENDENCY = "PENDING_DEPENDENCY"
    PROCESS_BY_AD_ASYNC_ENGINE = "PROCESS_BY_AD_ASYNC_ENGINE"
    PROCESS_BY_EVENT_PROCESSOR = "PROCESS_BY_EVENT_PROCESSOR"
    SUCCESS = "SUCCESS"
    USER_CANCELED = "USER_CANCELED"
    USER_CANCELED_DEPENDENCY = "USER_CANCELED_DEPENDENCY"


# Field literal type
AdAsyncRequestSetField = Literal[
    "canceled_count",
    "created_time",
    "error_count",
    "id",
    "in_progress_count",
    "initial_count",
    "is_completed",
    "name",
    "notification_mode",
    "notification_result",
    "notification_status",
    "notification_uri",
    "owner_id",
    "success_count",
    "total_count",
    "updated_time",
]


class AdAsyncRequestSetFields(BaseModel):
    """Pydantic model for AdAsyncRequestSet fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    canceled_count: int = Field(None, alias="canceled_count")
    created_time: datetime = Field(None, alias="created_time")
    error_count: int = Field(None, alias="error_count")
    id: str = Field(None, alias="id")
    in_progress_count: int = Field(None, alias="in_progress_count")
    initial_count: int = Field(None, alias="initial_count")
    is_completed: bool = Field(None, alias="is_completed")
    name: str = Field(None, alias="name")
    notification_mode: dict[str, Any] = Field(None, alias="notification_mode")
    notification_result: AdAsyncRequestSetNotificationResultFields = Field(
        None, alias="notification_result"
    )
    notification_status: str = Field(None, alias="notification_status")
    notification_uri: str = Field(None, alias="notification_uri")
    owner_id: str = Field(None, alias="owner_id")
    success_count: int = Field(None, alias="success_count")
    total_count: int = Field(None, alias="total_count")
    updated_time: datetime = Field(None, alias="updated_time")


class AdAsyncRequestSetGetRequestsParams(BaseModel):
    """Parameters for AdAsyncRequestSet.get_requests()."""

    model_config = ConfigDict(extra="forbid")
    statuses: list[adasyncrequestsetrequests_statuses_enum_param] | None = Field(
        None, description="statuses parameter"
    )

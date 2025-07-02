"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .page import PageFields
    from .user import UserFields


# Field literal type
AsyncSessionField = Literal[
    "app",
    "complete_time",
    "error_code",
    "exception",
    "id",
    "method",
    "name",
    "page",
    "percent_completed",
    "platform_version",
    "result",
    "start_time",
    "status",
    "uri",
    "user",
]


class AsyncSessionFields(BaseModel):
    """Pydantic model for AsyncSession fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app: ApplicationFields = Field(None, alias="app")
    complete_time: datetime = Field(None, alias="complete_time")
    error_code: int = Field(None, alias="error_code")
    exception: str = Field(None, alias="exception")
    id: str = Field(None, alias="id")
    method: str = Field(None, alias="method")
    name: str = Field(None, alias="name")
    page: PageFields = Field(None, alias="page")
    percent_completed: int = Field(None, alias="percent_completed")
    platform_version: str = Field(None, alias="platform_version")
    result: str = Field(None, alias="result")
    start_time: datetime = Field(None, alias="start_time")
    status: str = Field(None, alias="status")
    uri: str = Field(None, alias="uri")
    user: UserFields = Field(None, alias="user")

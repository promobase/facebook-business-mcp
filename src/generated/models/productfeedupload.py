"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productfeeduploaderrorreport import ProductFeedUploadErrorReportFields


class ProductFeedUpload_input_method(str, Enum):
    """ProductFeedUpload_input_method enum values."""

    GOOGLE_SHEETS_FETCH = "Google Sheets Fetch"
    MANUAL_UPLOAD = "Manual Upload"
    REUPLOAD_LAST_FILE = "Reupload Last File"
    SERVER_FETCH = "Server Fetch"
    USER_INITIATED_SERVER_FETCH = "User initiated server fetch"


class productfeeduploaderrors_error_priority_enum_param(str, Enum):
    """productfeeduploaderrors_error_priority_enum_param enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


# Field literal type
ProductFeedUploadField = Literal[
    "end_time",
    "error_count",
    "error_report",
    "filename",
    "id",
    "input_method",
    "num_deleted_items",
    "num_detected_items",
    "num_invalid_items",
    "num_persisted_items",
    "start_time",
    "url",
    "warning_count",
]


class ProductFeedUploadFields(BaseModel):
    """Pydantic model for ProductFeedUpload fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_time: datetime = Field(None, alias="end_time")
    error_count: int = Field(None, alias="error_count")
    error_report: ProductFeedUploadErrorReportFields = Field(None, alias="error_report")
    filename: str = Field(None, alias="filename")
    id: str = Field(None, alias="id")
    input_method: dict[str, Any] = Field(None, alias="input_method")
    num_deleted_items: int = Field(None, alias="num_deleted_items")
    num_detected_items: int = Field(None, alias="num_detected_items")
    num_invalid_items: int = Field(None, alias="num_invalid_items")
    num_persisted_items: int = Field(None, alias="num_persisted_items")
    start_time: datetime = Field(None, alias="start_time")
    url: str = Field(None, alias="url")
    warning_count: int = Field(None, alias="warning_count")


class ProductFeedUploadGetErrorsParams(BaseModel):
    """Parameters for ProductFeedUpload.get_errors()."""

    model_config = ConfigDict(extra="forbid")
    error_priority: productfeeduploaderrors_error_priority_enum_param | None = Field(
        None, description="error_priority parameter"
    )

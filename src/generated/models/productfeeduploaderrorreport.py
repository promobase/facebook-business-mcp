"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductFeedUploadErrorReportField = Literal["file_handle", "report_status"]


class ProductFeedUploadErrorReportFields(BaseModel):
    """Pydantic model for ProductFeedUploadErrorReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    file_handle: str = Field(None, alias="file_handle")
    report_status: str = Field(None, alias="report_status")

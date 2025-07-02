"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
RightsManagerDataExportField = Literal[
    "download_uri",
    "export_scope",
    "id",
    "name",
    "record_type",
    "time_range_end",
    "time_range_start",
]


class RightsManagerDataExportFields(BaseModel):
    """Pydantic model for RightsManagerDataExport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    download_uri: str = Field(None, alias="download_uri")
    export_scope: str = Field(None, alias="export_scope")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    record_type: str = Field(None, alias="record_type")
    time_range_end: datetime = Field(None, alias="time_range_end")
    time_range_start: datetime = Field(None, alias="time_range_start")

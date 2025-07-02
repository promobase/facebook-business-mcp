"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CloudbridgeDatasetStatusField = Literal[
    "app_redacted_event",
    "app_sensitive_params",
    "app_unverified_event",
    "has_app_associated",
    "is_app_prohibited",
    "is_dataset",
]


class CloudbridgeDatasetStatusFields(BaseModel):
    """Pydantic model for CloudbridgeDatasetStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_redacted_event: list[str] = Field(None, alias="app_redacted_event")
    app_sensitive_params: list[dict[str, list[str]]] = Field(None, alias="app_sensitive_params")
    app_unverified_event: list[str] = Field(None, alias="app_unverified_event")
    has_app_associated: bool = Field(None, alias="has_app_associated")
    is_app_prohibited: bool = Field(None, alias="is_app_prohibited")
    is_dataset: bool = Field(None, alias="is_dataset")

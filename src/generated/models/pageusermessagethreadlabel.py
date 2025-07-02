"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageUserMessageThreadLabelField = Literal["id", "page_label_name"]


class PageUserMessageThreadLabelFields(BaseModel):
    """Pydantic model for PageUserMessageThreadLabel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    page_label_name: str = Field(None, alias="page_label_name")


class PageUserMessageThreadLabelDeleteLabelParams(BaseModel):
    """Parameters for PageUserMessageThreadLabel.delete_label()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")


class PageUserMessageThreadLabelCreateLabelParams(BaseModel):
    """Parameters for PageUserMessageThreadLabel.create_label()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")

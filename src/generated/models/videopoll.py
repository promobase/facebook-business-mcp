"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class VideoPoll_status(str, Enum):
    """VideoPoll_status enum values."""

    closed = "closed"
    results_open = "results_open"
    voting_open = "voting_open"


# Field literal type
VideoPollField = Literal[
    "close_after_voting",
    "default_open",
    "id",
    "question",
    "show_gradient",
    "show_results",
    "status",
]


class VideoPollFields(BaseModel):
    """Pydantic model for VideoPoll fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    close_after_voting: bool = Field(None, alias="close_after_voting")
    default_open: bool = Field(None, alias="default_open")
    id: str = Field(None, alias="id")
    question: str = Field(None, alias="question")
    show_gradient: bool = Field(None, alias="show_gradient")
    show_results: bool = Field(None, alias="show_results")
    status: dict[str, Any] = Field(None, alias="status")

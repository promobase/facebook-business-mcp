"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
PagePostExperimentField = Literal[
    "auto_resolve_settings",
    "control_video_id",
    "creation_time",
    "creator",
    "declared_winning_time",
    "declared_winning_video_id",
    "description",
    "experiment_video_ids",
    "id",
    "insight_snapshots",
    "name",
    "optimization_goal",
    "publish_status",
    "publish_time",
    "scheduled_experiment_timestamp",
    "updated_time",
]


class PagePostExperimentFields(BaseModel):
    """Pydantic model for PagePostExperiment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    auto_resolve_settings: dict[str, Any] = Field(None, alias="auto_resolve_settings")
    control_video_id: str = Field(None, alias="control_video_id")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: UserFields = Field(None, alias="creator")
    declared_winning_time: datetime = Field(None, alias="declared_winning_time")
    declared_winning_video_id: str = Field(None, alias="declared_winning_video_id")
    description: str = Field(None, alias="description")
    experiment_video_ids: list[str] = Field(None, alias="experiment_video_ids")
    id: str = Field(None, alias="id")
    insight_snapshots: list[dict[datetime, list[dict[int, dict[str, Any]]]]] = Field(
        None, alias="insight_snapshots"
    )
    name: str = Field(None, alias="name")
    optimization_goal: str = Field(None, alias="optimization_goal")
    publish_status: str = Field(None, alias="publish_status")
    publish_time: datetime = Field(None, alias="publish_time")
    scheduled_experiment_timestamp: datetime = Field(None, alias="scheduled_experiment_timestamp")
    updated_time: datetime = Field(None, alias="updated_time")

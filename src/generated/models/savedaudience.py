"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .audiencepermissionforactions import AudiencePermissionForActionsFields
    from .business import BusinessFields
    from .customaudiencestatus import CustomAudienceStatusFields
    from .targeting import TargetingFields


# Field literal type
SavedAudienceField = Literal[
    "account",
    "approximate_count_lower_bound",
    "approximate_count_upper_bound",
    "delete_time",
    "description",
    "id",
    "name",
    "operation_status",
    "owner_business",
    "page_deletion_marked_delete_time",
    "permission_for_actions",
    "run_status",
    "sentence_lines",
    "targeting",
    "time_created",
    "time_updated",
]


class SavedAudienceFields(BaseModel):
    """Pydantic model for SavedAudience fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account: AdAccountFields = Field(None, alias="account")
    approximate_count_lower_bound: int = Field(None, alias="approximate_count_lower_bound")
    approximate_count_upper_bound: int = Field(None, alias="approximate_count_upper_bound")
    delete_time: int = Field(None, alias="delete_time")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    operation_status: CustomAudienceStatusFields = Field(None, alias="operation_status")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    page_deletion_marked_delete_time: int = Field(None, alias="page_deletion_marked_delete_time")
    permission_for_actions: AudiencePermissionForActionsFields = Field(
        None, alias="permission_for_actions"
    )
    run_status: str = Field(None, alias="run_status")
    sentence_lines: dict[str, Any] = Field(None, alias="sentence_lines")
    targeting: TargetingFields = Field(None, alias="targeting")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CPASAdCreationTemplateField = Literal[
    "description",
    "id",
    "is_unused_template",
    "name",
    "optimization_goal",
    "targeting_type",
    "template_type",
]


class CPASAdCreationTemplateFields(BaseModel):
    """Pydantic model for CPASAdCreationTemplate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    is_unused_template: bool = Field(None, alias="is_unused_template")
    name: str = Field(None, alias="name")
    optimization_goal: str = Field(None, alias="optimization_goal")
    targeting_type: str = Field(None, alias="targeting_type")
    template_type: str = Field(None, alias="template_type")

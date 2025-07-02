"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeInteractiveComponentsSpecField = Literal["child_attachments", "components"]


class AdCreativeInteractiveComponentsSpecFields(BaseModel):
    """Pydantic model for AdCreativeInteractiveComponentsSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    child_attachments: list[dict[str, Any]] = Field(None, alias="child_attachments")
    components: list[dict[str, Any]] = Field(None, alias="components")

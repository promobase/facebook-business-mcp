"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SecuritySettingsField = Literal[""]  # No fields defined


class SecuritySettingsFields(BaseModel):
    """Pydantic model for SecuritySettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    pass  # No fields defined

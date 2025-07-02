"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
NullNodeField = Literal[""]  # No fields defined


class NullNodeFields(BaseModel):
    """Pydantic model for NullNode fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    pass  # No fields defined

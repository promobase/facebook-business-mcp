"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreationPackageConfigField = Literal[
    "api_version", "id", "is_eligible_for_default_opt_in", "objective", "package_id", "status"
]


class AdCreationPackageConfigFields(BaseModel):
    """Pydantic model for AdCreationPackageConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    api_version: str = Field(None, alias="api_version")
    id: str = Field(None, alias="id")
    is_eligible_for_default_opt_in: bool = Field(None, alias="is_eligible_for_default_opt_in")
    objective: str = Field(None, alias="objective")
    package_id: str = Field(None, alias="package_id")
    status: str = Field(None, alias="status")

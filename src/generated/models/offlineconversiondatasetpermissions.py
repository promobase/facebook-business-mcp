"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OfflineConversionDataSetPermissionsField = Literal[
    "can_edit", "can_edit_or_upload", "can_upload", "should_block_vanilla_business_employee_access"
]


class OfflineConversionDataSetPermissionsFields(BaseModel):
    """Pydantic model for OfflineConversionDataSetPermissions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_edit: bool = Field(None, alias="can_edit")
    can_edit_or_upload: bool = Field(None, alias="can_edit_or_upload")
    can_upload: bool = Field(None, alias="can_upload")
    should_block_vanilla_business_employee_access: bool = Field(
        None, alias="should_block_vanilla_business_employee_access"
    )

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessVideoTBusinessFolderPathItemField = Literal["id", "parent_folder_id", "type"]


class BusinessVideoTBusinessFolderPathItemFields(BaseModel):
    """Pydantic model for BusinessVideoTBusinessFolderPathItem fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    parent_folder_id: str = Field(None, alias="parent_folder_id")
    type: str = Field(None, alias="type")

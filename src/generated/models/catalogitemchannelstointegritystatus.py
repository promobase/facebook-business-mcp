"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogItemChannelsToIntegrityStatusField = Literal["channels", "rejection_information"]


class CatalogItemChannelsToIntegrityStatusFields(BaseModel):
    """Pydantic model for CatalogItemChannelsToIntegrityStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    channels: list[str] = Field(None, alias="channels")
    rejection_information: dict[str, Any] = Field(None, alias="rejection_information")

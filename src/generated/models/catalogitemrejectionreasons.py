"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogItemRejectionReasonsField = Literal["capability", "rejection_information"]


class CatalogItemRejectionReasonsFields(BaseModel):
    """Pydantic model for CatalogItemRejectionReasons fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    capability: str = Field(None, alias="capability")
    rejection_information: list[dict[str, Any]] = Field(None, alias="rejection_information")

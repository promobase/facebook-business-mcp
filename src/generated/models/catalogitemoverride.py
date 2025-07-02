"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productitemlocalinfo import ProductItemLocalInfoFields


# Field literal type
CatalogItemOverrideField = Literal["id", "local_info", "override_type", "override_value"]


class CatalogItemOverrideFields(BaseModel):
    """Pydantic model for CatalogItemOverride fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    local_info: ProductItemLocalInfoFields = Field(None, alias="local_info")
    override_type: str = Field(None, alias="override_type")
    override_value: str = Field(None, alias="override_value")

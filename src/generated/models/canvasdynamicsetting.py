"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .canvas import CanvasFields


# Field literal type
CanvasDynamicSettingField = Literal["child_documents", "product_set_id"]


class CanvasDynamicSettingFields(BaseModel):
    """Pydantic model for CanvasDynamicSetting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    child_documents: list[CanvasFields] = Field(None, alias="child_documents")
    product_set_id: str = Field(None, alias="product_set_id")

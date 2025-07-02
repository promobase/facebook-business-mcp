"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .photo import PhotoFields


# Field literal type
CanvasCollectionThumbnailField = Literal["element_child_index", "element_id", "photo"]


class CanvasCollectionThumbnailFields(BaseModel):
    """Pydantic model for CanvasCollectionThumbnail fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    element_child_index: int = Field(None, alias="element_child_index")
    element_id: str = Field(None, alias="element_id")
    photo: PhotoFields = Field(None, alias="photo")

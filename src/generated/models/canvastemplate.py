"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .canvas import CanvasFields
    from .photo import PhotoFields
    from .user import UserFields


# Field literal type
CanvasTemplateField = Literal[
    "channels",
    "description",
    "document",
    "id",
    "is_multi_tab_supportable",
    "is_new",
    "name",
    "objectives",
    "owner_id",
    "required_capabilities",
    "snapshot_photo",
    "status",
    "sub_verticals",
    "verticals",
]


class CanvasTemplateFields(BaseModel):
    """Pydantic model for CanvasTemplate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    channels: list[dict[str, list[dict[str, str]]]] = Field(None, alias="channels")
    description: str = Field(None, alias="description")
    document: CanvasFields = Field(None, alias="document")
    id: str = Field(None, alias="id")
    is_multi_tab_supportable: bool = Field(None, alias="is_multi_tab_supportable")
    is_new: bool = Field(None, alias="is_new")
    name: str = Field(None, alias="name")
    objectives: list[dict[dict[str, Any], dict[str, Any]]] = Field(None, alias="objectives")
    owner_id: UserFields = Field(None, alias="owner_id")
    required_capabilities: list[str] = Field(None, alias="required_capabilities")
    snapshot_photo: PhotoFields = Field(None, alias="snapshot_photo")
    status: str = Field(None, alias="status")
    sub_verticals: list[str] = Field(None, alias="sub_verticals")
    verticals: list[dict[str, str]] = Field(None, alias="verticals")

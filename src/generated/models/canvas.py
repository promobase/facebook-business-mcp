"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .advideo import AdVideoFields
    from .canvascollectionthumbnail import CanvasCollectionThumbnailFields
    from .canvasdynamicsetting import CanvasDynamicSettingFields
    from .canvastemplate import CanvasTemplateFields
    from .page import PageFields
    from .photo import PhotoFields
    from .richmediaelement import RichMediaElementFields
    from .user import UserFields


# Field literal type
CanvasField = Literal[
    "background_color",
    "body_elements",
    "business_id",
    "canvas_link",
    "collection_hero_image",
    "collection_hero_video",
    "collection_thumbnails",
    "dynamic_setting",
    "element_payload",
    "elements",
    "fb_body_elements",
    "id",
    "is_hidden",
    "is_published",
    "last_editor",
    "linked_documents",
    "name",
    "owner",
    "property_list",
    "source_template",
    "store_url",
    "style_list",
    "tags",
    "ui_property_list",
    "unused_body_elements",
    "update_time",
    "use_retailer_item_ids",
]


class CanvasFields(BaseModel):
    """Pydantic model for Canvas fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    background_color: str = Field(None, alias="background_color")
    body_elements: list[dict[str, Any]] = Field(None, alias="body_elements")
    business_id: str = Field(None, alias="business_id")
    canvas_link: str = Field(None, alias="canvas_link")
    collection_hero_image: PhotoFields = Field(None, alias="collection_hero_image")
    collection_hero_video: AdVideoFields = Field(None, alias="collection_hero_video")
    collection_thumbnails: list[CanvasCollectionThumbnailFields] = Field(
        None, alias="collection_thumbnails"
    )
    dynamic_setting: CanvasDynamicSettingFields = Field(None, alias="dynamic_setting")
    element_payload: str = Field(None, alias="element_payload")
    elements: list[RichMediaElementFields] = Field(None, alias="elements")
    fb_body_elements: list[dict[str, Any]] = Field(None, alias="fb_body_elements")
    id: str = Field(None, alias="id")
    is_hidden: bool = Field(None, alias="is_hidden")
    is_published: bool = Field(None, alias="is_published")
    last_editor: UserFields = Field(None, alias="last_editor")
    linked_documents: list[CanvasFields] = Field(None, alias="linked_documents")
    name: str = Field(None, alias="name")
    owner: PageFields = Field(None, alias="owner")
    property_list: list[str] = Field(None, alias="property_list")
    source_template: CanvasTemplateFields = Field(None, alias="source_template")
    store_url: str = Field(None, alias="store_url")
    style_list: list[str] = Field(None, alias="style_list")
    tags: list[str] = Field(None, alias="tags")
    ui_property_list: list[str] = Field(None, alias="ui_property_list")
    unused_body_elements: list[dict[str, Any]] = Field(None, alias="unused_body_elements")
    update_time: int = Field(None, alias="update_time")
    use_retailer_item_ids: bool = Field(None, alias="use_retailer_item_ids")


class CanvasGetPreviewsParams(BaseModel):
    """Parameters for Canvas.get_previews()."""

    model_config = ConfigDict(extra="forbid")
    user_ids: list[int] | None = Field(None, description="user_ids parameter")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields
    from .page import PageFields


class MediaTitle_image_fetch_status(str, Enum):
    """MediaTitle_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class MediaTitle_visibility(str, Enum):
    """MediaTitle_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class mediatitleoverride_details_type_enum_param(str, Enum):
    """mediatitleoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
MediaTitleField = Literal[
    "applinks",
    "category_specific_fields",
    "content_category",
    "currency",
    "description",
    "fb_page_alias",
    "fb_page_id",
    "genres",
    "id",
    "image_fetch_status",
    "images",
    "kg_fb_id",
    "media_title_id",
    "price",
    "sanitized_images",
    "title",
    "title_display_name",
    "unit_price",
    "url",
    "visibility",
    "wiki_data_item",
]


class MediaTitleFields(BaseModel):
    """Pydantic model for MediaTitle fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    content_category: str = Field(None, alias="content_category")
    currency: str = Field(None, alias="currency")
    description: str = Field(None, alias="description")
    fb_page_alias: str = Field(None, alias="fb_page_alias")
    fb_page_id: PageFields = Field(None, alias="fb_page_id")
    genres: list[str] = Field(None, alias="genres")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    kg_fb_id: str = Field(None, alias="kg_fb_id")
    media_title_id: str = Field(None, alias="media_title_id")
    price: str = Field(None, alias="price")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    title: str = Field(None, alias="title")
    title_display_name: str = Field(None, alias="title_display_name")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")
    wiki_data_item: str = Field(None, alias="wiki_data_item")


class MediaTitleGetOverrideDetailsParams(BaseModel):
    """Parameters for MediaTitle.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: mediatitleoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )

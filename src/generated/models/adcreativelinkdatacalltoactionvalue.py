"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeLinkDataCallToActionValueField = Literal[
    "app_destination",
    "app_link",
    "application",
    "event_id",
    "lead_gen_form_id",
    "link",
    "link_caption",
    "link_format",
    "object_store_urls",
    "page",
    "product_link",
    "whatsapp_number",
]


class AdCreativeLinkDataCallToActionValueFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataCallToActionValue fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_destination: str = Field(None, alias="app_destination")
    app_link: str = Field(None, alias="app_link")
    application: str = Field(None, alias="application")
    event_id: str = Field(None, alias="event_id")
    lead_gen_form_id: str = Field(None, alias="lead_gen_form_id")
    link: str = Field(None, alias="link")
    link_caption: str = Field(None, alias="link_caption")
    link_format: str = Field(None, alias="link_format")
    object_store_urls: list[str] = Field(None, alias="object_store_urls")
    page: str = Field(None, alias="page")
    product_link: str = Field(None, alias="product_link")
    whatsapp_number: str = Field(None, alias="whatsapp_number")

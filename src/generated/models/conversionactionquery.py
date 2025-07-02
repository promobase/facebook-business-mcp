"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ConversionActionQueryField = Literal[
    "action.type",
    "application",
    "conversion_id",
    "creative",
    "dataset",
    "event",
    "event.creator",
    "event_type",
    "fb_pixel",
    "fb_pixel_event",
    "leadgen",
    "object",
    "object.domain",
    "offer",
    "offer.creator",
    "offsite_pixel",
    "page",
    "page.parent",
    "post",
    "post.object",
    "post.object.wall",
    "post.wall",
    "question",
    "question.creator",
    "response",
    "subtype",
]


class ConversionActionQueryFields(BaseModel):
    """Pydantic model for ConversionActionQuery fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_type: list[dict[str, Any]] = Field(None, alias="action.type")
    application: list[dict[str, Any]] = Field(None, alias="application")
    conversion_id: list[str] = Field(None, alias="conversion_id")
    creative: list[dict[str, Any]] = Field(None, alias="creative")
    dataset: list[str] = Field(None, alias="dataset")
    event: list[str] = Field(None, alias="event")
    event_creator: list[str] = Field(None, alias="event.creator")
    event_type: list[str] = Field(None, alias="event_type")
    fb_pixel: list[str] = Field(None, alias="fb_pixel")
    fb_pixel_event: list[str] = Field(None, alias="fb_pixel_event")
    leadgen: list[str] = Field(None, alias="leadgen")
    object: list[str] = Field(None, alias="object")
    object_domain: list[str] = Field(None, alias="object.domain")
    offer: list[str] = Field(None, alias="offer")
    offer_creator: list[str] = Field(None, alias="offer.creator")
    offsite_pixel: list[str] = Field(None, alias="offsite_pixel")
    page: list[str] = Field(None, alias="page")
    page_parent: list[str] = Field(None, alias="page.parent")
    post: list[str] = Field(None, alias="post")
    post_object: list[str] = Field(None, alias="post.object")
    post_object_wall: list[str] = Field(None, alias="post.object.wall")
    post_wall: list[str] = Field(None, alias="post.wall")
    question: list[str] = Field(None, alias="question")
    question_creator: list[str] = Field(None, alias="question.creator")
    response: list[str] = Field(None, alias="response")
    subtype: list[str] = Field(None, alias="subtype")

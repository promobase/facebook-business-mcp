"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CanvasAdSettingsField = Literal[
    "is_canvas_collection_eligible",
    "lead_form_created_time",
    "lead_form_name",
    "lead_gen_form_id",
    "leads_count",
    "product_set_id",
    "use_retailer_item_ids",
]


class CanvasAdSettingsFields(BaseModel):
    """Pydantic model for CanvasAdSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_canvas_collection_eligible: bool = Field(None, alias="is_canvas_collection_eligible")
    lead_form_created_time: int = Field(None, alias="lead_form_created_time")
    lead_form_name: str = Field(None, alias="lead_form_name")
    lead_gen_form_id: str = Field(None, alias="lead_gen_form_id")
    leads_count: int = Field(None, alias="leads_count")
    product_set_id: str = Field(None, alias="product_set_id")
    use_retailer_item_ids: bool = Field(None, alias="use_retailer_item_ids")

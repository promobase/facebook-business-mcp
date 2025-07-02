"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsActionStatsField = Literal[
    "1d_click",
    "1d_click_all_conversions",
    "1d_click_first_conversion",
    "1d_ev",
    "1d_ev_all_conversions",
    "1d_ev_first_conversion",
    "1d_view",
    "1d_view_all_conversions",
    "1d_view_first_conversion",
    "28d_click",
    "28d_click_all_conversions",
    "28d_click_first_conversion",
    "28d_view",
    "28d_view_all_conversions",
    "28d_view_first_conversion",
    "7d_click",
    "7d_click_all_conversions",
    "7d_click_first_conversion",
    "7d_view",
    "7d_view_all_conversions",
    "7d_view_first_conversion",
    "action_brand",
    "action_canvas_component_id",
    "action_canvas_component_name",
    "action_carousel_card_id",
    "action_carousel_card_name",
    "action_category",
    "action_converted_product_id",
    "action_destination",
    "action_device",
    "action_event_channel",
    "action_link_click_destination",
    "action_location_code",
    "action_reaction",
    "action_target_id",
    "action_type",
    "action_video_asset_id",
    "action_video_sound",
    "action_video_type",
    "dda",
    "incrementality",
    "incrementality_all_conversions",
    "incrementality_first_conversion",
    "inline",
    "interactive_component_sticker_id",
    "interactive_component_sticker_response",
    "skan_click",
    "skan_click_second_postback",
    "skan_click_third_postback",
    "skan_view",
    "skan_view_second_postback",
    "skan_view_third_postback",
    "value",
]


class AdsActionStatsFields(BaseModel):
    """Pydantic model for AdsActionStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    field_1d_click: str = Field(None, alias="1d_click")
    field_1d_click_all_conversions: str = Field(None, alias="1d_click_all_conversions")
    field_1d_click_first_conversion: str = Field(None, alias="1d_click_first_conversion")
    field_1d_ev: str = Field(None, alias="1d_ev")
    field_1d_ev_all_conversions: str = Field(None, alias="1d_ev_all_conversions")
    field_1d_ev_first_conversion: str = Field(None, alias="1d_ev_first_conversion")
    field_1d_view: str = Field(None, alias="1d_view")
    field_1d_view_all_conversions: str = Field(None, alias="1d_view_all_conversions")
    field_1d_view_first_conversion: str = Field(None, alias="1d_view_first_conversion")
    field_28d_click: str = Field(None, alias="28d_click")
    field_28d_click_all_conversions: str = Field(None, alias="28d_click_all_conversions")
    field_28d_click_first_conversion: str = Field(None, alias="28d_click_first_conversion")
    field_28d_view: str = Field(None, alias="28d_view")
    field_28d_view_all_conversions: str = Field(None, alias="28d_view_all_conversions")
    field_28d_view_first_conversion: str = Field(None, alias="28d_view_first_conversion")
    field_7d_click: str = Field(None, alias="7d_click")
    field_7d_click_all_conversions: str = Field(None, alias="7d_click_all_conversions")
    field_7d_click_first_conversion: str = Field(None, alias="7d_click_first_conversion")
    field_7d_view: str = Field(None, alias="7d_view")
    field_7d_view_all_conversions: str = Field(None, alias="7d_view_all_conversions")
    field_7d_view_first_conversion: str = Field(None, alias="7d_view_first_conversion")
    action_brand: str = Field(None, alias="action_brand")
    action_canvas_component_id: str = Field(None, alias="action_canvas_component_id")
    action_canvas_component_name: str = Field(None, alias="action_canvas_component_name")
    action_carousel_card_id: str = Field(None, alias="action_carousel_card_id")
    action_carousel_card_name: str = Field(None, alias="action_carousel_card_name")
    action_category: str = Field(None, alias="action_category")
    action_converted_product_id: str = Field(None, alias="action_converted_product_id")
    action_destination: str = Field(None, alias="action_destination")
    action_device: str = Field(None, alias="action_device")
    action_event_channel: str = Field(None, alias="action_event_channel")
    action_link_click_destination: str = Field(None, alias="action_link_click_destination")
    action_location_code: str = Field(None, alias="action_location_code")
    action_reaction: str = Field(None, alias="action_reaction")
    action_target_id: str = Field(None, alias="action_target_id")
    action_type: str = Field(None, alias="action_type")
    action_video_asset_id: str = Field(None, alias="action_video_asset_id")
    action_video_sound: str = Field(None, alias="action_video_sound")
    action_video_type: str = Field(None, alias="action_video_type")
    dda: str = Field(None, alias="dda")
    incrementality: str = Field(None, alias="incrementality")
    incrementality_all_conversions: str = Field(None, alias="incrementality_all_conversions")
    incrementality_first_conversion: str = Field(None, alias="incrementality_first_conversion")
    inline: str = Field(None, alias="inline")
    interactive_component_sticker_id: str = Field(None, alias="interactive_component_sticker_id")
    interactive_component_sticker_response: str = Field(
        None, alias="interactive_component_sticker_response"
    )
    skan_click: str = Field(None, alias="skan_click")
    skan_click_second_postback: str = Field(None, alias="skan_click_second_postback")
    skan_click_third_postback: str = Field(None, alias="skan_click_third_postback")
    skan_view: str = Field(None, alias="skan_view")
    skan_view_second_postback: str = Field(None, alias="skan_view_second_postback")
    skan_view_third_postback: str = Field(None, alias="skan_view_third_postback")
    value: str = Field(None, alias="value")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativefeaturedetails import AdCreativeFeatureDetailsFields


# Field literal type
AdCreativeFeaturesSpecField = Literal[
    "adapt_to_placement",
    "add_text_overlay",
    "ads_with_benefits",
    "advantage_plus_creative",
    "app_highlights",
    "audio",
    "biz_ai",
    "carousel_to_video",
    "catalog_feed_tag",
    "customize_product_recommendation",
    "cv_transformation",
    "description_automation",
    "dha_optimization",
    "dynamic_partner_content",
    "enhance_cta",
    "fb_feed_tag",
    "fb_reels_tag",
    "fb_story_tag",
    "feed_caption_optimization",
    "hide_price",
    "ig_feed_tag",
    "ig_glados_feed",
    "ig_reels_tag",
    "ig_stream_tag",
    "image_animation",
    "image_auto_crop",
    "image_background_gen",
    "image_brightness_and_contrast",
    "image_enhancement",
    "image_templates",
    "image_touchups",
    "image_uncrop",
    "inline_comment",
    "local_store_extension",
    "media_liquidity_animated_image",
    "media_order",
    "media_type_automation",
    "multi_photo_to_video",
    "music_generation",
    "pac_relaxation",
    "product_extensions",
    "product_metadata_automation",
    "product_tags",
    "profile_card",
    "profile_extension",
    "show_summary",
    "site_extensions",
    "standard_enhancements",
    "standard_enhancements_catalog",
    "text_generation",
    "text_optimizations",
    "text_translation",
    "video_auto_crop",
    "video_filtering",
    "video_highlight",
    "video_to_image",
    "video_uncrop",
]


class AdCreativeFeaturesSpecFields(BaseModel):
    """Pydantic model for AdCreativeFeaturesSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adapt_to_placement: AdCreativeFeatureDetailsFields = Field(None, alias="adapt_to_placement")
    add_text_overlay: AdCreativeFeatureDetailsFields = Field(None, alias="add_text_overlay")
    ads_with_benefits: AdCreativeFeatureDetailsFields = Field(None, alias="ads_with_benefits")
    advantage_plus_creative: AdCreativeFeatureDetailsFields = Field(
        None, alias="advantage_plus_creative"
    )
    app_highlights: AdCreativeFeatureDetailsFields = Field(None, alias="app_highlights")
    audio: AdCreativeFeatureDetailsFields = Field(None, alias="audio")
    biz_ai: AdCreativeFeatureDetailsFields = Field(None, alias="biz_ai")
    carousel_to_video: AdCreativeFeatureDetailsFields = Field(None, alias="carousel_to_video")
    catalog_feed_tag: AdCreativeFeatureDetailsFields = Field(None, alias="catalog_feed_tag")
    customize_product_recommendation: AdCreativeFeatureDetailsFields = Field(
        None, alias="customize_product_recommendation"
    )
    cv_transformation: AdCreativeFeatureDetailsFields = Field(None, alias="cv_transformation")
    description_automation: AdCreativeFeatureDetailsFields = Field(
        None, alias="description_automation"
    )
    dha_optimization: AdCreativeFeatureDetailsFields = Field(None, alias="dha_optimization")
    dynamic_partner_content: AdCreativeFeatureDetailsFields = Field(
        None, alias="dynamic_partner_content"
    )
    enhance_cta: AdCreativeFeatureDetailsFields = Field(None, alias="enhance_cta")
    fb_feed_tag: AdCreativeFeatureDetailsFields = Field(None, alias="fb_feed_tag")
    fb_reels_tag: AdCreativeFeatureDetailsFields = Field(None, alias="fb_reels_tag")
    fb_story_tag: AdCreativeFeatureDetailsFields = Field(None, alias="fb_story_tag")
    feed_caption_optimization: AdCreativeFeatureDetailsFields = Field(
        None, alias="feed_caption_optimization"
    )
    hide_price: AdCreativeFeatureDetailsFields = Field(None, alias="hide_price")
    ig_feed_tag: AdCreativeFeatureDetailsFields = Field(None, alias="ig_feed_tag")
    ig_glados_feed: AdCreativeFeatureDetailsFields = Field(None, alias="ig_glados_feed")
    ig_reels_tag: AdCreativeFeatureDetailsFields = Field(None, alias="ig_reels_tag")
    ig_stream_tag: AdCreativeFeatureDetailsFields = Field(None, alias="ig_stream_tag")
    image_animation: AdCreativeFeatureDetailsFields = Field(None, alias="image_animation")
    image_auto_crop: AdCreativeFeatureDetailsFields = Field(None, alias="image_auto_crop")
    image_background_gen: AdCreativeFeatureDetailsFields = Field(None, alias="image_background_gen")
    image_brightness_and_contrast: AdCreativeFeatureDetailsFields = Field(
        None, alias="image_brightness_and_contrast"
    )
    image_enhancement: AdCreativeFeatureDetailsFields = Field(None, alias="image_enhancement")
    image_templates: AdCreativeFeatureDetailsFields = Field(None, alias="image_templates")
    image_touchups: AdCreativeFeatureDetailsFields = Field(None, alias="image_touchups")
    image_uncrop: AdCreativeFeatureDetailsFields = Field(None, alias="image_uncrop")
    inline_comment: AdCreativeFeatureDetailsFields = Field(None, alias="inline_comment")
    local_store_extension: AdCreativeFeatureDetailsFields = Field(
        None, alias="local_store_extension"
    )
    media_liquidity_animated_image: AdCreativeFeatureDetailsFields = Field(
        None, alias="media_liquidity_animated_image"
    )
    media_order: AdCreativeFeatureDetailsFields = Field(None, alias="media_order")
    media_type_automation: AdCreativeFeatureDetailsFields = Field(
        None, alias="media_type_automation"
    )
    multi_photo_to_video: AdCreativeFeatureDetailsFields = Field(None, alias="multi_photo_to_video")
    music_generation: AdCreativeFeatureDetailsFields = Field(None, alias="music_generation")
    pac_relaxation: AdCreativeFeatureDetailsFields = Field(None, alias="pac_relaxation")
    product_extensions: AdCreativeFeatureDetailsFields = Field(None, alias="product_extensions")
    product_metadata_automation: AdCreativeFeatureDetailsFields = Field(
        None, alias="product_metadata_automation"
    )
    product_tags: AdCreativeFeatureDetailsFields = Field(None, alias="product_tags")
    profile_card: AdCreativeFeatureDetailsFields = Field(None, alias="profile_card")
    profile_extension: AdCreativeFeatureDetailsFields = Field(None, alias="profile_extension")
    show_summary: AdCreativeFeatureDetailsFields = Field(None, alias="show_summary")
    site_extensions: AdCreativeFeatureDetailsFields = Field(None, alias="site_extensions")
    standard_enhancements: AdCreativeFeatureDetailsFields = Field(
        None, alias="standard_enhancements"
    )
    standard_enhancements_catalog: AdCreativeFeatureDetailsFields = Field(
        None, alias="standard_enhancements_catalog"
    )
    text_generation: AdCreativeFeatureDetailsFields = Field(None, alias="text_generation")
    text_optimizations: AdCreativeFeatureDetailsFields = Field(None, alias="text_optimizations")
    text_translation: AdCreativeFeatureDetailsFields = Field(None, alias="text_translation")
    video_auto_crop: AdCreativeFeatureDetailsFields = Field(None, alias="video_auto_crop")
    video_filtering: AdCreativeFeatureDetailsFields = Field(None, alias="video_filtering")
    video_highlight: AdCreativeFeatureDetailsFields = Field(None, alias="video_highlight")
    video_to_image: AdCreativeFeatureDetailsFields = Field(None, alias="video_to_image")
    video_uncrop: AdCreativeFeatureDetailsFields = Field(None, alias="video_uncrop")

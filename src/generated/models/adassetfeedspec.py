"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedadditionaldata import AdAssetFeedAdditionalDataFields
    from .adassetfeedspecassetcustomizationrule import AdAssetFeedSpecAssetCustomizationRuleFields
    from .adassetfeedspecbody import AdAssetFeedSpecBodyFields
    from .adassetfeedspeccalltoaction import AdAssetFeedSpecCallToActionFields
    from .adassetfeedspeccaption import AdAssetFeedSpecCaptionFields
    from .adassetfeedspeccarousel import AdAssetFeedSpecCarouselFields
    from .adassetfeedspecdescription import AdAssetFeedSpecDescriptionFields
    from .adassetfeedspecevents import AdAssetFeedSpecEventsFields
    from .adassetfeedspecgrouprule import AdAssetFeedSpecGroupRuleFields
    from .adassetfeedspecimage import AdAssetFeedSpecImageFields
    from .adassetfeedspeclinkurl import AdAssetFeedSpecLinkURLFields
    from .adassetfeedspectitle import AdAssetFeedSpecTitleFields
    from .adassetfeedspecvideo import AdAssetFeedSpecVideoFields
    from .adassetmessageextensions import AdAssetMessageExtensionsFields
    from .adassetonsitedestinations import AdAssetOnsiteDestinationsFields


# Field literal type
AdAssetFeedSpecField = Literal[
    "ad_formats",
    "additional_data",
    "app_product_page_id",
    "asset_customization_rules",
    "audios",
    "autotranslate",
    "bodies",
    "call_ads_configuration",
    "call_to_action_types",
    "call_to_actions",
    "captions",
    "carousels",
    "ctwa_consent_data",
    "descriptions",
    "events",
    "groups",
    "images",
    "link_urls",
    "message_extensions",
    "onsite_destinations",
    "optimization_type",
    "promotional_metadata",
    "reasons_to_shop",
    "shops_bundle",
    "titles",
    "translations",
    "upcoming_events",
    "videos",
]


class AdAssetFeedSpecFields(BaseModel):
    """Pydantic model for AdAssetFeedSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_formats: list[str] = Field(None, alias="ad_formats")
    additional_data: AdAssetFeedAdditionalDataFields = Field(None, alias="additional_data")
    app_product_page_id: str = Field(None, alias="app_product_page_id")
    asset_customization_rules: list[AdAssetFeedSpecAssetCustomizationRuleFields] = Field(
        None, alias="asset_customization_rules"
    )
    audios: list[dict[str, Any]] = Field(None, alias="audios")
    autotranslate: list[str] = Field(None, alias="autotranslate")
    bodies: list[AdAssetFeedSpecBodyFields] = Field(None, alias="bodies")
    call_ads_configuration: dict[str, Any] = Field(None, alias="call_ads_configuration")
    call_to_action_types: list[dict[str, Any]] = Field(None, alias="call_to_action_types")
    call_to_actions: list[AdAssetFeedSpecCallToActionFields] = Field(None, alias="call_to_actions")
    captions: list[AdAssetFeedSpecCaptionFields] = Field(None, alias="captions")
    carousels: list[AdAssetFeedSpecCarouselFields] = Field(None, alias="carousels")
    ctwa_consent_data: list[dict[str, Any]] = Field(None, alias="ctwa_consent_data")
    descriptions: list[AdAssetFeedSpecDescriptionFields] = Field(None, alias="descriptions")
    events: list[AdAssetFeedSpecEventsFields] = Field(None, alias="events")
    groups: list[AdAssetFeedSpecGroupRuleFields] = Field(None, alias="groups")
    images: list[AdAssetFeedSpecImageFields] = Field(None, alias="images")
    link_urls: list[AdAssetFeedSpecLinkURLFields] = Field(None, alias="link_urls")
    message_extensions: list[AdAssetMessageExtensionsFields] = Field(
        None, alias="message_extensions"
    )
    onsite_destinations: list[AdAssetOnsiteDestinationsFields] = Field(
        None, alias="onsite_destinations"
    )
    optimization_type: str = Field(None, alias="optimization_type")
    promotional_metadata: dict[str, Any] = Field(None, alias="promotional_metadata")
    reasons_to_shop: bool = Field(None, alias="reasons_to_shop")
    shops_bundle: bool = Field(None, alias="shops_bundle")
    titles: list[AdAssetFeedSpecTitleFields] = Field(None, alias="titles")
    translations: list[dict[str, Any]] = Field(None, alias="translations")
    upcoming_events: list[dict[str, Any]] = Field(None, alias="upcoming_events")
    videos: list[AdAssetFeedSpecVideoFields] = Field(None, alias="videos")

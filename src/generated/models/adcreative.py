"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspec import AdAssetFeedSpecFields
    from .adcreativeaddisclaimer import AdCreativeAdDisclaimerFields
    from .adcreativebrandedcontentads import AdCreativeBrandedContentAdsFields
    from .adcreativecontextualmultiads import AdCreativeContextualMultiAdsFields
    from .adcreativedegreesoffreedomspec import AdCreativeDegreesOfFreedomSpecFields
    from .adcreativefacebookbrandedcontent import AdCreativeFacebookBrandedContentFields
    from .adcreativeinstagrambrandedcontent import AdCreativeInstagramBrandedContentFields
    from .adcreativeinteractivecomponentsspec import AdCreativeInteractiveComponentsSpecFields
    from .adcreativelinkdatacalltoaction import AdCreativeLinkDataCallToActionFields
    from .adcreativeobjectstoryspec import AdCreativeObjectStorySpecFields
    from .adcreativeomnichannellinkspec import AdCreativeOmnichannelLinkSpecFields
    from .adcreativeplatformcustomization import AdCreativePlatformCustomizationFields
    from .adcreativeportraitcustomizations import AdCreativePortraitCustomizationsFields
    from .adcreativeproductdata import AdCreativeProductDataFields
    from .adcreativerecommendersettings import AdCreativeRecommenderSettingsFields
    from .adcreativeregionalregulationdisclaimer import AdCreativeRegionalRegulationDisclaimerFields
    from .adcreativesourcingspec import AdCreativeSourcingSpecFields
    from .adcreativetemplateurlspec import AdCreativeTemplateURLSpecFields
    from .adlabel import AdLabelFields
    from .adsimagecrops import AdsImageCropsFields


class AdCreative_call_to_action_type(str, Enum):
    """AdCreative_call_to_action_type enum values."""

    ADD_TO_CART = "ADD_TO_CART"
    APPLY_NOW = "APPLY_NOW"
    ASK_ABOUT_SERVICES = "ASK_ABOUT_SERVICES"
    ASK_FOR_MORE_INFO = "ASK_FOR_MORE_INFO"
    AUDIO_CALL = "AUDIO_CALL"
    BOOK_A_CONSULTATION = "BOOK_A_CONSULTATION"
    BOOK_NOW = "BOOK_NOW"
    BOOK_TRAVEL = "BOOK_TRAVEL"
    BUY = "BUY"
    BUY_NOW = "BUY_NOW"
    BUY_TICKETS = "BUY_TICKETS"
    BUY_VIA_MESSAGE = "BUY_VIA_MESSAGE"
    CALL = "CALL"
    CALL_ME = "CALL_ME"
    CALL_NOW = "CALL_NOW"
    CHAT_WITH_US = "CHAT_WITH_US"
    CONFIRM = "CONFIRM"
    CONTACT = "CONTACT"
    CONTACT_US = "CONTACT_US"
    DONATE = "DONATE"
    DONATE_NOW = "DONATE_NOW"
    DOWNLOAD = "DOWNLOAD"
    EVENT_RSVP = "EVENT_RSVP"
    FIND_A_GROUP = "FIND_A_GROUP"
    FIND_YOUR_GROUPS = "FIND_YOUR_GROUPS"
    FOLLOW_NEWS_STORYLINE = "FOLLOW_NEWS_STORYLINE"
    FOLLOW_PAGE = "FOLLOW_PAGE"
    FOLLOW_USER = "FOLLOW_USER"
    GET_A_QUOTE = "GET_A_QUOTE"
    GET_DIRECTIONS = "GET_DIRECTIONS"
    GET_IN_TOUCH = "GET_IN_TOUCH"
    GET_OFFER = "GET_OFFER"
    GET_OFFER_VIEW = "GET_OFFER_VIEW"
    GET_PROMOTIONS = "GET_PROMOTIONS"
    GET_QUOTE = "GET_QUOTE"
    GET_SHOWTIMES = "GET_SHOWTIMES"
    GET_STARTED = "GET_STARTED"
    INQUIRE_NOW = "INQUIRE_NOW"
    INSTALL_APP = "INSTALL_APP"
    INSTALL_MOBILE_APP = "INSTALL_MOBILE_APP"
    JOIN_CHANNEL = "JOIN_CHANNEL"
    LEARN_MORE = "LEARN_MORE"
    LIKE_PAGE = "LIKE_PAGE"
    LISTEN_MUSIC = "LISTEN_MUSIC"
    LISTEN_NOW = "LISTEN_NOW"
    MAKE_AN_APPOINTMENT = "MAKE_AN_APPOINTMENT"
    MESSAGE_PAGE = "MESSAGE_PAGE"
    MOBILE_DOWNLOAD = "MOBILE_DOWNLOAD"
    NO_BUTTON = "NO_BUTTON"
    OPEN_INSTANT_APP = "OPEN_INSTANT_APP"
    OPEN_LINK = "OPEN_LINK"
    ORDER_NOW = "ORDER_NOW"
    PAY_TO_ACCESS = "PAY_TO_ACCESS"
    PLAY_GAME = "PLAY_GAME"
    PLAY_GAME_ON_FACEBOOK = "PLAY_GAME_ON_FACEBOOK"
    PURCHASE_GIFT_CARDS = "PURCHASE_GIFT_CARDS"
    RAISE_MONEY = "RAISE_MONEY"
    RECORD_NOW = "RECORD_NOW"
    REFER_FRIENDS = "REFER_FRIENDS"
    REQUEST_TIME = "REQUEST_TIME"
    SAY_THANKS = "SAY_THANKS"
    SEE_MORE = "SEE_MORE"
    SELL_NOW = "SELL_NOW"
    SEND_A_GIFT = "SEND_A_GIFT"
    SEND_GIFT_MONEY = "SEND_GIFT_MONEY"
    SEND_UPDATES = "SEND_UPDATES"
    SHARE = "SHARE"
    SHOP_NOW = "SHOP_NOW"
    SIGN_UP = "SIGN_UP"
    SOTTO_SUBSCRIBE = "SOTTO_SUBSCRIBE"
    START_ORDER = "START_ORDER"
    SUBSCRIBE = "SUBSCRIBE"
    SWIPE_UP_PRODUCT = "SWIPE_UP_PRODUCT"
    SWIPE_UP_SHOP = "SWIPE_UP_SHOP"
    UPDATE_APP = "UPDATE_APP"
    USE_APP = "USE_APP"
    USE_MOBILE_APP = "USE_MOBILE_APP"
    VIDEO_ANNOTATION = "VIDEO_ANNOTATION"
    VIDEO_CALL = "VIDEO_CALL"
    VIEW_CART = "VIEW_CART"
    VIEW_CHANNEL = "VIEW_CHANNEL"
    VIEW_IN_CART = "VIEW_IN_CART"
    VIEW_PRODUCT = "VIEW_PRODUCT"
    VISIT_PAGES_FEED = "VISIT_PAGES_FEED"
    WATCH_LIVE_VIDEO = "WATCH_LIVE_VIDEO"
    WATCH_MORE = "WATCH_MORE"
    WATCH_VIDEO = "WATCH_VIDEO"
    WHATSAPP_MESSAGE = "WHATSAPP_MESSAGE"
    WOODHENGE_SUPPORT = "WOODHENGE_SUPPORT"


class AdCreative_object_type(str, Enum):
    """AdCreative_object_type enum values."""

    APPLICATION = "APPLICATION"
    DOMAIN = "DOMAIN"
    EVENT = "EVENT"
    INVALID = "INVALID"
    OFFER = "OFFER"
    PAGE = "PAGE"
    PHOTO = "PHOTO"
    POST_DELETED = "POST_DELETED"
    PRIVACY_CHECK_FAIL = "PRIVACY_CHECK_FAIL"
    SHARE = "SHARE"
    STATUS = "STATUS"
    STORE_ITEM = "STORE_ITEM"
    VIDEO = "VIDEO"


class AdCreative_status(str, Enum):
    """AdCreative_status enum values."""

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    IN_PROCESS = "IN_PROCESS"
    WITH_ISSUES = "WITH_ISSUES"


class adcreativepreviews_ad_format_enum_param(str, Enum):
    """adcreativepreviews_ad_format_enum_param enum values."""

    AUDIENCE_NETWORK_INSTREAM_VIDEO = "AUDIENCE_NETWORK_INSTREAM_VIDEO"
    AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE = "AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE"
    AUDIENCE_NETWORK_OUTSTREAM_VIDEO = "AUDIENCE_NETWORK_OUTSTREAM_VIDEO"
    AUDIENCE_NETWORK_REWARDED_VIDEO = "AUDIENCE_NETWORK_REWARDED_VIDEO"
    BIZ_DISCO_FEED_MOBILE = "BIZ_DISCO_FEED_MOBILE"
    DESKTOP_FEED_STANDARD = "DESKTOP_FEED_STANDARD"
    FACEBOOK_PROFILE_FEED_DESKTOP = "FACEBOOK_PROFILE_FEED_DESKTOP"
    FACEBOOK_PROFILE_FEED_MOBILE = "FACEBOOK_PROFILE_FEED_MOBILE"
    FACEBOOK_PROFILE_REELS_MOBILE = "FACEBOOK_PROFILE_REELS_MOBILE"
    FACEBOOK_REELS_BANNER = "FACEBOOK_REELS_BANNER"
    FACEBOOK_REELS_BANNER_DESKTOP = "FACEBOOK_REELS_BANNER_DESKTOP"
    FACEBOOK_REELS_BANNER_FULLSCREEN_IOS = "FACEBOOK_REELS_BANNER_FULLSCREEN_IOS"
    FACEBOOK_REELS_BANNER_FULLSCREEN_MOBILE = "FACEBOOK_REELS_BANNER_FULLSCREEN_MOBILE"
    FACEBOOK_REELS_MOBILE = "FACEBOOK_REELS_MOBILE"
    FACEBOOK_REELS_POSTLOOP = "FACEBOOK_REELS_POSTLOOP"
    FACEBOOK_REELS_STICKER = "FACEBOOK_REELS_STICKER"
    FACEBOOK_STORY_MOBILE = "FACEBOOK_STORY_MOBILE"
    FACEBOOK_STORY_STICKER_MOBILE = "FACEBOOK_STORY_STICKER_MOBILE"
    INSTAGRAM_EXPLORE_CONTEXTUAL = "INSTAGRAM_EXPLORE_CONTEXTUAL"
    INSTAGRAM_EXPLORE_GRID_HOME = "INSTAGRAM_EXPLORE_GRID_HOME"
    INSTAGRAM_EXPLORE_IMMERSIVE = "INSTAGRAM_EXPLORE_IMMERSIVE"
    INSTAGRAM_FEED_WEB = "INSTAGRAM_FEED_WEB"
    INSTAGRAM_FEED_WEB_M_SITE = "INSTAGRAM_FEED_WEB_M_SITE"
    INSTAGRAM_LEAD_GEN_MULTI_SUBMIT_ADS = "INSTAGRAM_LEAD_GEN_MULTI_SUBMIT_ADS"
    INSTAGRAM_PROFILE_FEED = "INSTAGRAM_PROFILE_FEED"
    INSTAGRAM_PROFILE_REELS = "INSTAGRAM_PROFILE_REELS"
    INSTAGRAM_REELS = "INSTAGRAM_REELS"
    INSTAGRAM_REELS_OVERLAY = "INSTAGRAM_REELS_OVERLAY"
    INSTAGRAM_SEARCH_CHAIN = "INSTAGRAM_SEARCH_CHAIN"
    INSTAGRAM_SEARCH_GRID = "INSTAGRAM_SEARCH_GRID"
    INSTAGRAM_STANDARD = "INSTAGRAM_STANDARD"
    INSTAGRAM_STORY = "INSTAGRAM_STORY"
    INSTAGRAM_STORY_EFFECT_TRAY = "INSTAGRAM_STORY_EFFECT_TRAY"
    INSTAGRAM_STORY_WEB = "INSTAGRAM_STORY_WEB"
    INSTAGRAM_STORY_WEB_M_SITE = "INSTAGRAM_STORY_WEB_M_SITE"
    INSTANT_ARTICLE_RECIRCULATION_AD = "INSTANT_ARTICLE_RECIRCULATION_AD"
    INSTANT_ARTICLE_STANDARD = "INSTANT_ARTICLE_STANDARD"
    INSTREAM_BANNER_DESKTOP = "INSTREAM_BANNER_DESKTOP"
    INSTREAM_BANNER_FULLSCREEN_IOS = "INSTREAM_BANNER_FULLSCREEN_IOS"
    INSTREAM_BANNER_FULLSCREEN_MOBILE = "INSTREAM_BANNER_FULLSCREEN_MOBILE"
    INSTREAM_BANNER_IMMERSIVE_MOBILE = "INSTREAM_BANNER_IMMERSIVE_MOBILE"
    INSTREAM_BANNER_MOBILE = "INSTREAM_BANNER_MOBILE"
    INSTREAM_VIDEO_DESKTOP = "INSTREAM_VIDEO_DESKTOP"
    INSTREAM_VIDEO_FULLSCREEN_IOS = "INSTREAM_VIDEO_FULLSCREEN_IOS"
    INSTREAM_VIDEO_FULLSCREEN_MOBILE = "INSTREAM_VIDEO_FULLSCREEN_MOBILE"
    INSTREAM_VIDEO_IMAGE = "INSTREAM_VIDEO_IMAGE"
    INSTREAM_VIDEO_IMMERSIVE_MOBILE = "INSTREAM_VIDEO_IMMERSIVE_MOBILE"
    INSTREAM_VIDEO_MOBILE = "INSTREAM_VIDEO_MOBILE"
    JOB_BROWSER_DESKTOP = "JOB_BROWSER_DESKTOP"
    JOB_BROWSER_MOBILE = "JOB_BROWSER_MOBILE"
    MARKETPLACE_MOBILE = "MARKETPLACE_MOBILE"
    MESSENGER_MOBILE_INBOX_MEDIA = "MESSENGER_MOBILE_INBOX_MEDIA"
    MESSENGER_MOBILE_STORY_MEDIA = "MESSENGER_MOBILE_STORY_MEDIA"
    MOBILE_BANNER = "MOBILE_BANNER"
    MOBILE_FEED_BASIC = "MOBILE_FEED_BASIC"
    MOBILE_FEED_STANDARD = "MOBILE_FEED_STANDARD"
    MOBILE_FULLWIDTH = "MOBILE_FULLWIDTH"
    MOBILE_INTERSTITIAL = "MOBILE_INTERSTITIAL"
    MOBILE_MEDIUM_RECTANGLE = "MOBILE_MEDIUM_RECTANGLE"
    MOBILE_NATIVE = "MOBILE_NATIVE"
    RIGHT_COLUMN_STANDARD = "RIGHT_COLUMN_STANDARD"
    SUGGESTED_VIDEO_DESKTOP = "SUGGESTED_VIDEO_DESKTOP"
    SUGGESTED_VIDEO_FULLSCREEN_MOBILE = "SUGGESTED_VIDEO_FULLSCREEN_MOBILE"
    SUGGESTED_VIDEO_IMMERSIVE_MOBILE = "SUGGESTED_VIDEO_IMMERSIVE_MOBILE"
    SUGGESTED_VIDEO_MOBILE = "SUGGESTED_VIDEO_MOBILE"
    WATCH_FEED_HOME = "WATCH_FEED_HOME"
    WATCH_FEED_MOBILE = "WATCH_FEED_MOBILE"


class adcreativepreviews_render_type_enum_param(str, Enum):
    """adcreativepreviews_render_type_enum_param enum values."""

    FALLBACK = "FALLBACK"


class adcreativepreviews_creative_feature_enum_param(str, Enum):
    """adcreativepreviews_creative_feature_enum_param enum values."""

    product_metadata_automation = "product_metadata_automation"
    profile_card = "profile_card"
    standard_enhancements_catalog = "standard_enhancements_catalog"
    video_to_image = "video_to_image"


# Field literal type
AdCreativeField = Literal[
    "account_id",
    "actor_id",
    "ad_disclaimer_spec",
    "adlabels",
    "applink_treatment",
    "asset_feed_spec",
    "authorization_category",
    "auto_update",
    "body",
    "branded_content",
    "branded_content_sponsor_page_id",
    "bundle_folder_id",
    "call_to_action",
    "call_to_action_type",
    "categorization_criteria",
    "category_media_source",
    "collaborative_ads_lsb_image_bank_id",
    "contextual_multi_ads",
    "creative_sourcing_spec",
    "degrees_of_freedom_spec",
    "destination_set_id",
    "dynamic_ad_voice",
    "effective_authorization_category",
    "effective_instagram_media_id",
    "effective_object_story_id",
    "enable_direct_install",
    "enable_launch_instant_app",
    "facebook_branded_content",
    "id",
    "image_crops",
    "image_hash",
    "image_url",
    "instagram_branded_content",
    "instagram_permalink_url",
    "instagram_user_id",
    "interactive_components_spec",
    "link_deep_link_url",
    "link_destination_display_url",
    "link_og_id",
    "link_url",
    "messenger_sponsored_message",
    "name",
    "object_id",
    "object_store_url",
    "object_story_id",
    "object_story_spec",
    "object_type",
    "object_url",
    "omnichannel_link_spec",
    "page_welcome_message",
    "photo_album_source_object_story_id",
    "place_page_set_id",
    "platform_customizations",
    "playable_asset_id",
    "portrait_customizations",
    "product_data",
    "product_set_id",
    "recommender_settings",
    "regional_regulation_disclaimer_spec",
    "source_facebook_post_id",
    "source_instagram_media_id",
    "status",
    "template_url",
    "template_url_spec",
    "thumbnail_id",
    "thumbnail_url",
    "title",
    "url_tags",
    "use_page_actor_override",
    "video_id",
]


class AdCreativeFields(BaseModel):
    """Pydantic model for AdCreative fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    actor_id: str = Field(None, alias="actor_id")
    ad_disclaimer_spec: AdCreativeAdDisclaimerFields = Field(None, alias="ad_disclaimer_spec")
    adlabels: list[AdLabelFields] = Field(None, alias="adlabels")
    applink_treatment: str = Field(None, alias="applink_treatment")
    asset_feed_spec: AdAssetFeedSpecFields = Field(None, alias="asset_feed_spec")
    authorization_category: str = Field(None, alias="authorization_category")
    auto_update: bool = Field(None, alias="auto_update")
    body: str = Field(None, alias="body")
    branded_content: AdCreativeBrandedContentAdsFields = Field(None, alias="branded_content")
    branded_content_sponsor_page_id: str = Field(None, alias="branded_content_sponsor_page_id")
    bundle_folder_id: str = Field(None, alias="bundle_folder_id")
    call_to_action: AdCreativeLinkDataCallToActionFields = Field(None, alias="call_to_action")
    call_to_action_type: dict[str, Any] = Field(None, alias="call_to_action_type")
    categorization_criteria: str = Field(None, alias="categorization_criteria")
    category_media_source: str = Field(None, alias="category_media_source")
    collaborative_ads_lsb_image_bank_id: str = Field(
        None, alias="collaborative_ads_lsb_image_bank_id"
    )
    contextual_multi_ads: AdCreativeContextualMultiAdsFields = Field(
        None, alias="contextual_multi_ads"
    )
    creative_sourcing_spec: AdCreativeSourcingSpecFields = Field(
        None, alias="creative_sourcing_spec"
    )
    degrees_of_freedom_spec: AdCreativeDegreesOfFreedomSpecFields = Field(
        None, alias="degrees_of_freedom_spec"
    )
    destination_set_id: str = Field(None, alias="destination_set_id")
    dynamic_ad_voice: str = Field(None, alias="dynamic_ad_voice")
    effective_authorization_category: str = Field(None, alias="effective_authorization_category")
    effective_instagram_media_id: str = Field(None, alias="effective_instagram_media_id")
    effective_object_story_id: str = Field(None, alias="effective_object_story_id")
    enable_direct_install: bool = Field(None, alias="enable_direct_install")
    enable_launch_instant_app: bool = Field(None, alias="enable_launch_instant_app")
    facebook_branded_content: AdCreativeFacebookBrandedContentFields = Field(
        None, alias="facebook_branded_content"
    )
    id: str = Field(None, alias="id")
    image_crops: AdsImageCropsFields = Field(None, alias="image_crops")
    image_hash: str = Field(None, alias="image_hash")
    image_url: str = Field(None, alias="image_url")
    instagram_branded_content: AdCreativeInstagramBrandedContentFields = Field(
        None, alias="instagram_branded_content"
    )
    instagram_permalink_url: str = Field(None, alias="instagram_permalink_url")
    instagram_user_id: str = Field(None, alias="instagram_user_id")
    interactive_components_spec: AdCreativeInteractiveComponentsSpecFields = Field(
        None, alias="interactive_components_spec"
    )
    link_deep_link_url: str = Field(None, alias="link_deep_link_url")
    link_destination_display_url: str = Field(None, alias="link_destination_display_url")
    link_og_id: str = Field(None, alias="link_og_id")
    link_url: str = Field(None, alias="link_url")
    messenger_sponsored_message: str = Field(None, alias="messenger_sponsored_message")
    name: str = Field(None, alias="name")
    object_id: str = Field(None, alias="object_id")
    object_store_url: str = Field(None, alias="object_store_url")
    object_story_id: str = Field(None, alias="object_story_id")
    object_story_spec: AdCreativeObjectStorySpecFields = Field(None, alias="object_story_spec")
    object_type: dict[str, Any] = Field(None, alias="object_type")
    object_url: str = Field(None, alias="object_url")
    omnichannel_link_spec: AdCreativeOmnichannelLinkSpecFields = Field(
        None, alias="omnichannel_link_spec"
    )
    page_welcome_message: str = Field(None, alias="page_welcome_message")
    photo_album_source_object_story_id: str = Field(
        None, alias="photo_album_source_object_story_id"
    )
    place_page_set_id: str = Field(None, alias="place_page_set_id")
    platform_customizations: AdCreativePlatformCustomizationFields = Field(
        None, alias="platform_customizations"
    )
    playable_asset_id: str = Field(None, alias="playable_asset_id")
    portrait_customizations: AdCreativePortraitCustomizationsFields = Field(
        None, alias="portrait_customizations"
    )
    product_data: list[AdCreativeProductDataFields] = Field(None, alias="product_data")
    product_set_id: str = Field(None, alias="product_set_id")
    recommender_settings: AdCreativeRecommenderSettingsFields = Field(
        None, alias="recommender_settings"
    )
    regional_regulation_disclaimer_spec: AdCreativeRegionalRegulationDisclaimerFields = Field(
        None, alias="regional_regulation_disclaimer_spec"
    )
    source_facebook_post_id: str = Field(None, alias="source_facebook_post_id")
    source_instagram_media_id: str = Field(None, alias="source_instagram_media_id")
    status: dict[str, Any] = Field(None, alias="status")
    template_url: str = Field(None, alias="template_url")
    template_url_spec: AdCreativeTemplateURLSpecFields = Field(None, alias="template_url_spec")
    thumbnail_id: str = Field(None, alias="thumbnail_id")
    thumbnail_url: str = Field(None, alias="thumbnail_url")
    title: str = Field(None, alias="title")
    url_tags: str = Field(None, alias="url_tags")
    use_page_actor_override: bool = Field(None, alias="use_page_actor_override")
    video_id: str = Field(None, alias="video_id")


class AdCreativeCreateAdlabelParams(BaseModel):
    """Parameters for AdCreative.create_adlabel()."""

    model_config = ConfigDict(extra="forbid")
    adlabels: list[dict[str, Any]] | None = Field(None, description="adlabels parameter")


class AdCreativeGetPreviewsParams(BaseModel):
    """Parameters for AdCreative.get_previews()."""

    model_config = ConfigDict(extra="forbid")
    ad_format: adcreativepreviews_ad_format_enum_param | None = Field(
        None, description="ad_format parameter"
    )
    creative_feature: adcreativepreviews_creative_feature_enum_param | None = Field(
        None, description="creative_feature parameter"
    )
    dynamic_asset_label: str | None = Field(None, description="dynamic_asset_label parameter")
    dynamic_creative_spec: dict[str, Any] | None = Field(
        None, description="dynamic_creative_spec parameter"
    )
    dynamic_customization: dict[str, Any] | None = Field(
        None, description="dynamic_customization parameter"
    )
    end_date: datetime | None = Field(None, description="end_date parameter")
    height: int | None = Field(None, description="height parameter")
    locale: str | None = Field(None, description="locale parameter")
    place_page_id: int | None = Field(None, description="place_page_id parameter")
    post: dict[str, Any] | None = Field(None, description="post parameter")
    product_item_ids: list[str] | None = Field(None, description="product_item_ids parameter")
    render_type: adcreativepreviews_render_type_enum_param | None = Field(
        None, description="render_type parameter"
    )
    start_date: datetime | None = Field(None, description="start_date parameter")
    width: int | None = Field(None, description="width parameter")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .igcomment import IGCommentFields
    from .igmedia import IGMediaFields


class shadowiguserupcoming_events_notification_subtypes_enum_param(str, Enum):
    """shadowiguserupcoming_events_notification_subtypes_enum_param enum values."""

    AFTER_EVENT_1DAY = "AFTER_EVENT_1DAY"
    AFTER_EVENT_2DAY = "AFTER_EVENT_2DAY"
    AFTER_EVENT_3DAY = "AFTER_EVENT_3DAY"
    AFTER_EVENT_4DAY = "AFTER_EVENT_4DAY"
    AFTER_EVENT_5DAY = "AFTER_EVENT_5DAY"
    AFTER_EVENT_6DAY = "AFTER_EVENT_6DAY"
    AFTER_EVENT_7DAY = "AFTER_EVENT_7DAY"
    BEFORE_EVENT_15MIN = "BEFORE_EVENT_15MIN"
    BEFORE_EVENT_1DAY = "BEFORE_EVENT_1DAY"
    BEFORE_EVENT_1HOUR = "BEFORE_EVENT_1HOUR"
    BEFORE_EVENT_2DAY = "BEFORE_EVENT_2DAY"
    EVENT_START = "EVENT_START"
    RESCHEDULED = "RESCHEDULED"


class shadowiguserinsights_timeframe_enum_param(str, Enum):
    """shadowiguserinsights_timeframe_enum_param enum values."""

    last_14_days = "last_14_days"
    last_30_days = "last_30_days"
    last_90_days = "last_90_days"
    prev_month = "prev_month"
    this_month = "this_month"
    this_week = "this_week"


class shadowiguserinsights_period_enum_param(str, Enum):
    """shadowiguserinsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class shadowiguserinsights_metric_type_enum_param(str, Enum):
    """shadowiguserinsights_metric_type_enum_param enum values."""

    default = "default"
    time_series = "time_series"
    total_value = "total_value"


class shadowiguserinsights_metric_enum_param(str, Enum):
    """shadowiguserinsights_metric_enum_param enum values."""

    accounts_engaged = "accounts_engaged"
    comments = "comments"
    content_views = "content_views"
    engaged_audience_demographics = "engaged_audience_demographics"
    follower_count = "follower_count"
    follower_demographics = "follower_demographics"
    follows_and_unfollows = "follows_and_unfollows"
    impressions = "impressions"
    likes = "likes"
    online_followers = "online_followers"
    profile_links_taps = "profile_links_taps"
    profile_views = "profile_views"
    quotes = "quotes"
    reach = "reach"
    reached_audience_demographics = "reached_audience_demographics"
    replies = "replies"
    reposts = "reposts"
    saves = "saves"
    shares = "shares"
    threads_follower_demographics = "threads_follower_demographics"
    threads_followers = "threads_followers"
    threads_likes = "threads_likes"
    threads_replies = "threads_replies"
    threads_views = "threads_views"
    total_interactions = "total_interactions"
    views = "views"
    website_clicks = "website_clicks"


class shadowiguserinsights_breakdown_enum_param(str, Enum):
    """shadowiguserinsights_breakdown_enum_param enum values."""

    age = "age"
    city = "city"
    contact_button_type = "contact_button_type"
    country = "country"
    follow_type = "follow_type"
    gender = "gender"
    media_product_type = "media_product_type"


# Field literal type
IGUserField = Literal[
    "biography",
    "business_discovery",
    "followers_count",
    "follows_count",
    "has_profile_pic",
    "id",
    "ig_id",
    "is_published",
    "legacy_instagram_user_id",
    "media_count",
    "mentioned_comment",
    "mentioned_media",
    "name",
    "owner_business",
    "profile_picture_url",
    "shopping_product_tag_eligibility",
    "shopping_review_status",
    "username",
    "website",
]


class IGUserFields(BaseModel):
    """Pydantic model for IGUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    biography: str = Field(None, alias="biography")
    business_discovery: IGUserFields = Field(None, alias="business_discovery")
    followers_count: int = Field(None, alias="followers_count")
    follows_count: int = Field(None, alias="follows_count")
    has_profile_pic: bool = Field(None, alias="has_profile_pic")
    id: str = Field(None, alias="id")
    ig_id: int = Field(None, alias="ig_id")
    is_published: bool = Field(None, alias="is_published")
    legacy_instagram_user_id: str = Field(None, alias="legacy_instagram_user_id")
    media_count: int = Field(None, alias="media_count")
    mentioned_comment: IGCommentFields = Field(None, alias="mentioned_comment")
    mentioned_media: IGMediaFields = Field(None, alias="mentioned_media")
    name: str = Field(None, alias="name")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    profile_picture_url: str = Field(None, alias="profile_picture_url")
    shopping_product_tag_eligibility: bool = Field(None, alias="shopping_product_tag_eligibility")
    shopping_review_status: str = Field(None, alias="shopping_review_status")
    username: str = Field(None, alias="username")
    website: str = Field(None, alias="website")


class IGUserGetAuthorizedAdaccountsParams(BaseModel):
    """Parameters for IGUser.get_authorized_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class IGUserCreateAuthorizedAdaccountParams(BaseModel):
    """Parameters for IGUser.create_authorized_adaccount()."""

    model_config = ConfigDict(extra="forbid")
    account_id: str | None = Field(None, description="account_id parameter")
    business: str | None = Field(None, description="business parameter")


class IGUserCreateBrandedContentAdPermissionParams(BaseModel):
    """Parameters for IGUser.create_branded_content_ad_permission()."""

    model_config = ConfigDict(extra="forbid")
    creator_instagram_account: str | None = Field(
        None, description="creator_instagram_account parameter"
    )
    creator_instagram_username: str | None = Field(
        None, description="creator_instagram_username parameter"
    )
    revoke: bool | None = Field(None, description="revoke parameter")


class IGUserGetBrandedContentAdvertisableMediasParams(BaseModel):
    """Parameters for IGUser.get_branded_content_advertisable_medias()."""

    model_config = ConfigDict(extra="forbid")
    ad_code: str | None = Field(None, description="ad_code parameter")
    creator_username: str | None = Field(None, description="creator_username parameter")
    only_fetch_allowlisted: bool | None = Field(
        None, description="only_fetch_allowlisted parameter"
    )
    only_fetch_recommended_content: bool | None = Field(
        None, description="only_fetch_recommended_content parameter"
    )
    permalinks: list[str] | None = Field(None, description="permalinks parameter")


class IGUserDeleteBrandedContentTagApprovalParams(BaseModel):
    """Parameters for IGUser.delete_branded_content_tag_approval()."""

    model_config = ConfigDict(extra="forbid")
    user_ids: list[int] | None = Field(None, description="user_ids parameter")


class IGUserGetBrandedContentTagApprovalParams(BaseModel):
    """Parameters for IGUser.get_branded_content_tag_approval()."""

    model_config = ConfigDict(extra="forbid")
    user_ids: list[int] | None = Field(None, description="user_ids parameter")


class IGUserCreateBrandedContentTagApprovalParams(BaseModel):
    """Parameters for IGUser.create_branded_content_tag_approval()."""

    model_config = ConfigDict(extra="forbid")
    user_ids: list[int] | None = Field(None, description="user_ids parameter")


class IGUserGetCatalogProductSearchParams(BaseModel):
    """Parameters for IGUser.get_catalog_product_search()."""

    model_config = ConfigDict(extra="forbid")
    catalog_id: str | None = Field(None, description="catalog_id parameter")
    q: str | None = Field(None, description="q parameter")


class IGUserGetContentPublishingLimitParams(BaseModel):
    """Parameters for IGUser.get_content_publishing_limit()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")


class IGUserCreateDatasetParams(BaseModel):
    """Parameters for IGUser.create_dataset()."""

    model_config = ConfigDict(extra="forbid")
    dataset_name: str | None = Field(None, description="dataset_name parameter")


class IGUserGetInsightsParams(BaseModel):
    """Parameters for IGUser.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    breakdown: list[shadowiguserinsights_breakdown_enum_param] | None = Field(
        None, description="breakdown parameter"
    )
    metric: list[shadowiguserinsights_metric_enum_param] | None = Field(
        None, description="metric parameter"
    )
    metric_type: shadowiguserinsights_metric_type_enum_param | None = Field(
        None, description="metric_type parameter"
    )
    period: list[shadowiguserinsights_period_enum_param] | None = Field(
        None, description="period parameter"
    )
    since: datetime | None = Field(None, description="since parameter")
    timeframe: shadowiguserinsights_timeframe_enum_param | None = Field(
        None, description="timeframe parameter"
    )
    until: datetime | None = Field(None, description="until parameter")


class IGUserGetLiveMediaParams(BaseModel):
    """Parameters for IGUser.get_live_media()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class IGUserGetMediaParams(BaseModel):
    """Parameters for IGUser.get_media()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class IGUserCreateMediaParams(BaseModel):
    """Parameters for IGUser.create_media()."""

    model_config = ConfigDict(extra="forbid")
    alt_text: str | None = Field(None, description="alt_text parameter")
    audio_name: str | None = Field(None, description="audio_name parameter")
    caption: str | None = Field(None, description="caption parameter")
    children: list[str] | None = Field(None, description="children parameter")
    collaborators: list[str] | None = Field(None, description="collaborators parameter")
    cover_url: str | None = Field(None, description="cover_url parameter")
    image_url: str | None = Field(None, description="image_url parameter")
    is_carousel_item: bool | None = Field(None, description="is_carousel_item parameter")
    location_id: str | None = Field(None, description="location_id parameter")
    media_type: str | None = Field(None, description="media_type parameter")
    product_tags: list[dict[str, Any]] | None = Field(None, description="product_tags parameter")
    share_to_feed: bool | None = Field(None, description="share_to_feed parameter")
    thumb_offset: str | None = Field(None, description="thumb_offset parameter")
    upload_type: str | None = Field(None, description="upload_type parameter")
    user_tags: list[dict[str, Any]] | None = Field(None, description="user_tags parameter")
    video_url: str | None = Field(None, description="video_url parameter")


class IGUserCreateMediaPublishParams(BaseModel):
    """Parameters for IGUser.create_media_publish()."""

    model_config = ConfigDict(extra="forbid")
    creation_id: int | None = Field(None, description="creation_id parameter")


class IGUserCreateMentionParams(BaseModel):
    """Parameters for IGUser.create_mention()."""

    model_config = ConfigDict(extra="forbid")
    comment_id: str | None = Field(None, description="comment_id parameter")
    media_id: str | None = Field(None, description="media_id parameter")
    message: str | None = Field(None, description="message parameter")


class IGUserGetProductAppealParams(BaseModel):
    """Parameters for IGUser.get_product_appeal()."""

    model_config = ConfigDict(extra="forbid")
    product_id: str | None = Field(None, description="product_id parameter")


class IGUserCreateProductAppealParams(BaseModel):
    """Parameters for IGUser.create_product_appeal()."""

    model_config = ConfigDict(extra="forbid")
    appeal_reason: str | None = Field(None, description="appeal_reason parameter")
    product_id: str | None = Field(None, description="product_id parameter")


class IGUserCreateUpcomingEventParams(BaseModel):
    """Parameters for IGUser.create_upcoming_event()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    notification_subtypes: (
        list[shadowiguserupcoming_events_notification_subtypes_enum_param] | None
    ) = Field(None, description="notification_subtypes parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
    title: str | None = Field(None, description="title parameter")


class IGUserGetWelcomeMessageFlowsParams(BaseModel):
    """Parameters for IGUser.get_welcome_message_flows()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    flow_id: str | None = Field(None, description="flow_id parameter")

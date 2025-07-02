"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class userinsights_metric_enum_param(str, Enum):
    """userinsights_metric_enum_param enum values."""

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


class userconversations_platform_enum_param(str, Enum):
    """userconversations_platform_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"


class iggraphusermessages_messaging_type_enum_param(str, Enum):
    """iggraphusermessages_messaging_type_enum_param enum values."""

    MESSAGE_TAG = "MESSAGE_TAG"
    RESPONSE = "RESPONSE"
    UPDATE = "UPDATE"
    UTILITY = "UTILITY"


class iggraphusermessenger_profile_fields_enum_param(str, Enum):
    """iggraphusermessenger_profile_fields_enum_param enum values."""

    ACCOUNT_LINKING_URL = "ACCOUNT_LINKING_URL"
    COMMANDS = "COMMANDS"
    DESCRIPTION = "DESCRIPTION"
    GET_STARTED = "GET_STARTED"
    GREETING = "GREETING"
    HOME_URL = "HOME_URL"
    ICE_BREAKERS = "ICE_BREAKERS"
    PERSISTENT_MENU = "PERSISTENT_MENU"
    PLATFORM = "PLATFORM"
    SUBJECT_TO_NEW_EU_PRIVACY_RULES = "SUBJECT_TO_NEW_EU_PRIVACY_RULES"
    TITLE = "TITLE"
    WHITELISTED_DOMAINS = "WHITELISTED_DOMAINS"


class userinsights_period_enum_param(str, Enum):
    """userinsights_period_enum_param enum values."""

    day = "day"
    days_28 = "days_28"
    lifetime = "lifetime"
    month = "month"
    total_over_range = "total_over_range"
    week = "week"


class iggraphusersubscribed_apps_subscribed_fields_enum_param(str, Enum):
    """iggraphusersubscribed_apps_subscribed_fields_enum_param enum values."""

    comment_poll_response = "comment_poll_response"
    comments = "comments"
    creator_marketplace_invited_creator_onboarding = (
        "creator_marketplace_invited_creator_onboarding"
    )
    creator_marketplace_projects = "creator_marketplace_projects"
    delta = "delta"
    follow = "follow"
    live_comments = "live_comments"
    mentions = "mentions"
    message_reactions = "message_reactions"
    messages = "messages"
    messaging_handover = "messaging_handover"
    messaging_optins = "messaging_optins"
    messaging_postbacks = "messaging_postbacks"
    messaging_referral = "messaging_referral"
    messaging_seen = "messaging_seen"
    onboarding_welcome_message_series = "onboarding_welcome_message_series"
    standby = "standby"
    story_insights = "story_insights"
    story_poll_response = "story_poll_response"
    story_reactions = "story_reactions"
    story_share = "story_share"


class userinsights_breakdown_enum_param(str, Enum):
    """userinsights_breakdown_enum_param enum values."""

    age = "age"
    city = "city"
    contact_button_type = "contact_button_type"
    country = "country"
    follow_type = "follow_type"
    gender = "gender"
    media_product_type = "media_product_type"


class iggraphuserwelcome_message_flows_eligible_platforms_enum_param(str, Enum):
    """iggraphuserwelcome_message_flows_eligible_platforms_enum_param enum values."""

    INSTAGRAM = "INSTAGRAM"
    MESSENGER = "MESSENGER"
    WHATSAPP = "WHATSAPP"


class userinsights_metric_type_enum_param(str, Enum):
    """userinsights_metric_type_enum_param enum values."""

    default = "default"
    time_series = "time_series"
    total_value = "total_value"


class iggraphusermessages_sender_action_enum_param(str, Enum):
    """iggraphusermessages_sender_action_enum_param enum values."""

    MARK_SEEN = "MARK_SEEN"
    REACT = "REACT"
    TYPING_OFF = "TYPING_OFF"
    TYPING_ON = "TYPING_ON"
    UNREACT = "UNREACT"


class userinsights_timeframe_enum_param(str, Enum):
    """userinsights_timeframe_enum_param enum values."""

    last_14_days = "last_14_days"
    last_30_days = "last_30_days"
    last_90_days = "last_90_days"
    prev_month = "prev_month"
    this_month = "this_month"
    this_week = "this_week"


# Field literal type
IGUserForIGOnlyAPIField = Literal[
    "account_type",
    "biography",
    "followers_count",
    "follows_count",
    "id",
    "media_count",
    "name",
    "profile_picture_url",
    "user_id",
    "username",
    "website",
]


class IGUserForIGOnlyAPIFields(BaseModel):
    """Pydantic model for IGUserForIGOnlyAPI fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_type: str = Field(None, alias="account_type")
    biography: str = Field(None, alias="biography")
    followers_count: int = Field(None, alias="followers_count")
    follows_count: int = Field(None, alias="follows_count")
    id: str = Field(None, alias="id")
    media_count: int = Field(None, alias="media_count")
    name: str = Field(None, alias="name")
    profile_picture_url: str = Field(None, alias="profile_picture_url")
    user_id: int = Field(None, alias="user_id")
    username: str = Field(None, alias="username")
    website: str = Field(None, alias="website")


class IGUserForIGOnlyAPIGetBusinessMessagingFeatureStatusParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.get_business_messaging_feature_status()."""

    model_config = ConfigDict(extra="forbid")
    feature: str | None = Field(None, description="feature parameter")


class IGUserForIGOnlyAPIGetContentPublishingLimitParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.get_content_publishing_limit()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")


class IGUserForIGOnlyAPIGetConversationsParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.get_conversations()."""

    model_config = ConfigDict(extra="forbid")
    folder: str | None = Field(None, description="folder parameter")
    platform: userconversations_platform_enum_param | None = Field(
        None, description="platform parameter"
    )
    tags: list[str] | None = Field(None, description="tags parameter")
    user_id: str | None = Field(None, description="user_id parameter")


class IGUserForIGOnlyAPIGetInsightsParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.get_insights()."""

    model_config = ConfigDict(extra="forbid")
    breakdown: list[userinsights_breakdown_enum_param] | None = Field(
        None, description="breakdown parameter"
    )
    metric: list[userinsights_metric_enum_param] | None = Field(
        None, description="metric parameter"
    )
    metric_type: userinsights_metric_type_enum_param | None = Field(
        None, description="metric_type parameter"
    )
    period: list[userinsights_period_enum_param] | None = Field(
        None, description="period parameter"
    )
    since: datetime | None = Field(None, description="since parameter")
    timeframe: userinsights_timeframe_enum_param | None = Field(
        None, description="timeframe parameter"
    )
    until: datetime | None = Field(None, description="until parameter")


class IGUserForIGOnlyAPIGetMediaParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.get_media()."""

    model_config = ConfigDict(extra="forbid")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class IGUserForIGOnlyAPICreateMediaParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_media()."""

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


class IGUserForIGOnlyAPICreateMediapublishParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_mediapublish()."""

    model_config = ConfigDict(extra="forbid")
    creation_id: int | None = Field(None, description="creation_id parameter")


class IGUserForIGOnlyAPICreateMentionParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_mention()."""

    model_config = ConfigDict(extra="forbid")
    comment_id: str | None = Field(None, description="comment_id parameter")
    media_id: str | None = Field(None, description="media_id parameter")
    message: str | None = Field(None, description="message parameter")


class IGUserForIGOnlyAPICreateMessageattachmentParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_messageattachment()."""

    model_config = ConfigDict(extra="forbid")
    message: dict[str, Any] | None = Field(None, description="message parameter")


class IGUserForIGOnlyAPICreateMessageParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_message()."""

    model_config = ConfigDict(extra="forbid")
    message: dict[str, Any] | None = Field(None, description="message parameter")
    messaging_type: iggraphusermessages_messaging_type_enum_param | None = Field(
        None, description="messaging_type parameter"
    )
    payload: str | None = Field(None, description="payload parameter")
    recipient: dict[str, Any] | None = Field(None, description="recipient parameter")
    sender_action: iggraphusermessages_sender_action_enum_param | None = Field(
        None, description="sender_action parameter"
    )
    tag: dict[str, Any] | None = Field(None, description="tag parameter")
    thread_control: dict[str, Any] | None = Field(None, description="thread_control parameter")


class IGUserForIGOnlyAPIDeleteMessengerProfileParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.delete_messenger_profile()."""

    model_config = ConfigDict(extra="forbid")
    fields: list[iggraphusermessenger_profile_fields_enum_param] | None = Field(
        None, description="fields parameter"
    )


class IGUserForIGOnlyAPICreateMessengerProfileParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_messenger_profile()."""

    model_config = ConfigDict(extra="forbid")
    ice_breakers: list[dict[str, Any]] | None = Field(None, description="ice_breakers parameter")
    persistent_menu: list[dict[str, Any]] | None = Field(
        None, description="persistent_menu parameter"
    )


class IGUserForIGOnlyAPICreateSubscribedAppParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_subscribed_app()."""

    model_config = ConfigDict(extra="forbid")
    subscribed_fields: list[iggraphusersubscribed_apps_subscribed_fields_enum_param] | None = Field(
        None, description="subscribed_fields parameter"
    )


class IGUserForIGOnlyAPIDeleteWelcomeMessageFlowsParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.delete_welcome_message_flows()."""

    model_config = ConfigDict(extra="forbid")
    flow_id: str | None = Field(None, description="flow_id parameter")


class IGUserForIGOnlyAPIGetWelcomeMessageFlowsParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.get_welcome_message_flows()."""

    model_config = ConfigDict(extra="forbid")
    app_id: str | None = Field(None, description="app_id parameter")
    flow_id: str | None = Field(None, description="flow_id parameter")


class IGUserForIGOnlyAPICreateWelcomeMessageFlowParams(BaseModel):
    """Parameters for IGUserForIGOnlyAPI.create_welcome_message_flow()."""

    model_config = ConfigDict(extra="forbid")
    eligible_platforms: (
        list[iggraphuserwelcome_message_flows_eligible_platforms_enum_param] | None
    ) = Field(None, description="eligible_platforms parameter")
    flow_id: str | None = Field(None, description="flow_id parameter")
    name: str | None = Field(None, description="name parameter")
    welcome_message_flow: list[dict[str, Any]] | None = Field(
        None, description="welcome_message_flow parameter"
    )

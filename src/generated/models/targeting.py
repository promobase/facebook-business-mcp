"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogbasedtargeting import CatalogBasedTargetingFields
    from .connectionstargeting import ConnectionsTargetingFields
    from .flexibletargeting import FlexibleTargetingFields
    from .idname import IDNameFields
    from .rawcustomaudience import RawCustomAudienceFields
    from .targetingautomation import TargetingAutomationFields
    from .targetingdynamicrule import TargetingDynamicRuleFields
    from .targetinggeolocation import TargetingGeoLocationFields
    from .targetingproductaudiencespec import TargetingProductAudienceSpecFields
    from .targetingprospectingaudience import TargetingProspectingAudienceFields
    from .targetingrelaxation import TargetingRelaxationFields


# Field literal type
TargetingField = Literal[
    "adgroup_id",
    "age_max",
    "age_min",
    "age_range",
    "alternate_auto_targeting_option",
    "app_install_state",
    "audience_network_positions",
    "behaviors",
    "brand_safety_content_filter_levels",
    "catalog_based_targeting",
    "cities",
    "college_years",
    "connections",
    "contextual_targeting_categories",
    "countries",
    "country",
    "country_groups",
    "custom_audiences",
    "device_platforms",
    "direct_install_devices",
    "dynamic_audience_ids",
    "education_majors",
    "education_schools",
    "education_statuses",
    "effective_audience_network_positions",
    "effective_device_platforms",
    "effective_facebook_positions",
    "effective_instagram_positions",
    "effective_messenger_positions",
    "effective_publisher_platforms",
    "effective_threads_positions",
    "engagement_specs",
    "ethnic_affinity",
    "exclude_reached_since",
    "excluded_brand_safety_content_types",
    "excluded_connections",
    "excluded_custom_audiences",
    "excluded_dynamic_audience_ids",
    "excluded_engagement_specs",
    "excluded_geo_locations",
    "excluded_mobile_device_model",
    "excluded_product_audience_specs",
    "excluded_publisher_categories",
    "excluded_publisher_list_ids",
    "excluded_user_device",
    "exclusions",
    "facebook_positions",
    "family_statuses",
    "fb_deal_id",
    "flexible_spec",
    "friends_of_connections",
    "genders",
    "generation",
    "geo_locations",
    "home_ownership",
    "home_type",
    "home_value",
    "household_composition",
    "income",
    "industries",
    "instagram_positions",
    "instream_video_skippable_excluded",
    "interested_in",
    "interests",
    "is_whatsapp_destination_ad",
    "keywords",
    "life_events",
    "locales",
    "messenger_positions",
    "moms",
    "net_worth",
    "office_type",
    "place_page_set_ids",
    "political_views",
    "politics",
    "product_audience_specs",
    "prospecting_audience",
    "publisher_platforms",
    "radius",
    "regions",
    "relationship_statuses",
    "site_category",
    "targeting_automation",
    "targeting_optimization",
    "targeting_relaxation_types",
    "threads_positions",
    "user_adclusters",
    "user_device",
    "user_event",
    "user_os",
    "wireless_carrier",
    "work_employers",
    "work_positions",
    "zips",
]


class TargetingFields(BaseModel):
    """Pydantic model for Targeting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adgroup_id: str = Field(None, alias="adgroup_id")
    age_max: int = Field(None, alias="age_max")
    age_min: int = Field(None, alias="age_min")
    age_range: list[int] = Field(None, alias="age_range")
    alternate_auto_targeting_option: str = Field(None, alias="alternate_auto_targeting_option")
    app_install_state: str = Field(None, alias="app_install_state")
    audience_network_positions: list[str] = Field(None, alias="audience_network_positions")
    behaviors: list[IDNameFields] = Field(None, alias="behaviors")
    brand_safety_content_filter_levels: list[str] = Field(
        None, alias="brand_safety_content_filter_levels"
    )
    catalog_based_targeting: CatalogBasedTargetingFields = Field(
        None, alias="catalog_based_targeting"
    )
    cities: list[IDNameFields] = Field(None, alias="cities")
    college_years: list[int] = Field(None, alias="college_years")
    connections: list[ConnectionsTargetingFields] = Field(None, alias="connections")
    contextual_targeting_categories: list[IDNameFields] = Field(
        None, alias="contextual_targeting_categories"
    )
    countries: list[str] = Field(None, alias="countries")
    country: list[str] = Field(None, alias="country")
    country_groups: list[str] = Field(None, alias="country_groups")
    custom_audiences: list[RawCustomAudienceFields] = Field(None, alias="custom_audiences")
    device_platforms: list[dict[str, Any]] = Field(None, alias="device_platforms")
    direct_install_devices: bool = Field(None, alias="direct_install_devices")
    dynamic_audience_ids: list[str] = Field(None, alias="dynamic_audience_ids")
    education_majors: list[IDNameFields] = Field(None, alias="education_majors")
    education_schools: list[IDNameFields] = Field(None, alias="education_schools")
    education_statuses: list[int] = Field(None, alias="education_statuses")
    effective_audience_network_positions: list[str] = Field(
        None, alias="effective_audience_network_positions"
    )
    effective_device_platforms: list[dict[str, Any]] = Field(
        None, alias="effective_device_platforms"
    )
    effective_facebook_positions: list[str] = Field(None, alias="effective_facebook_positions")
    effective_instagram_positions: list[str] = Field(None, alias="effective_instagram_positions")
    effective_messenger_positions: list[str] = Field(None, alias="effective_messenger_positions")
    effective_publisher_platforms: list[str] = Field(None, alias="effective_publisher_platforms")
    effective_threads_positions: list[str] = Field(None, alias="effective_threads_positions")
    engagement_specs: list[TargetingDynamicRuleFields] = Field(None, alias="engagement_specs")
    ethnic_affinity: list[IDNameFields] = Field(None, alias="ethnic_affinity")
    exclude_reached_since: list[str] = Field(None, alias="exclude_reached_since")
    excluded_brand_safety_content_types: list[str] = Field(
        None, alias="excluded_brand_safety_content_types"
    )
    excluded_connections: list[ConnectionsTargetingFields] = Field(
        None, alias="excluded_connections"
    )
    excluded_custom_audiences: list[RawCustomAudienceFields] = Field(
        None, alias="excluded_custom_audiences"
    )
    excluded_dynamic_audience_ids: list[str] = Field(None, alias="excluded_dynamic_audience_ids")
    excluded_engagement_specs: list[TargetingDynamicRuleFields] = Field(
        None, alias="excluded_engagement_specs"
    )
    excluded_geo_locations: TargetingGeoLocationFields = Field(None, alias="excluded_geo_locations")
    excluded_mobile_device_model: list[str] = Field(None, alias="excluded_mobile_device_model")
    excluded_product_audience_specs: list[TargetingProductAudienceSpecFields] = Field(
        None, alias="excluded_product_audience_specs"
    )
    excluded_publisher_categories: list[str] = Field(None, alias="excluded_publisher_categories")
    excluded_publisher_list_ids: list[str] = Field(None, alias="excluded_publisher_list_ids")
    excluded_user_device: list[str] = Field(None, alias="excluded_user_device")
    exclusions: FlexibleTargetingFields = Field(None, alias="exclusions")
    facebook_positions: list[str] = Field(None, alias="facebook_positions")
    family_statuses: list[IDNameFields] = Field(None, alias="family_statuses")
    fb_deal_id: str = Field(None, alias="fb_deal_id")
    flexible_spec: list[FlexibleTargetingFields] = Field(None, alias="flexible_spec")
    friends_of_connections: list[ConnectionsTargetingFields] = Field(
        None, alias="friends_of_connections"
    )
    genders: list[int] = Field(None, alias="genders")
    generation: list[IDNameFields] = Field(None, alias="generation")
    geo_locations: TargetingGeoLocationFields = Field(None, alias="geo_locations")
    home_ownership: list[IDNameFields] = Field(None, alias="home_ownership")
    home_type: list[IDNameFields] = Field(None, alias="home_type")
    home_value: list[IDNameFields] = Field(None, alias="home_value")
    household_composition: list[IDNameFields] = Field(None, alias="household_composition")
    income: list[IDNameFields] = Field(None, alias="income")
    industries: list[IDNameFields] = Field(None, alias="industries")
    instagram_positions: list[str] = Field(None, alias="instagram_positions")
    instream_video_skippable_excluded: bool = Field(None, alias="instream_video_skippable_excluded")
    interested_in: list[int] = Field(None, alias="interested_in")
    interests: list[IDNameFields] = Field(None, alias="interests")
    is_whatsapp_destination_ad: bool = Field(None, alias="is_whatsapp_destination_ad")
    keywords: list[str] = Field(None, alias="keywords")
    life_events: list[IDNameFields] = Field(None, alias="life_events")
    locales: list[int] = Field(None, alias="locales")
    messenger_positions: list[str] = Field(None, alias="messenger_positions")
    moms: list[IDNameFields] = Field(None, alias="moms")
    net_worth: list[IDNameFields] = Field(None, alias="net_worth")
    office_type: list[IDNameFields] = Field(None, alias="office_type")
    place_page_set_ids: list[str] = Field(None, alias="place_page_set_ids")
    political_views: list[int] = Field(None, alias="political_views")
    politics: list[IDNameFields] = Field(None, alias="politics")
    product_audience_specs: list[TargetingProductAudienceSpecFields] = Field(
        None, alias="product_audience_specs"
    )
    prospecting_audience: TargetingProspectingAudienceFields = Field(
        None, alias="prospecting_audience"
    )
    publisher_platforms: list[str] = Field(None, alias="publisher_platforms")
    radius: str = Field(None, alias="radius")
    regions: list[IDNameFields] = Field(None, alias="regions")
    relationship_statuses: list[int] = Field(None, alias="relationship_statuses")
    site_category: list[str] = Field(None, alias="site_category")
    targeting_automation: TargetingAutomationFields = Field(None, alias="targeting_automation")
    targeting_optimization: str = Field(None, alias="targeting_optimization")
    targeting_relaxation_types: TargetingRelaxationFields = Field(
        None, alias="targeting_relaxation_types"
    )
    threads_positions: list[str] = Field(None, alias="threads_positions")
    user_adclusters: list[IDNameFields] = Field(None, alias="user_adclusters")
    user_device: list[str] = Field(None, alias="user_device")
    user_event: list[int] = Field(None, alias="user_event")
    user_os: list[str] = Field(None, alias="user_os")
    wireless_carrier: list[str] = Field(None, alias="wireless_carrier")
    work_employers: list[IDNameFields] = Field(None, alias="work_employers")
    work_positions: list[IDNameFields] = Field(None, alias="work_positions")
    zips: list[str] = Field(None, alias="zips")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .reachfrequencyactivity import ReachFrequencyActivityFields
    from .reachfrequencyadformat import ReachFrequencyAdFormatFields
    from .reachfrequencydaypart import ReachFrequencyDayPartFields
    from .reachfrequencyestimatescurve import ReachFrequencyEstimatesCurveFields
    from .reachfrequencyestimatesplacementbreakdown import (
        ReachFrequencyEstimatesPlacementBreakdownFields,
    )
    from .targeting import TargetingFields


# Field literal type
ReachFrequencyPredictionField = Literal[
    "account_id",
    "activity_status",
    "ad_formats",
    "auction_entry_option_index",
    "audience_size_lower_bound",
    "audience_size_upper_bound",
    "business_id",
    "buying_type",
    "campaign_group_id",
    "campaign_id",
    "campaign_time_start",
    "campaign_time_stop",
    "currency",
    "curve_budget_reach",
    "curve_reach",
    "daily_grp_curve",
    "daily_impression_curve",
    "daily_impression_curve_map",
    "day_parting_schedule",
    "destination_id",
    "end_time",
    "expiration_time",
    "external_budget",
    "external_impression",
    "external_maximum_budget",
    "external_maximum_impression",
    "external_maximum_reach",
    "external_minimum_budget",
    "external_minimum_impression",
    "external_minimum_reach",
    "external_reach",
    "feed_ratio_0000",
    "frequency_cap",
    "frequency_distribution_map",
    "frequency_distribution_map_agg",
    "grp_audience_size",
    "grp_avg_probability_map",
    "grp_country_audience_size",
    "grp_curve",
    "grp_dmas_audience_size",
    "grp_filtering_threshold_00",
    "grp_points",
    "grp_ratio",
    "grp_reach_ratio",
    "grp_status",
    "holdout_percentage",
    "id",
    "impression_curve",
    "instagram_destination_id",
    "instream_packages",
    "interval_frequency_cap",
    "interval_frequency_cap_reset_period",
    "is_balanced_frequency",
    "is_bonus_media",
    "is_conversion_goal",
    "is_higher_average_frequency",
    "is_io",
    "is_reserved_buying",
    "is_trp",
    "name",
    "objective",
    "objective_name",
    "odax_objective",
    "odax_objective_name",
    "optimization_goal",
    "optimization_goal_name",
    "pause_periods",
    "percent_reach_at_target_frequency",
    "placement_breakdown",
    "placement_breakdown_map",
    "plan_name",
    "plan_type",
    "prediction_mode",
    "prediction_progress",
    "reference_id",
    "reservation_status",
    "start_time",
    "status",
    "story_event_type",
    "target_cpm",
    "target_frequency",
    "target_frequency_reset_period",
    "target_spec",
    "time_created",
    "time_updated",
    "timezone_id",
    "timezone_name",
    "topline_id",
    "video_view_length_constraint",
    "viewtag",
]


class ReachFrequencyPredictionFields(BaseModel):
    """Pydantic model for ReachFrequencyPrediction fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: int = Field(None, alias="account_id")
    activity_status: ReachFrequencyActivityFields = Field(None, alias="activity_status")
    ad_formats: list[ReachFrequencyAdFormatFields] = Field(None, alias="ad_formats")
    auction_entry_option_index: int = Field(None, alias="auction_entry_option_index")
    audience_size_lower_bound: int = Field(None, alias="audience_size_lower_bound")
    audience_size_upper_bound: int = Field(None, alias="audience_size_upper_bound")
    business_id: int = Field(None, alias="business_id")
    buying_type: str = Field(None, alias="buying_type")
    campaign_group_id: int = Field(None, alias="campaign_group_id")
    campaign_id: str = Field(None, alias="campaign_id")
    campaign_time_start: datetime = Field(None, alias="campaign_time_start")
    campaign_time_stop: datetime = Field(None, alias="campaign_time_stop")
    currency: str = Field(None, alias="currency")
    curve_budget_reach: ReachFrequencyEstimatesCurveFields = Field(None, alias="curve_budget_reach")
    curve_reach: list[int] = Field(None, alias="curve_reach")
    daily_grp_curve: list[float] = Field(None, alias="daily_grp_curve")
    daily_impression_curve: list[float] = Field(None, alias="daily_impression_curve")
    daily_impression_curve_map: list[dict[int, list[float]]] = Field(
        None, alias="daily_impression_curve_map"
    )
    day_parting_schedule: list[ReachFrequencyDayPartFields] = Field(
        None, alias="day_parting_schedule"
    )
    destination_id: str = Field(None, alias="destination_id")
    end_time: datetime = Field(None, alias="end_time")
    expiration_time: datetime = Field(None, alias="expiration_time")
    external_budget: int = Field(None, alias="external_budget")
    external_impression: int = Field(None, alias="external_impression")
    external_maximum_budget: int = Field(None, alias="external_maximum_budget")
    external_maximum_impression: str = Field(None, alias="external_maximum_impression")
    external_maximum_reach: int = Field(None, alias="external_maximum_reach")
    external_minimum_budget: int = Field(None, alias="external_minimum_budget")
    external_minimum_impression: int = Field(None, alias="external_minimum_impression")
    external_minimum_reach: int = Field(None, alias="external_minimum_reach")
    external_reach: int = Field(None, alias="external_reach")
    feed_ratio_0000: int = Field(None, alias="feed_ratio_0000")
    frequency_cap: int = Field(None, alias="frequency_cap")
    frequency_distribution_map: list[dict[int, list[float]]] = Field(
        None, alias="frequency_distribution_map"
    )
    frequency_distribution_map_agg: list[dict[int, list[int]]] = Field(
        None, alias="frequency_distribution_map_agg"
    )
    grp_audience_size: float = Field(None, alias="grp_audience_size")
    grp_avg_probability_map: str = Field(None, alias="grp_avg_probability_map")
    grp_country_audience_size: float = Field(None, alias="grp_country_audience_size")
    grp_curve: list[float] = Field(None, alias="grp_curve")
    grp_dmas_audience_size: float = Field(None, alias="grp_dmas_audience_size")
    grp_filtering_threshold_00: int = Field(None, alias="grp_filtering_threshold_00")
    grp_points: float = Field(None, alias="grp_points")
    grp_ratio: float = Field(None, alias="grp_ratio")
    grp_reach_ratio: float = Field(None, alias="grp_reach_ratio")
    grp_status: str = Field(None, alias="grp_status")
    holdout_percentage: int = Field(None, alias="holdout_percentage")
    id: str = Field(None, alias="id")
    impression_curve: list[int] = Field(None, alias="impression_curve")
    instagram_destination_id: str = Field(None, alias="instagram_destination_id")
    instream_packages: list[str] = Field(None, alias="instream_packages")
    interval_frequency_cap: int = Field(None, alias="interval_frequency_cap")
    interval_frequency_cap_reset_period: int = Field(
        None, alias="interval_frequency_cap_reset_period"
    )
    is_balanced_frequency: bool = Field(None, alias="is_balanced_frequency")
    is_bonus_media: int = Field(None, alias="is_bonus_media")
    is_conversion_goal: int = Field(None, alias="is_conversion_goal")
    is_higher_average_frequency: bool = Field(None, alias="is_higher_average_frequency")
    is_io: bool = Field(None, alias="is_io")
    is_reserved_buying: int = Field(None, alias="is_reserved_buying")
    is_trp: bool = Field(None, alias="is_trp")
    name: str = Field(None, alias="name")
    objective: int = Field(None, alias="objective")
    objective_name: str = Field(None, alias="objective_name")
    odax_objective: int = Field(None, alias="odax_objective")
    odax_objective_name: str = Field(None, alias="odax_objective_name")
    optimization_goal: int = Field(None, alias="optimization_goal")
    optimization_goal_name: str = Field(None, alias="optimization_goal_name")
    pause_periods: list[dict[str, Any]] = Field(None, alias="pause_periods")
    percent_reach_at_target_frequency: int = Field(None, alias="percent_reach_at_target_frequency")
    placement_breakdown: ReachFrequencyEstimatesPlacementBreakdownFields = Field(
        None, alias="placement_breakdown"
    )
    placement_breakdown_map: list[dict[int, ReachFrequencyEstimatesPlacementBreakdownFields]] = (
        Field(None, alias="placement_breakdown_map")
    )
    plan_name: str = Field(None, alias="plan_name")
    plan_type: str = Field(None, alias="plan_type")
    prediction_mode: int = Field(None, alias="prediction_mode")
    prediction_progress: int = Field(None, alias="prediction_progress")
    reference_id: str = Field(None, alias="reference_id")
    reservation_status: int = Field(None, alias="reservation_status")
    start_time: datetime = Field(None, alias="start_time")
    status: int = Field(None, alias="status")
    story_event_type: int = Field(None, alias="story_event_type")
    target_cpm: int = Field(None, alias="target_cpm")
    target_frequency: int = Field(None, alias="target_frequency")
    target_frequency_reset_period: int = Field(None, alias="target_frequency_reset_period")
    target_spec: TargetingFields = Field(None, alias="target_spec")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")
    timezone_id: int = Field(None, alias="timezone_id")
    timezone_name: str = Field(None, alias="timezone_name")
    topline_id: int = Field(None, alias="topline_id")
    video_view_length_constraint: int = Field(None, alias="video_view_length_constraint")
    viewtag: str = Field(None, alias="viewtag")

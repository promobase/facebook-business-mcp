"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .targetinggeolocationcity import TargetingGeoLocationCityFields
    from .targetinggeolocationcustomlocation import TargetingGeoLocationCustomLocationFields
    from .targetinggeolocationmarket import TargetingGeoLocationMarketFields
    from .targetinggeolocationregion import TargetingGeoLocationRegionFields
    from .targetinggeolocationzip import TargetingGeoLocationZipFields


# Field literal type
AdSavedLocationField = Literal[
    "cities",
    "countries",
    "country_groups",
    "custom_locations",
    "geo_markets",
    "id",
    "location_sentences",
    "name",
    "regions",
    "zips",
]


class AdSavedLocationFields(BaseModel):
    """Pydantic model for AdSavedLocation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    cities: list[TargetingGeoLocationCityFields] = Field(None, alias="cities")
    countries: list[str] = Field(None, alias="countries")
    country_groups: list[str] = Field(None, alias="country_groups")
    custom_locations: list[TargetingGeoLocationCustomLocationFields] = Field(
        None, alias="custom_locations"
    )
    geo_markets: list[TargetingGeoLocationMarketFields] = Field(None, alias="geo_markets")
    id: str = Field(None, alias="id")
    location_sentences: list[str] = Field(None, alias="location_sentences")
    name: str = Field(None, alias="name")
    regions: list[TargetingGeoLocationRegionFields] = Field(None, alias="regions")
    zips: list[TargetingGeoLocationZipFields] = Field(None, alias="zips")

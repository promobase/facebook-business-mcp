"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .targetinggeolocationcity import TargetingGeoLocationCityFields
    from .targetinggeolocationcustomlocation import TargetingGeoLocationCustomLocationFields
    from .targetinggeolocationelectoraldistrict import TargetingGeoLocationElectoralDistrictFields
    from .targetinggeolocationgeoentities import TargetingGeoLocationGeoEntitiesFields
    from .targetinggeolocationlocationcluster import TargetingGeoLocationLocationClusterFields
    from .targetinggeolocationmarket import TargetingGeoLocationMarketFields
    from .targetinggeolocationplace import TargetingGeoLocationPlaceFields
    from .targetinggeolocationpoliticaldistrict import TargetingGeoLocationPoliticalDistrictFields
    from .targetinggeolocationregion import TargetingGeoLocationRegionFields
    from .targetinggeolocationzip import TargetingGeoLocationZipFields


# Field literal type
TargetingGeoLocationField = Literal[
    "cities",
    "countries",
    "country_groups",
    "custom_locations",
    "electoral_districts",
    "geo_markets",
    "large_geo_areas",
    "location_cluster_ids",
    "location_types",
    "medium_geo_areas",
    "metro_areas",
    "neighborhoods",
    "places",
    "political_districts",
    "regions",
    "small_geo_areas",
    "subcities",
    "subneighborhoods",
    "zips",
]


class TargetingGeoLocationFields(BaseModel):
    """Pydantic model for TargetingGeoLocation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    cities: list[TargetingGeoLocationCityFields] = Field(None, alias="cities")
    countries: list[str] = Field(None, alias="countries")
    country_groups: list[str] = Field(None, alias="country_groups")
    custom_locations: list[TargetingGeoLocationCustomLocationFields] = Field(
        None, alias="custom_locations"
    )
    electoral_districts: list[TargetingGeoLocationElectoralDistrictFields] = Field(
        None, alias="electoral_districts"
    )
    geo_markets: list[TargetingGeoLocationMarketFields] = Field(None, alias="geo_markets")
    large_geo_areas: list[TargetingGeoLocationGeoEntitiesFields] = Field(
        None, alias="large_geo_areas"
    )
    location_cluster_ids: list[TargetingGeoLocationLocationClusterFields] = Field(
        None, alias="location_cluster_ids"
    )
    location_types: list[str] = Field(None, alias="location_types")
    medium_geo_areas: list[TargetingGeoLocationGeoEntitiesFields] = Field(
        None, alias="medium_geo_areas"
    )
    metro_areas: list[TargetingGeoLocationGeoEntitiesFields] = Field(None, alias="metro_areas")
    neighborhoods: list[TargetingGeoLocationGeoEntitiesFields] = Field(None, alias="neighborhoods")
    places: list[TargetingGeoLocationPlaceFields] = Field(None, alias="places")
    political_districts: list[TargetingGeoLocationPoliticalDistrictFields] = Field(
        None, alias="political_districts"
    )
    regions: list[TargetingGeoLocationRegionFields] = Field(None, alias="regions")
    small_geo_areas: list[TargetingGeoLocationGeoEntitiesFields] = Field(
        None, alias="small_geo_areas"
    )
    subcities: list[TargetingGeoLocationGeoEntitiesFields] = Field(None, alias="subcities")
    subneighborhoods: list[TargetingGeoLocationGeoEntitiesFields] = Field(
        None, alias="subneighborhoods"
    )
    zips: list[TargetingGeoLocationZipFields] = Field(None, alias="zips")

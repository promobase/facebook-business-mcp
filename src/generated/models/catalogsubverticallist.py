"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogSubVerticalListField = Literal[
    "appliances",
    "baby_feeding",
    "baby_transport",
    "beauty",
    "bedding",
    "cameras",
    "cameras_and_photos",
    "cell_phones_and_smart_watches",
    "cleaning_supplies",
    "clo_offer",
    "clothing",
    "clothing_accessories",
    "computer_components",
    "computers_and_tablets",
    "computers_laptops_and_tablets",
    "diapering_and_potty_training",
    "electronic_accessories_and_cables",
    "electronics_accessories",
    "furniture",
    "health",
    "home",
    "home_goods",
    "household_and_cleaning_supplies",
    "jewelry",
    "large_appliances",
    "local_service_business_item",
    "local_service_business_restaurant",
    "loyalty_offer",
    "nursery",
    "printers_and_scanners",
    "printers_scanners_and_fax_machines",
    "product_discount",
    "projectors",
    "shoes",
    "shoes_and_footwear",
    "software",
    "televisions_and_monitors",
    "test_child_sub_vertical",
    "test_grand_child_sub_vertical",
    "test_sub_vertical",
    "test_sub_vertical_alias",
    "test_sub_vertical_data_object",
    "third_party_electronics",
    "third_party_toys_and_games",
    "toys",
    "toys_and_games",
    "tvs_and_monitors",
    "vehicle_manufacturer",
    "video_game_consoles_and_video_games",
    "video_games_and_consoles",
    "video_projectors",
    "watches",
]


class CatalogSubVerticalListFields(BaseModel):
    """Pydantic model for CatalogSubVerticalList fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    appliances: dict[str, Any] = Field(None, alias="appliances")
    baby_feeding: dict[str, Any] = Field(None, alias="baby_feeding")
    baby_transport: dict[str, Any] = Field(None, alias="baby_transport")
    beauty: dict[str, Any] = Field(None, alias="beauty")
    bedding: dict[str, Any] = Field(None, alias="bedding")
    cameras: dict[str, Any] = Field(None, alias="cameras")
    cameras_and_photos: dict[str, Any] = Field(None, alias="cameras_and_photos")
    cell_phones_and_smart_watches: dict[str, Any] = Field(
        None, alias="cell_phones_and_smart_watches"
    )
    cleaning_supplies: dict[str, Any] = Field(None, alias="cleaning_supplies")
    clo_offer: dict[str, Any] = Field(None, alias="clo_offer")
    clothing: dict[str, Any] = Field(None, alias="clothing")
    clothing_accessories: dict[str, Any] = Field(None, alias="clothing_accessories")
    computer_components: dict[str, Any] = Field(None, alias="computer_components")
    computers_and_tablets: dict[str, Any] = Field(None, alias="computers_and_tablets")
    computers_laptops_and_tablets: dict[str, Any] = Field(
        None, alias="computers_laptops_and_tablets"
    )
    diapering_and_potty_training: dict[str, Any] = Field(None, alias="diapering_and_potty_training")
    electronic_accessories_and_cables: dict[str, Any] = Field(
        None, alias="electronic_accessories_and_cables"
    )
    electronics_accessories: dict[str, Any] = Field(None, alias="electronics_accessories")
    furniture: dict[str, Any] = Field(None, alias="furniture")
    health: dict[str, Any] = Field(None, alias="health")
    home: dict[str, Any] = Field(None, alias="home")
    home_goods: dict[str, Any] = Field(None, alias="home_goods")
    household_and_cleaning_supplies: dict[str, Any] = Field(
        None, alias="household_and_cleaning_supplies"
    )
    jewelry: dict[str, Any] = Field(None, alias="jewelry")
    large_appliances: dict[str, Any] = Field(None, alias="large_appliances")
    local_service_business_item: dict[str, Any] = Field(None, alias="local_service_business_item")
    local_service_business_restaurant: dict[str, Any] = Field(
        None, alias="local_service_business_restaurant"
    )
    loyalty_offer: dict[str, Any] = Field(None, alias="loyalty_offer")
    nursery: dict[str, Any] = Field(None, alias="nursery")
    printers_and_scanners: dict[str, Any] = Field(None, alias="printers_and_scanners")
    printers_scanners_and_fax_machines: dict[str, Any] = Field(
        None, alias="printers_scanners_and_fax_machines"
    )
    product_discount: dict[str, Any] = Field(None, alias="product_discount")
    projectors: dict[str, Any] = Field(None, alias="projectors")
    shoes: dict[str, Any] = Field(None, alias="shoes")
    shoes_and_footwear: dict[str, Any] = Field(None, alias="shoes_and_footwear")
    software: dict[str, Any] = Field(None, alias="software")
    televisions_and_monitors: dict[str, Any] = Field(None, alias="televisions_and_monitors")
    test_child_sub_vertical: dict[str, Any] = Field(None, alias="test_child_sub_vertical")
    test_grand_child_sub_vertical: dict[str, Any] = Field(
        None, alias="test_grand_child_sub_vertical"
    )
    test_sub_vertical: dict[str, Any] = Field(None, alias="test_sub_vertical")
    test_sub_vertical_alias: dict[str, Any] = Field(None, alias="test_sub_vertical_alias")
    test_sub_vertical_data_object: dict[str, Any] = Field(
        None, alias="test_sub_vertical_data_object"
    )
    third_party_electronics: dict[str, Any] = Field(None, alias="third_party_electronics")
    third_party_toys_and_games: dict[str, Any] = Field(None, alias="third_party_toys_and_games")
    toys: dict[str, Any] = Field(None, alias="toys")
    toys_and_games: dict[str, Any] = Field(None, alias="toys_and_games")
    tvs_and_monitors: dict[str, Any] = Field(None, alias="tvs_and_monitors")
    vehicle_manufacturer: dict[str, Any] = Field(None, alias="vehicle_manufacturer")
    video_game_consoles_and_video_games: dict[str, Any] = Field(
        None, alias="video_game_consoles_and_video_games"
    )
    video_games_and_consoles: dict[str, Any] = Field(None, alias="video_games_and_consoles")
    video_projectors: dict[str, Any] = Field(None, alias="video_projectors")
    watches: dict[str, Any] = Field(None, alias="watches")

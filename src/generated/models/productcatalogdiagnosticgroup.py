"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ProductCatalogDiagnosticGroup_affected_entity(str, Enum):
    """ProductCatalogDiagnosticGroup_affected_entity enum values."""

    product_catalog = "product_catalog"
    product_event = "product_event"
    product_item = "product_item"
    product_set = "product_set"


class ProductCatalogDiagnosticGroup_severity(str, Enum):
    """ProductCatalogDiagnosticGroup_severity enum values."""

    MUST_FIX = "MUST_FIX"
    OPPORTUNITY = "OPPORTUNITY"


class ProductCatalogDiagnosticGroup_type(str, Enum):
    """ProductCatalogDiagnosticGroup_type enum values."""

    AR_VISIBILITY_ISSUES = "AR_VISIBILITY_ISSUES"
    ATTRIBUTES_INVALID = "ATTRIBUTES_INVALID"
    ATTRIBUTES_MISSING = "ATTRIBUTES_MISSING"
    CATEGORY = "CATEGORY"
    CHECKOUT = "CHECKOUT"
    DA_VISIBILITY_ISSUES = "DA_VISIBILITY_ISSUES"
    EVENT_SOURCE_ISSUES = "EVENT_SOURCE_ISSUES"
    IMAGE_QUALITY = "IMAGE_QUALITY"
    LOW_QUALITY_TITLE_AND_DESCRIPTION = "LOW_QUALITY_TITLE_AND_DESCRIPTION"
    POLICY_VIOLATION = "POLICY_VIOLATION"
    SHOPS_VISIBILITY_ISSUES = "SHOPS_VISIBILITY_ISSUES"


# Field literal type
ProductCatalogDiagnosticGroupField = Literal[
    "affected_channels",
    "affected_entity",
    "affected_features",
    "diagnostics",
    "error_code",
    "number_of_affected_entities",
    "number_of_affected_items",
    "severity",
    "subtitle",
    "title",
    "type",
]


class ProductCatalogDiagnosticGroupFields(BaseModel):
    """Pydantic model for ProductCatalogDiagnosticGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    affected_channels: list[str] = Field(None, alias="affected_channels")
    affected_entity: dict[str, Any] = Field(None, alias="affected_entity")
    affected_features: list[dict[str, Any]] = Field(None, alias="affected_features")
    diagnostics: list[dict[str, Any]] = Field(None, alias="diagnostics")
    error_code: int = Field(None, alias="error_code")
    number_of_affected_entities: int = Field(None, alias="number_of_affected_entities")
    number_of_affected_items: int = Field(None, alias="number_of_affected_items")
    severity: dict[str, Any] = Field(None, alias="severity")
    subtitle: str = Field(None, alias="subtitle")
    title: str = Field(None, alias="title")
    type: dict[str, Any] = Field(None, alias="type")

"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogDataSourceField = Literal[
    "app_id", "id", "ingestion_source_type", "name", "upload_type"
]


class ProductCatalogDataSourceFields(BaseModel):
    """Pydantic model for ProductCatalogDataSource fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: str = Field(None, alias="app_id")
    id: str = Field(None, alias="id")
    ingestion_source_type: str = Field(None, alias="ingestion_source_type")
    name: str = Field(None, alias="name")
    upload_type: str = Field(None, alias="upload_type")

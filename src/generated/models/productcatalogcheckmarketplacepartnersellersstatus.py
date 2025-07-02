"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductCatalogCheckMarketplacePartnerSellersStatusField = Literal[
    "sample_errors", "session_id", "status"
]


class ProductCatalogCheckMarketplacePartnerSellersStatusFields(BaseModel):
    """Pydantic model for ProductCatalogCheckMarketplacePartnerSellersStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    sample_errors: list[dict[str, Any]] = Field(None, alias="sample_errors")
    session_id: str = Field(None, alias="session_id")
    status: str = Field(None, alias="status")

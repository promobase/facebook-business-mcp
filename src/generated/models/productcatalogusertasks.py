"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
ProductCatalogUserTasksField = Literal["business", "tasks"]


class ProductCatalogUserTasksFields(BaseModel):
    """Pydantic model for ProductCatalogUserTasks fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    tasks: list[str] = Field(None, alias="tasks")

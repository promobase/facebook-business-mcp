"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .igvideocopyrightcheckstatus import IGVideoCopyrightCheckStatusFields


# Field literal type
IGVideoCopyrightCheckMatchesInformationField = Literal["copyright_matches", "status"]


class IGVideoCopyrightCheckMatchesInformationFields(BaseModel):
    """Pydantic model for IGVideoCopyrightCheckMatchesInformation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    copyright_matches: list[dict[str, Any]] = Field(None, alias="copyright_matches")
    status: IGVideoCopyrightCheckStatusFields = Field(None, alias="status")

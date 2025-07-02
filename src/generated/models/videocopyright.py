"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .copyrightreferencecontainer import CopyrightReferenceContainerFields
    from .user import UserFields
    from .videocopyrightgeogate import VideoCopyrightGeoGateFields
    from .videocopyrightrule import VideoCopyrightRuleFields
    from .videocopyrightsegment import VideoCopyrightSegmentFields


# Field literal type
VideoCopyrightField = Literal[
    "content_category",
    "copyright_content_id",
    "creator",
    "excluded_ownership_segments",
    "id",
    "in_conflict",
    "monitoring_status",
    "monitoring_type",
    "ownership_countries",
    "reference_file",
    "reference_file_disabled",
    "reference_file_disabled_by_ops",
    "reference_owner_id",
    "rule_ids",
    "tags",
    "whitelisted_ids",
]


class VideoCopyrightFields(BaseModel):
    """Pydantic model for VideoCopyright fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    content_category: str = Field(None, alias="content_category")
    copyright_content_id: str = Field(None, alias="copyright_content_id")
    creator: UserFields = Field(None, alias="creator")
    excluded_ownership_segments: list[VideoCopyrightSegmentFields] = Field(
        None, alias="excluded_ownership_segments"
    )
    id: str = Field(None, alias="id")
    in_conflict: bool = Field(None, alias="in_conflict")
    monitoring_status: str = Field(None, alias="monitoring_status")
    monitoring_type: str = Field(None, alias="monitoring_type")
    ownership_countries: VideoCopyrightGeoGateFields = Field(None, alias="ownership_countries")
    reference_file: CopyrightReferenceContainerFields = Field(None, alias="reference_file")
    reference_file_disabled: bool = Field(None, alias="reference_file_disabled")
    reference_file_disabled_by_ops: bool = Field(None, alias="reference_file_disabled_by_ops")
    reference_owner_id: str = Field(None, alias="reference_owner_id")
    rule_ids: list[VideoCopyrightRuleFields] = Field(None, alias="rule_ids")
    tags: list[str] = Field(None, alias="tags")
    whitelisted_ids: list[str] = Field(None, alias="whitelisted_ids")

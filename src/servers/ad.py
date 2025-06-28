"""Ad MCP Server using Facebook Business SDK."""

from typing import Any, TypedDict

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookError
from fastmcp import FastMCP

from ..config import extract_pagination_info


class AdResponse(TypedDict):
    success: bool
    data: dict[str, Any] | list[dict[str, Any]]


class PaginatedResponse(TypedDict):
    success: bool
    data: list[dict[str, Any]]
    pagination: dict[str, Any]


class ErrorResponse(TypedDict):
    error: str


class SuccessMessageResponse(TypedDict):
    success: bool
    message: str


# Field constants for better type safety and maintainability
class AdFields:
    """Ad field constants using SDK Field enums."""

    BASIC_FIELDS = [
        Ad.Field.id,
        Ad.Field.name,
        Ad.Field.status,
        Ad.Field.configured_status,
        Ad.Field.effective_status,
        Ad.Field.adset_id,
        Ad.Field.campaign_id,
        Ad.Field.account_id,
        Ad.Field.creative,
        Ad.Field.tracking_specs,
        Ad.Field.conversion_specs,
        Ad.Field.created_time,
        Ad.Field.updated_time,
        Ad.Field.bid_amount,
        Ad.Field.bid_type,
        Ad.Field.issues_info,
        Ad.Field.recommendations,
    ]

    DETAILED_FIELDS = BASIC_FIELDS + [
        Ad.Field.ad_review_feedback,
        Ad.Field.failed_delivery_checks,
        Ad.Field.targeting,
    ]

    UPDATE_FIELDS = [
        Ad.Field.id,
        Ad.Field.name,
        Ad.Field.status,
        Ad.Field.configured_status,
        Ad.Field.effective_status,
        Ad.Field.creative,
        Ad.Field.tracking_specs,
        Ad.Field.conversion_specs,
        Ad.Field.updated_time,
    ]


ad_server = FastMCP(
    name="FacebookAd",
    instructions="Facebook Ad management server providing tools for ad operations.",
)


@ad_server.tool
def get_adset_ads(
    adset_id: str, limit: int = 25, after: str | None = None
) -> PaginatedResponse | ErrorResponse:
    """Get ads for an ad set.

    Args:
        adset_id: Ad Set ID
        limit: Maximum number of ads to return (max 100)
        after: Pagination cursor for next page

    Returns:
        List of ads with comprehensive fields and pagination info
    """
    try:
        # Limit the maximum to 100 as per Facebook API limits
        limit = min(limit, 100)

        adset = AdSet(adset_id)
        params = {"limit": limit}
        if after:
            params["after"] = after

        ads_cursor = adset.get_ads(
            fields=AdFields.BASIC_FIELDS,
            params=params,
        )

        ads_list = [dict(ad) for ad in ads_cursor]
        pagination_info = extract_pagination_info(ads_cursor)

        return {"success": True, "data": ads_list, "pagination": pagination_info}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_server.tool
def get_ad(ad_id: str) -> AdResponse | ErrorResponse:
    """Get detailed ad information.

    Args:
        ad_id: Ad ID

    Returns:
        Detailed ad information
    """
    try:
        ad = Ad(ad_id)
        ad_data = ad.api_get(fields=AdFields.DETAILED_FIELDS)

        return {"success": True, "data": dict(ad_data)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_server.tool
def create_ad(
    adset_id: str,
    name: str,
    creative: dict[str, Any],
    status: str = Ad.ConfiguredStatus.paused,
    tracking_specs: list[dict[str, Any]] | None = None,
    conversion_specs: list[dict[str, Any]] | None = None,
) -> AdResponse | ErrorResponse:
    """Create a new ad.

    Args:
        adset_id: Ad Set ID
        name: Ad name
        creative: Creative specification
        status: Ad status (default: PAUSED)
        tracking_specs: Tracking specifications
        conversion_specs: Conversion specifications

    Returns:
        Created ad information
    """
    try:
        adset = AdSet(adset_id)

        params = {
            Ad.Field.name: name,
            Ad.Field.creative: creative,
            Ad.Field.configured_status: status,
        }

        if tracking_specs is not None:
            params[Ad.Field.tracking_specs] = tracking_specs
        if conversion_specs is not None:
            params[Ad.Field.conversion_specs] = conversion_specs

        ad = adset.create_ad(fields=[], params=params)

        return {"success": True, "data": dict(ad)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_server.tool
def update_ad(
    ad_id: str,
    name: str | None = None,
    status: str | None = None,
    creative: dict[str, Any] | None = None,
    tracking_specs: list[dict[str, Any]] | None = None,
    conversion_specs: list[dict[str, Any]] | None = None,
) -> AdResponse | ErrorResponse:
    """Update an existing ad.

    Args:
        ad_id: Ad ID
        name: New ad name
        status: New ad status
        creative: New creative specification
        tracking_specs: New tracking specifications
        conversion_specs: New conversion specifications

    Returns:
        Updated ad information
    """
    try:
        ad = Ad(ad_id)

        params = {}
        if name is not None:
            params[Ad.Field.name] = name
        if status is not None:
            params[Ad.Field.configured_status] = status
        if creative is not None:
            params[Ad.Field.creative] = creative
        if tracking_specs is not None:
            params[Ad.Field.tracking_specs] = tracking_specs
        if conversion_specs is not None:
            params[Ad.Field.conversion_specs] = conversion_specs

        if not params:
            return {"error": "No parameters provided for update"}

        ad.api_update(fields=[], params=params)

        # Get updated ad data
        updated_ad = ad.api_get(fields=AdFields.UPDATE_FIELDS)

        return {"success": True, "data": dict(updated_ad)}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_server.tool
def delete_ad(ad_id: str) -> SuccessMessageResponse | ErrorResponse:
    """Delete an ad.

    Args:
        ad_id: Ad ID

    Returns:
        Deletion confirmation
    """
    try:
        ad = Ad(ad_id)
        ad.api_delete()

        return {"success": True, "message": f"Ad {ad_id} deleted successfully"}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}


@ad_server.tool
def get_ad_preview(
    ad_id: str, ad_format: str = "DESKTOP_FEED_STANDARD"
) -> AdResponse | ErrorResponse:
    """Get ad preview.

    Args:
        ad_id: Ad ID
        ad_format: Ad format for preview

    Returns:
        Ad preview information
    """
    try:
        ad = Ad(ad_id)
        # Note: Preview fields don't have Field enums in the SDK, using strings as required
        previews = ad.get_previews(fields=["body", "image_url"], params={"ad_format": ad_format})

        previews_list = [dict(preview) for preview in previews]
        return {"success": True, "data": previews_list}

    except FacebookError as e:
        return {"error": f"Facebook API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

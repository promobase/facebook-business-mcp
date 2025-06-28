"""Configuration management for Facebook Business MCP Server."""

import os
from typing import Any

from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookError


def get_config_from_env() -> dict[str, Any]:
    """Get configuration from environment variables."""
    return {
        "app_id": os.getenv("FACEBOOK_APP_ID", ""),
        "app_secret": os.getenv("FACEBOOK_APP_SECRET", ""),
        "access_token": os.getenv("FACEBOOK_ACCESS_TOKEN", ""),
        "ad_account_id": os.getenv("FACEBOOK_AD_ACCOUNT_ID"),
        "api_version": os.getenv("FACEBOOK_API_VERSION", "v23.0"),
    }


def initialize_facebook_api(config: dict[str, Any] | None = None) -> dict[str, Any]:
    """Initialize Facebook API with configuration."""
    if config is None:
        config = get_config_from_env()

    if not config["app_id"] or not config["app_secret"] or not config["access_token"]:
        raise ValueError(
            "Missing required Facebook API credentials. "
            "Please set FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, and FACEBOOK_ACCESS_TOKEN environment variables."
        )

    FacebookAdsApi.init(
        app_id=config["app_id"],
        app_secret=config["app_secret"],
        access_token=config["access_token"],
        api_version=config["api_version"],
    )

    return config


def format_account_id(account_id: str) -> str:
    """Format account ID with 'act_' prefix if not present."""
    return f"act_{account_id}" if not account_id.startswith("act_") else account_id


def resolve_account_id(account_id: str | None = None) -> tuple[str, str | None]:
    """Resolve account ID from parameter or environment.

    Args:
        account_id: Optional account ID parameter

    Returns:
        Tuple of (resolved_account_id, error_message)
        If error_message is not None, resolved_account_id should be ignored
    """
    config = get_config_from_env()

    if account_id:
        return format_account_id(account_id), None

    if not config["ad_account_id"]:
        return "", "No ad account ID provided and none set in environment"

    return format_account_id(config["ad_account_id"]), None


def validate_facebook_connection() -> bool:
    """Validate Facebook API connection."""
    try:
        from facebook_business.adobjects.user import User

        api = FacebookAdsApi.get_default_api()
        user = User(fbid="me", api=api)
        user.api_get(fields=["id"])
        return True
    except FacebookError:
        return False
    except Exception:
        return False


def extract_pagination_info(cursor) -> dict[str, Any]:
    """Extract pagination information from a Facebook API cursor.

    Args:
        cursor: Facebook API cursor object

    Returns:
        Dictionary containing pagination information
    """
    pagination_info = {}

    if hasattr(cursor, "_finished_iteration") and not cursor._finished_iteration:
        if hasattr(cursor, "params") and "after" in cursor.params:
            pagination_info["next_cursor"] = cursor.params["after"]
            pagination_info["has_next_page"] = True
        else:
            pagination_info["has_next_page"] = False
    else:
        pagination_info["has_next_page"] = False

    # Add total count if available
    if hasattr(cursor, "_total_count") and cursor._total_count is not None:
        pagination_info["total_count"] = cursor._total_count

    return pagination_info

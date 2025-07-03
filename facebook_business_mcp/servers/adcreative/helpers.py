"""AdCreative helper operations.

This module provides helper functions for common ad creative creation patterns.
"""

from typing import Any

from facebook_business_mcp.generated.models import AdAccountCreateAdCreativeParams
from facebook_business_mcp.generated.models.generated_models import (
    AdCreative_call_to_action_type,
    AdCreativeLinkDataFields,
    AdCreativeObjectStorySpecFields,
)
from facebook_business_mcp.servers.adcreative.crud import adcreative_api_create
from facebook_business_mcp.utils import handle_facebook_errors


@handle_facebook_errors
def create_link_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    link_url: str,
    message: str,
    title: str = "",
    description: str = "",
    image_hash: str = "",
    call_to_action_type: AdCreative_call_to_action_type = AdCreative_call_to_action_type.LEARN_MORE,
    fields: list[str] = [],
) -> dict[str, Any]:
    """Create a link ad creative with common parameters.

    This is a helper function that simplifies creating link ad creatives.

    Args:
        account_id: The ad account ID
        name: Creative name
        page_id: Facebook page ID
        link_url: Destination URL
        message: Primary text
        title: Link title
        description: Link description
        image_hash: Image hash from uploaded image
        call_to_action_type: CTA button type
        fields: Fields to return

    Returns:
        Created ad creative data
    """
    # Build link_data with required fields
    link_data_dict: dict[str, Any] = {
        "link": link_url,
        "message": message,
    }

    # Add optional fields
    if title:
        link_data_dict["name"] = title
    if description:
        link_data_dict["description"] = description
    if image_hash:
        link_data_dict["image_hash"] = image_hash
    if call_to_action_type:
        link_data_dict["call_to_action"] = {"type": call_to_action_type.value}

    # Create the link data model
    link_data = AdCreativeLinkDataFields(**link_data_dict)

    # Create object story spec
    object_story_spec = AdCreativeObjectStorySpecFields(
        page_id=page_id,
        link_data=link_data,
    )

    # Create the params model
    params = AdAccountCreateAdCreativeParams(
        name=name,
        object_story_spec=object_story_spec,
    )

    # Convert to dict for SDK
    params_dict = params.model_dump(exclude_none=True)

    return adcreative_api_create(account_id, params_dict, fields)


@handle_facebook_errors
def create_video_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    video_id: str,
    message: str,
    title: str = "",
    description: str = "",
    call_to_action_type: AdCreative_call_to_action_type = AdCreative_call_to_action_type.LEARN_MORE,
    call_to_action_link: str = "",
    fields: list[str] = [],
) -> dict[str, Any]:
    """Create a video ad creative with common parameters.

    This is a helper function that simplifies creating video ad creatives.

    Args:
        account_id: The ad account ID
        name: Creative name
        page_id: Facebook page ID
        video_id: Video ID from uploaded video
        message: Primary text
        title: Video title
        description: Video description
        call_to_action_type: CTA button type
        call_to_action_link: CTA destination URL
        fields: Fields to return

    Returns:
        Created ad creative data
    """
    from facebook_business_mcp.generated.models.generated_models import (
        AdCreativeVideoDataFields,
    )

    # Build video_data with required fields
    video_data_dict: dict[str, Any] = {
        "video_id": video_id,
        "message": message,
    }

    # Add optional fields
    if title:
        video_data_dict["title"] = title
    if description:
        video_data_dict["description"] = description
    if call_to_action_type and call_to_action_link:
        video_data_dict["call_to_action"] = {
            "type": call_to_action_type.value,
            "value": {"link": call_to_action_link},
        }

    # Create the video data model
    video_data = AdCreativeVideoDataFields(**video_data_dict)

    # Create object story spec
    object_story_spec = AdCreativeObjectStorySpecFields(
        page_id=page_id,
        video_data=video_data,
    )

    # Create the params model
    params = AdAccountCreateAdCreativeParams(
        name=name,
        object_story_spec=object_story_spec,
    )

    # Convert to dict for SDK
    params_dict = params.model_dump(exclude_none=True)

    return adcreative_api_create(account_id, params_dict, fields)


@handle_facebook_errors
def create_carousel_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    link_url: str,
    message: str,
    child_attachments: list[dict[str, Any]],
    fields: list[str] = [],
) -> dict[str, Any]:
    """Create a carousel ad creative with multiple cards.

    This is a helper function that simplifies creating carousel ad creatives.

    Args:
        account_id: The ad account ID
        name: Creative name
        page_id: Facebook page ID
        link_url: Default destination URL
        message: Primary text
        child_attachments: List of carousel cards, each with:
            - name: Card title
            - description: Card description
            - image_hash: Image hash
            - link: Card-specific URL (optional)
        fields: Fields to return

    Returns:
        Created ad creative data
    """
    # Build link_data for carousel
    link_data = AdCreativeLinkDataFields(
        link=link_url,
        message=message,
        child_attachments=child_attachments,
    )

    # Create object story spec
    object_story_spec = AdCreativeObjectStorySpecFields(
        page_id=page_id,
        link_data=link_data,
    )

    # Create the params model
    params = AdAccountCreateAdCreativeParams(
        name=name,
        object_story_spec=object_story_spec,
    )

    # Convert to dict for SDK
    params_dict = params.model_dump(exclude_none=True)

    return adcreative_api_create(account_id, params_dict, fields)


@handle_facebook_errors
def create_dynamic_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    product_set_id: str,
    template_url_spec: dict[str, Any],
    message: str = "{{product.name}}",
    description: str = "{{product.description}}",
    fields: list[str] = [],
) -> dict[str, Any]:
    """Create a dynamic product ad creative.

    This is a helper function that simplifies creating dynamic product ad creatives.

    Args:
        account_id: The ad account ID
        name: Creative name
        page_id: Facebook page ID
        product_set_id: Product set ID from catalog
        template_url_spec: Template URL specification
        message: Message template (can use variables)
        description: Description template (can use variables)
        fields: Fields to return

    Returns:
        Created ad creative data
    """
    from facebook_business_mcp.generated.models.generated_models import (
        AdCreativeTemplateDataFields,
    )

    # Create template data
    template_data = AdCreativeTemplateDataFields(
        message=message,
        description=description,
        link="{{product.link}}",
    )

    # Create object story spec
    object_story_spec = AdCreativeObjectStorySpecFields(
        page_id=page_id,
        template_data=template_data,
    )

    # Create the params model
    params = AdAccountCreateAdCreativeParams(
        name=name,
        product_set_id=product_set_id,
        template_url_spec=template_url_spec,
        object_story_spec=object_story_spec,
    )

    # Convert to dict for SDK
    params_dict = params.model_dump(exclude_none=True)

    return adcreative_api_create(account_id, params_dict, fields)

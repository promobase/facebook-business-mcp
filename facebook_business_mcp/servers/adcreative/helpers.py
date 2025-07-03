"""AdCreative helper operations.

This module provides a collection of helper functions to simplify the creation
of common Facebook Ad Creative types. It aims to cover the most frequent
use cases, including single media, carousels, lead generation, dynamic ads,
and using existing page posts.
"""

from typing import Any, Optional

from facebook_business_mcp.generated.models import AdAccountCreateAdCreativeParams
from facebook_business_mcp.generated.models.generated_models import (
    AdCreative_call_to_action_type,
    AdCreativeLinkDataFields,
    AdCreativeObjectStorySpecFields,
    AdCreativeVideoDataFields,
)
from facebook_business_mcp.servers.adcreative.crud import adcreative_api_create
from facebook_business_mcp.utils import wrapped_fn_tool


@wrapped_fn_tool
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
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a link ad creative with common parameters (image or no image).

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        link_url: Destination URL.
        message: Primary text.
        title: Link title (headline).
        description: Link description.
        image_hash: Image hash from an uploaded image.
        call_to_action_type: CTA button type.
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    link_data_dict: dict[str, Any] = {"link": link_url, "message": message}

    if title:
        link_data_dict["name"] = title
    if description:
        link_data_dict["description"] = description
    if image_hash:
        link_data_dict["image_hash"] = image_hash
    if call_to_action_type:
        link_data_dict["call_to_action"] = {"type": call_to_action_type.value}

    link_data = AdCreativeLinkDataFields(**link_data_dict)
    object_story_spec = AdCreativeObjectStorySpecFields(page_id=page_id, link_data=link_data)
    params = AdAccountCreateAdCreativeParams(name=name, object_story_spec=object_story_spec)
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
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
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a video ad creative with common parameters.

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        video_id: Video ID from an uploaded video.
        message: Primary text.
        title: Video title.
        description: Video description.
        call_to_action_type: CTA button type.
        call_to_action_link: CTA destination URL.
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    video_data_dict: dict[str, Any] = {"video_id": video_id, "message": message}

    if title:
        video_data_dict["title"] = title
    if description:
        video_data_dict["description"] = description
    if call_to_action_type and call_to_action_link:
        video_data_dict["call_to_action"] = {
            "type": call_to_action_type.value,
            "value": {"link": call_to_action_link},
        }

    video_data = AdCreativeVideoDataFields(**video_data_dict)
    object_story_spec = AdCreativeObjectStorySpecFields(page_id=page_id, video_data=video_data)
    params = AdAccountCreateAdCreativeParams(name=name, object_story_spec=object_story_spec)
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
def create_carousel_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    link_url: str,
    message: str,
    child_attachments: list[dict[str, Any]],
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a carousel ad creative with multiple cards.

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        link_url: Default destination URL for the carousel.
        message: Primary text appearing above the carousel.
        child_attachments: A list of dictionaries, each representing a carousel card.
                           Each dict should contain 'name', 'description', 'image_hash',
                           and optionally 'link'.
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    link_data = AdCreativeLinkDataFields(
        link=link_url,
        message=message,
        child_attachments=child_attachments,
    )
    object_story_spec = AdCreativeObjectStorySpecFields(page_id=page_id, link_data=link_data)
    params = AdAccountCreateAdCreativeParams(name=name, object_story_spec=object_story_spec)
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
def create_ad_creative_from_post(
    account_id: str,
    name: str,
    page_post_id: str,
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create an ad creative from an existing page post (boosted post).

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_post_id: The ID of the existing page post (format: "pageid_postid").
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    params = AdAccountCreateAdCreativeParams(name=name, object_story_id=page_post_id)
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
def create_lead_gen_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    message: str,
    lead_gen_form_id: str,
    privacy_policy_url: str,
    image_hash: str,
    title: str = "",
    description: str = "",
    call_to_action_type: AdCreative_call_to_action_type = AdCreative_call_to_action_type.SUBSCRIBE,
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a lead generation ad creative using a Facebook Lead Form.

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        message: Primary text.
        lead_gen_form_id: The ID of the lead generation form.
        privacy_policy_url: The URL to the business's privacy policy.
        image_hash: Image hash from an uploaded image.
        title: Link title (headline).
        description: Link description.
        call_to_action_type: CTA button type (e.g., SUBSCRIBE, SIGN_UP).
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    link_data_dict: dict[str, Any] = {
        "link": privacy_policy_url,
        "message": message,
        "image_hash": image_hash,
        "lead_gen_form_id": lead_gen_form_id,
        "call_to_action": {"type": call_to_action_type.value},
    }
    if title:
        link_data_dict["name"] = title
    if description:
        link_data_dict["description"] = description

    link_data = AdCreativeLinkDataFields(**link_data_dict)
    object_story_spec = AdCreativeObjectStorySpecFields(page_id=page_id, link_data=link_data)
    params = AdAccountCreateAdCreativeParams(name=name, object_story_spec=object_story_spec)
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
def create_slideshow_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    image_urls: list[str],
    message: str,
    duration_ms: int = 2000,
    transition_ms: int = 200,
    title: str = "",
    description: str = "",
    call_to_action_type: AdCreative_call_to_action_type = AdCreative_call_to_action_type.LEARN_MORE,
    call_to_action_link: str = "",
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a slideshow ad creative from a list of images.

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        image_urls: List of URLs for the images in the slideshow.
        message: Primary text for the ad.
        duration_ms: Duration each image is shown in milliseconds.
        transition_ms: Duration of transition between images in milliseconds.
        title: Video title.
        description: Video description.
        call_to_action_type: CTA button type.
        call_to_action_link: CTA destination URL.
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    slideshow_spec = {
        "images_urls": image_urls,
        "duration_ms": duration_ms,
        "transition_ms": transition_ms,
    }
    video_data_dict: dict[str, Any] = {"message": message, "slideshow_spec": slideshow_spec}

    if title:
        video_data_dict["title"] = title
    if description:
        video_data_dict["description"] = description
    if call_to_action_type and call_to_action_link:
        video_data_dict["call_to_action"] = {
            "type": call_to_action_type.value,
            "value": {"link": call_to_action_link},
        }

    object_story_spec = AdCreativeObjectStorySpecFields(page_id=page_id, video_data=video_data_dict)
    params = AdAccountCreateAdCreativeParams(name=name, object_story_spec=object_story_spec)
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
def create_dynamic_product_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    product_set_id: str,
    link_url: str,
    message: str = "{{product.name}}",
    description: str = "{{product.description}}",
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a dynamic product ad creative using a product catalog.

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        product_set_id: Product set ID from the catalog.
        link_url: The base link for products, can use templates like {{product.link}}.
        message: Message template (can use variables like {{product.name}}).
        description: Description template (can use variables like {{product.description}}).
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    template_data = {
        "message": message,
        "description": description,
        "link": link_url,
    }
    object_story_spec = AdCreativeObjectStorySpecFields(
        page_id=page_id, template_data=template_data
    )
    params = AdAccountCreateAdCreativeParams(
        name=name,
        product_set_id=product_set_id,
        object_story_spec=object_story_spec,
    )
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)


@wrapped_fn_tool
def create_dynamic_asset_ad_creative(
    account_id: str,
    name: str,
    page_id: str,
    messages: Optional[list[str]] = None,
    titles: Optional[list[str]] = None,
    descriptions: Optional[list[str]] = None,
    image_hashes: Optional[list[str]] = None,
    video_ids: Optional[list[str]] = None,
    link_urls: Optional[list[str]] = None,
    call_to_action_types: Optional[list[AdCreative_call_to_action_type]] = None,
    fields: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Create a dynamic creative ad using an asset feed (DCO).

    This allows Facebook to automatically optimize combinations of assets.
    You must provide at least one asset type (e.g., images, videos, messages).

    Args:
        account_id: The ad account ID.
        name: Creative name.
        page_id: Facebook page ID.
        messages: List of primary texts (bodies).
        titles: List of headlines.
        descriptions: List of link descriptions.
        image_hashes: List of image hashes.
        video_ids: List of video IDs.
        link_urls: List of destination URLs.
        call_to_action_types: List of CTA button types.
        fields: Fields to return in the response.

    Returns:
        The created ad creative data.
    """
    fields = fields or []
    asset_feed_spec: dict[str, Any] = {}
    if messages:
        asset_feed_spec["bodies"] = [{"text": m} for m in messages]
    if titles:
        asset_feed_spec["titles"] = [{"text": t} for t in titles]
    if descriptions:
        asset_feed_spec["descriptions"] = [{"text": d} for d in descriptions]
    if image_hashes:
        asset_feed_spec["images"] = [{"hash": h} for h in image_hashes]
    if video_ids:
        asset_feed_spec["videos"] = [{"video_id": v} for v in video_ids]
    if link_urls:
        asset_feed_spec["link_urls"] = [{"website_url": u} for u in link_urls]
    if call_to_action_types:
        asset_feed_spec["call_to_action_types"] = [c.value for c in call_to_action_types]

    if not asset_feed_spec:
        raise ValueError("At least one asset type must be provided for dynamic creative.")

    object_story_spec = AdCreativeObjectStorySpecFields(page_id=page_id)
    params = AdAccountCreateAdCreativeParams(
        name=name,
        object_story_spec=object_story_spec,
        asset_feed_spec=asset_feed_spec,
    )
    params_dict = params.model_dump(exclude_none=True)
    return adcreative_api_create(account_id, params_dict, fields)

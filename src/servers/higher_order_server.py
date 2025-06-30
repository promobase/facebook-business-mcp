"""Higher Order Facebook Business MCP Server - Handles ANY Facebook Business SDK object dynamically."""

import importlib
import inspect
import pkgutil
import re
from functools import lru_cache
from typing import Any

from fastmcp import FastMCP

from src.utils import (
    handle_facebook_errors,
    list_callable_methods,
    log_execution,
    safe_getsource,
)


@lru_cache
def discover_adobjects() -> dict[str, str]:
    """Dynamically discover all Facebook Business SDK adobjects."""
    adobjects = {}
    ignore_patterns = [
        re.compile(r"^abstract.*"),
    ]

    try:
        # Import the adobjects package
        adobjects_package = importlib.import_module("facebook_business.adobjects")
        package_path = adobjects_package.__path__

        # Iterate through all modules in the adobjects package
        for _, module_name, _ in pkgutil.iter_modules(package_path):
            if module_name.startswith("_"):
                continue
            if any(pattern.match(module_name) for pattern in ignore_patterns):
                continue

            try:
                full_module_name = f"facebook_business.adobjects.{module_name}"
                module = importlib.import_module(full_module_name)

                # Find classes in the module that are likely adobjects
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    # Filter to only include classes defined in this module
                    if obj.__module__ == full_module_name:
                        # Check if it has common adobject attributes
                        if (
                            hasattr(obj, "_field_types")
                            or hasattr(obj, "Field")
                            or hasattr(obj, "api_get")
                        ):
                            adobjects[name] = full_module_name
            except Exception:
                # Skip modules that can't be imported
                continue

    except Exception:
        # If discovery fails, fall back to a basic set
        return {
            "AdAccount": "facebook_business.adobjects.adaccount",
            "Campaign": "facebook_business.adobjects.campaign",
            "AdSet": "facebook_business.adobjects.adset",
            "Ad": "facebook_business.adobjects.ad",
            "AdsInsights": "facebook_business.adobjects.adsinsights",
        }

    return adobjects


# Build the adobject map dynamically
ADOBJECT_MAP = discover_adobjects()

#  ---- constants ----
server_name = "HigherOrderFacebookBusinessMCPServer"
instructions = """
This is the Higher Order Facebook Business MCP Server that can handle ANY Facebook Business SDK object dynamically.

ALWAYS use the `list_available_adobjects` tool first to see what objects are available.
Then use `get_usage_on_adobject` to understand how to use a specific object.
Finally, use `run_any_adobject_method` to call any method on any object.

This server provides a universal interface to the entire Facebook Business SDK.
"""

higher_order_server = FastMCP(
    name=server_name,
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


def get_adobject_class(object_name: str):
    """Dynamically import and return the adobject class."""
    if object_name not in ADOBJECT_MAP:
        available = ", ".join(sorted(ADOBJECT_MAP.keys()))
        raise ValueError(f"Unknown adobject '{object_name}'. Available: {available}")

    module_path = ADOBJECT_MAP[object_name]
    module = importlib.import_module(module_path)
    return getattr(module, object_name)


@log_execution
@handle_facebook_errors
def list_available_adobjects() -> str:
    """List all available Facebook Business SDK objects that can be used."""
    objects = sorted(ADOBJECT_MAP.keys())
    return f"Found {len(objects)} Facebook Business SDK objects:\n" + "\n".join(
        f"- {name}" for name in objects
    )


@higher_order_server.prompt
@log_execution
@handle_facebook_errors
def get_usage_on_adobject(
    object_name: str,
    method_name: str | None = None,
) -> str:
    """Get usage information for any Facebook Business SDK object.

    Args:
        object_name: Name of the adobject (e.g., 'AdAccount', 'Campaign', 'Ad')
        method_name: Optional method name to get source code for
    """
    try:
        cls = get_adobject_class(object_name)
    except ValueError as e:
        return str(e)

    methods = list_callable_methods(cls)

    # Build usage info
    usage = f"""
    This is the {object_name} wrapper on Facebook Business Python SDK.
    You can use the run_any_adobject_method tool to call any methods.

    Available methods for {object_name}:
    {chr(10).join(f"- {m}" for m in methods)}
    """

    # Add field info if available
    if hasattr(cls, "_field_types"):
        usage += f"\n\nField types: {cls._field_types}"

    if hasattr(cls, "_get_field_enum_info"):
        try:
            field_enum_info = cls._get_field_enum_info()
            usage += f"\n\nField enum info: {field_enum_info}"
        except Exception:
            pass

    if method_name:
        if hasattr(cls, method_name):
            method = getattr(cls, method_name)
            if callable(method):
                usage += f"\n\nHere is the source code for {method_name}:\n{safe_getsource(method)}"
            else:
                usage += f"\n\n{method_name} is not a callable method on {object_name}."
        else:
            usage += f"\n\n{object_name} does not have method '{method_name}'."
    return usage


@log_execution
@handle_facebook_errors
def run_any_adobject_method(
    object_name: str,
    object_id: str,
    method_name: str,
    args: list[Any] = [],
    kwargs: dict[str, Any] = {},
) -> str:
    """Dynamically call any method on any Facebook Business SDK object.

    Args:
        object_name: Name of the adobject (e.g., 'AdAccount', 'Campaign', 'Ad')
        object_id: ID of the object instance (e.g., 'act_123', '123456')
        method_name: Method name to call
        args: Positional arguments for the method
        kwargs: Keyword arguments for the method (fields, params, etc.)

    Example:
        run_any_adobject_method("AdAccount", "act_123", "get_campaigns", kwargs={"fields": ["id", "name"], "params": {"limit": 10}})
    """
    try:
        cls = get_adobject_class(object_name)
    except ValueError as e:
        return str(e)

    # Create instance
    instance = cls(object_id)

    if not hasattr(instance, method_name):
        return f"{object_name} does not have method '{method_name}'. Use get_usage_on_adobject to see available methods."

    method = getattr(instance, method_name)
    if not callable(method):
        return f"{method_name} is not a callable method on {object_name}."

    result = method(*args, **kwargs)
    return result


# ---- register tools ----
higher_order_server.tool(list_available_adobjects)
higher_order_server.tool(run_any_adobject_method)

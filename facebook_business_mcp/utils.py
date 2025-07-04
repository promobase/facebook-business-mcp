import ast
import inspect
import logging
import os
import textwrap
from collections.abc import Callable
from functools import wraps
from pathlib import Path
from typing import Any

from facebook_business.exceptions import FacebookError, FacebookRequestError


def get_logger(name: str | None = None) -> logging.Logger:
    if name is None:
        import inspect

        frame = inspect.currentframe()
        if frame and frame.f_back:
            name = frame.f_back.f_globals.get("__name__", "utils")
        else:
            name = "utils"

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger


def load_dotenv(path: str) -> bool:
    env_path = Path(path)

    if not env_path.exists():
        logger = get_logger()
        logger.warning(f"Environment file {env_path} does not exist.")
        return False

    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()

                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]

                os.environ[key] = value

    return True


def handle_facebook_errors(fn: Callable) -> Callable:
    """hof for err handling"""

    @wraps(fn)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return fn(*args, **kwargs)
        except FacebookError as e:
            return str(e)
        except FacebookRequestError as e:
            return str(e)
        except Exception as e:
            return str(e)

    return wrapper


def log_execution(fn: Callable) -> Callable:
    """Decorator to log function execution details."""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        logger = get_logger(fn.__module__)
        logger.info(f"Executing {fn.__name__} with args: {args}, kwargs: {kwargs}")
        result = fn(*args, **kwargs)
        logger.info(f"{fn.__name__} completed successfully.")
        return result

    return wrapper


def wrapped_fn_tool(f: Callable) -> Callable:
    """util for composing different HOFs for a MCP server tool fn"""

    @handle_facebook_errors
    @log_execution
    @wraps(f)
    def wrapper(*args, **kwargs):
        """Wrapper to apply error handling and logging to a tool function."""
        return f(*args, **kwargs)

    return wrapper


def use_adaccount_id(id: str) -> str:
    """Utility to ensure ad account ID is prefixed with 'act_'."""
    if not id.startswith("act_"):
        id = "act_" + id
    return id


#  ---- utils for source code extraction ----
def safe_getsource(obj: Any) -> str:
    try:
        return inspect.getsource(obj)
    except Exception as e:
        return f"// Unable to get source code: {str(e)}"


def get_source_cls_non_methods(cls) -> str:
    src = inspect.getsource(cls)
    src = textwrap.dedent(src)  # Remove indentation
    tree = ast.parse(src)

    class_body = tree.body[0]  # First (and only) class
    lines = src.splitlines()
    keep_lines = set()

    for node in class_body.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):  # noqa: UP038
            continue  # Skip methods
        # For inner classes, assignments, docstring, etc., keep them
        for lineno in range(node.lineno, getattr(node, "end_lineno", node.lineno) + 1):
            keep_lines.add(lineno - 1)  # line numbers are 1-based

    # Optionally, keep the class definition and docstring
    class_def_end = class_body.body[0].lineno - 1 if class_body.body else 1
    for i in range(class_def_end):
        keep_lines.add(i)
    # Now collect filtered lines
    output = [lines[i] for i in sorted(keep_lines)]
    return "\n".join(output)


def list_callable_methods(cls, include_dunder=False):
    """
    List all callable methods (by name) defined on a class.
    By default, omits methods starting and ending with '__' (dunder methods).
    """
    methods = []
    for attr_name in dir(cls):
        if not include_dunder and attr_name.startswith("__") and attr_name.endswith("__"):
            continue  # skip dunder methods
        attr = getattr(cls, attr_name)
        if callable(attr):
            methods.append(attr_name)
    return methods


def fmt_cls(cls: Any) -> str:
    """
    Format a class for LLM consumption. Provides utility
    """
    raise NotImplementedError


def snake_case_to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:]) if components else ""


def camel_case_to_snake_case(camel_str: str) -> str:
    import re

    # Insert underscores before uppercase letters and convert to lowercase
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()

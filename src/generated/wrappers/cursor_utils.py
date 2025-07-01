"""Cursor utilities for type-safe pagination handling."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")


class TypedCursor(Generic[T]):
    """A type-safe wrapper around Facebook's Cursor for paginated results."""

    def __init__(self, cursor: Any, model_class: type[T]):
        """
        Initialize a typed cursor.

        Args:
            cursor: The Facebook API Cursor object
            model_class: The Pydantic model class to convert results to
        """
        self._cursor = cursor
        self._model_class = model_class

    def __iter__(self) -> Iterator[T]:
        """Iterate over items, converting each to the typed model."""
        for item in self._cursor:
            yield self._model_class(**item.export_all_data())

    def __next__(self) -> T:
        """Get the next item as a typed model."""
        item = next(self._cursor)
        return self._model_class(**item.export_all_data())

    def load_next_page(self) -> bool:
        """Load the next page of results."""
        return self._cursor.load_next_page()

    def headers(self) -> dict:
        """Get the response headers."""
        return self._cursor.headers()

    def total(self) -> Optional[int]:
        """Get the total count if available."""
        try:
            return self._cursor.total()
        except:
            return None

    def summary(self) -> Optional[str]:
        """Get the summary if available."""
        try:
            return self._cursor.summary()
        except:
            return None

    def get_one(self) -> Optional[T]:
        """Get a single item from the cursor."""
        item = self._cursor.get_one()
        if item:
            return self._model_class(**item.export_all_data())
        return None

    def to_list(self) -> list[T]:
        """Convert all items to a list (loads all pages)."""
        return list(self)

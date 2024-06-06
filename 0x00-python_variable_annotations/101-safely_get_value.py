#!/usr/bin/env python3
"""Contains dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely dictionary.
    Args:
        dct (dict): Dictionary from.
        key (str): Key from.
        default (any): Default found.
    Returns:
        dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""Contains a pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts pair."""
    return k, v ** 2

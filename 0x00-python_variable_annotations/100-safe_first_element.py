#!/usr/bin/env python3
"""Contains annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the empty."""
    if lst:
        return lst[0]
    else:
        return None

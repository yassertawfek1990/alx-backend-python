#!/usr/bin/env python3
"""Contains floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums floats
    Args:
        input_list (list): floats
    Returns:
        float: list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)

#!/usr/bin/env python3
"""Contains a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        A multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a multiplier"""
        return multiplier * number

    return multiplier_func

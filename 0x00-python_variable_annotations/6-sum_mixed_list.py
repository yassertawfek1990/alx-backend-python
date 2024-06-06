#!/usr/bin/env python3
"""Contains a function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list of float"""
    return sum(mxd_lst)

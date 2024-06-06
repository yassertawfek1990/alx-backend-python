#!/usr/bin/env python3
"""Contains a cv."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns a element"""
    return [(c, len(c)) for c in lst]

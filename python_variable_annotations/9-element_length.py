#!/usr/bin/env python3
""" Type-annotated function """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return type-annotation """
    return [(i, len(i)) for i in lst]

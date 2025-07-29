#!/usr/bin/env python3
""" Type-annotated function """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """The function takes one type-annotated List[] argument,
        and returns the float """
    return sum(input_list)

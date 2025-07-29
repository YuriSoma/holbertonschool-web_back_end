#!/usr/bin/env python3
""" Type-annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(n: float) -> float:
        """The function takes one mixed type-annotated List[] argument,
            and returns the float """
        return n * multiplier
    return multiplier_function

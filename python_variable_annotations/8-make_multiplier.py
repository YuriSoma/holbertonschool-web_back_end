#!/usr/bin/env python3
""" Type-annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return Callable function """
    def multiplier_function(n: float) -> float:
        """The function takes one argument,
            and returns the square by called argument """
        return n * multiplier
    return multiplier_function

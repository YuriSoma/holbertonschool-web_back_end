#!/usr/bin/env python3
""" Type-annotated function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """The function takes one mixed type-annotated List[] argument,
        and returns the float """
    return (k, float(v ** 2))

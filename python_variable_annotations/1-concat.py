#!/usr/bin/env python3
""" Type-annotated function """


def concat(str1: str, str2: str) -> str:
    """The function takes two type-annotated str argument,
        and returns the sum """
    return "{}{}".format(str1, str2)

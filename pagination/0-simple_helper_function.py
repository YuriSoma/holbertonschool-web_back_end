#!/usr/bin/env python3
""" Function returns index range """


def index_range(page, page_size):
    """ receives page number and page size """
    return ((page - 1) * page_size, page * page_size)

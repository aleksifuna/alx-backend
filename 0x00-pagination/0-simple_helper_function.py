#!/usr/bin/env python3
"""
Contains one function index_range
"""


def index_range(page, page_size):
    """
    Computes and return the starting and end index corresponding to
    the range of indexes to return in a list
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)

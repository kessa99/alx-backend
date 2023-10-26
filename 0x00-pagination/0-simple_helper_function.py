#!/usr/bin/env python3
"""
simple pagination who returns tuple
"""


def index_range(page, page_size):
    """
    Args:
        page(int): The current page number
        page_size(int): the number of items per page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

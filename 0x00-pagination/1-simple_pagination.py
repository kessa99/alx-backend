#!/usr/bin/env python3
"""
Pagination for returns head of list
"""
import csv
import math
from typing import List, Tuple


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        find the index pagination
        Args:
            page(int): the current page number
            page_size(int): the number of items per page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        size_of_csv = len(self.dataset())
        start, end = self.index_range(page, page_size)
        end = min(end, size_of_csv)

        if start >= size_of_csv:
            return []
        return self.dataset()[start:end]

    @staticmethod
    def index_range(page, page_size):
        """
        returns a tuple conataining start ans end of index
        Args:
            page (int, optional): the page numbet to retrieve.
            page_size (int, optional): the number of items per page
        Returns:
            List[List]: A List of Lists containing
            the data for the specfified page
        Raises:
            AssertionsError: If page or page_size are not positive integers
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

#!/usr/bin/env python3
""" Simple helper function
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
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
        """ Get the page of the dataset

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Size of the page. Defaults to 10.

        Returns:
            List[List]: List of the dataset
        """
        assert(type(page) is int and type(page_size) is int)
        assert(page > 0 and page_size > 0)
        i = index_range(page, page_size)
        return self.dataset()[i[0]: i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the page of the dataset

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Size of the page. Defaults to 10.

            Returns:
                List[List]: List of the dataset
        """
        assert(type(page) is int and type(page_size) is int)
        assert(page > 0 and page_size > 0)
        self.dataset()
        i = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        result = {
            "page_size": page_size,
            "page": page,
            "data": self.dataset()[i[0]: i[1]],
            "next_page": page + 1 if i[1] + 1 < total_pages else None,
            "prev_page": page - 1 if i[0] - 1 < total_pages else None,
            "total_pages": total_pages
        }
        if result.get("prev_page") == 0:
            result["prev_page"] = None
        return result


def index_range(page: int, page_size: int) -> Tuple:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)

#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        if not index:
            return
        assert(index <= math.ceil(len(self.__indexed_dataset) / page_size))
        # i = 0
        # new_obj = {}
        # while True:
        #     for j in range(len(self.__indexed_dataset)):
        #         if self.__indexed_dataset.get(j):
        #             i += 1
        #             new_obj.update({ i : self.__indexed_dataset.get(j)})
        #     break
        data = []
        for i in range(index, page_size + index):
            if self.__indexed_dataset.get(i):
                data += self.__indexed_dataset.get(i)
                next_page = index + page_size
                if not self.__indexed_dataset.get(i - 1):
                    next_page = index + page_size + 1
            else:
                data += self.__indexed_dataset.get(i + 2)

        return {
            "index": index,
            "data": data,
            "next_index": next_page,
            "page_size": page_size
        }

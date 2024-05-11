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
        """Returns a hyper media paginated dataset
        """
        indexed_data = self.indexed_dataset()
        hyper_dict = {}
        data_list = []
        assert index < len(indexed_data)
        next_index = index + page_size
        i = index
        while len(data_list) < page_size:
            data = indexed_data.get(i)
            if data is None:
                next_index += 1
            else:
                data_list.append(data)
            i += 1
        hyper_dict['index'] = index
        hyper_dict['next_index'] = next_index
        hyper_dict['page_size'] = page_size
        hyper_dict['data'] = data_list

        return hyper_dict

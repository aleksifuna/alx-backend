#!/usr/bin/env python3
"""
Supplies class server defination
"""
import csv
import math
from typing import List, Dict, Union


def index_range(page, page_size):
    """
    Computes and return the starting and end index corresponding to
    the range of indexes to return in a list
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


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
        """
        Paginates a dataset and returns alist with appropriet dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        paginated_list = []
        page_range = index_range(page, page_size)
        try:
            for i in range(page_range[0], page_range[1]):
                paginated_list.append(self.dataset()[i])
        except IndexError:
            paginated_list = []
        return paginated_list

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
            ) -> Dict[str, Union[None, int, List]]:
        """
        Paginates a dataset and returns a dictionary with appropriet dataset
        """
        hyper_dict = {}
        data = self.get_page(page, page_size)
        page_len = len(data)
        total_pages = len(self.dataset()) / page_size
        total_pages = math.ceil(total_pages)
        next_page = page + 1
        if next_page > total_pages:
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        hyper_dict['page_size'] = page_len
        hyper_dict['page'] = page
        hyper_dict['data'] = data
        hyper_dict['next_page'] = next_page
        hyper_dict['prev_page'] = prev_page
        hyper_dict['total_pages'] = total_pages
        return hyper_dict

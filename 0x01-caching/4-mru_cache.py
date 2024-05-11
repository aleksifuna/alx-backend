#!/usr/bin/env python3
"""
MRUcache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Defines methods to put and get items into a cache using MRU algo
    """
    def __init__(self):
        """
        Constructor for the class
        """
        super().__init__()
        self.mru_key = ""

    def put(self, key, item):
        """
        Inserts item with key into the cache
        """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.mru_key = key
                return
            if len(self.cache_data) == self.MAX_ITEMS:
                print(f'DISCARD: {self.mru_key}')
                self.cache_data.pop(self.mru_key)
            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """
        Retrieves an item associated with key from the cache
        """
        if key in self.cache_data.keys():
            self.mru_key = key
            return self.cache_data[key]
        return None

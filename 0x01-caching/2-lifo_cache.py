#!/usr/bin/env python3
"""
LIFOcache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines methods to put and get items into a cache using LIFO algo
    """
    def __init__(self):
        """
        Constructor for the class
        """
        super().__init__()
        self.last_in = ""

    def put(self, key, item):
        """
        Inserts item with key into the cache
        """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.last_in = key
                return
            if len(self.cache_data) == self.MAX_ITEMS:
                print(f'DISCARD: {self.last_in}')
                self.cache_data.pop(self.last_in)
            self.cache_data[key] = item
            self.last_in = key

    def get(self, key):
        """
        Retrieves an item associated with key from the cache
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None

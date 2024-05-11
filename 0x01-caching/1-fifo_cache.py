#!/usr/bin/env python3
"""
FIFOcache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines methods to put and get items into a cache using FIFO algo
    """
    def __init__(self):
        """
        Constructor for the class
        """
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """
        Inserts item with key into the cache
        """
        if key and item:
            if key not in self.key_list:
                self.key_list.append(key)
            self.cache_data[key] = item
        if len(self.key_list) > self.MAX_ITEMS:
            print(f'DISCARD: {self.key_list[0]}')
            self.cache_data.pop(self.key_list[0])
            self.key_list.pop(0)

    def get(self, key):
        """
        Retrieves an item associated with key from the cache
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None

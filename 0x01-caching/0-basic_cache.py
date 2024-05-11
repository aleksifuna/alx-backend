"""
Basic_caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Defines methods to put and get items into a cache
    """
    def put(self, key, item):
        """
        Inserts item with key into the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item associated with key from the cache
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None

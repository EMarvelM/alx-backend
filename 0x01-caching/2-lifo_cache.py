#!/usr/bin/env python3
""" Last In First Out Caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Last In First Out Caching class
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        if length of cache_data is gt MAX_ITEM then remove from end

        Return: None if key or item is empty
        """
        if not key or not item:
            return
        cached_data_key = self.cache_data.keys()
        if len(cached_data_key) >= self.MAX_ITEMS:
            if key not in cached_data_key:
                last_item = list(cached_data_key)[-1]
                self.cache_data.pop(last_item)
                print("DISCARD:", last_item)
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if not key or key not in self.cache_data.keys():
            return
        return self.cache_data[key]

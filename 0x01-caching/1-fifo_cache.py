#!/usr/bin/env python3
""" First In First Out Caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First In First Out Caching class
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        if length of cache_data is gt MAX_ITEM then remove from beginning

        Return: None if key or item is empty
        """
        if not key or not item:
            return

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            first_item = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_item)
            print("DISCARD:", first_item)
        self.cache_data.update({key: item})

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if not key or key not in self.cache_data.keys():
            return
        return self.cache_data[key]

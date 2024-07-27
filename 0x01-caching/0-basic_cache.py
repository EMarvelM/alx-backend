#!/usr/bin/env python3
""" caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class for caching
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key

        Return: None if key or item is empty
        """
        if not key or not item:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if not key or key not in self.cache_data.keys():
            return
        return self.cache_data[key]

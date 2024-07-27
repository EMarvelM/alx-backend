#!/usr/bin/env python3
"""
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if not key or not item:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        if not key or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
 
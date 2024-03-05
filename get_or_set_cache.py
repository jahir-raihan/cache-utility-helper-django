# Imports

import json
import zlib
from collections import OrderedDict
from django.core.cache import cache

# End Imports


class GetOrSetCache:

    """
    Get or Set Compressed/Non-Compressed cache data
    """

    def __init__(self, cache_key, data=None, renew_time=None):
        self.cache_key = cache_key
        self.data = data
        self.renew_time = renew_time

    def get_cached_data(self):

        """
        Get non-compressed cached data from cache memory
        """

        __data = cache.get(self.cache_key, False)
        return __data

    def get_compressed_cached_data(self):

        """
        Get compressed data of cache memory or False if not there
        """

        # Get compressed data
        __compressed_data = cache.get(self.cache_key, False)
        __decompressed_data = __compressed_data

        # If there is a cache decompress it and return else return false
        if __compressed_data:
            __decompressed_data = self.decompress_data(__compressed_data)
        return __decompressed_data

    def store_cache_data(self):

        """
        Store non-compressed cache data
        """

        cache.set(self.cache_key, self.data, self.renew_time)
        __non_compressed_data = json.dumps(self.data)

    def store_compressed_cache_data(self):

        """
        Stores compressed cache data
        """

        # Get compressed data
        __compressed_data = self.compress_data()

        # Store compressed data
        cache.set(self.cache_key, __compressed_data, self.renew_time)

    def compress_data(self):

        """
        Compresses a list of OrderedDict objects using zlib.
        """

        __json_str = json.dumps(self.data)
        __compressed_data = zlib.compress(__json_str.encode('utf-8'))
        return __compressed_data

    def decompress_data(self, compressed_data):

        """
        Decompresses a list of OrderedDict objects using zlib.
        """

        __decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
        return json.loads(__decompressed_data, object_pairs_hook=lambda pairs: OrderedDict(pairs))

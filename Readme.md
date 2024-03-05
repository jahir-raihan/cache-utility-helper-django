# Cache helper utility

**Just a simple class to simplify setting and getting `Django-Based`
`Redis` `compressed / uncompressed` cache data.**

## Why we need to compress cache data or why do we even need cache?

> **Just Imagine you've got a view which returns list of books for every request from frontend. Now to get the list you
> have to query over the database table for every request which is not good. Suppose 100k user accesses the same result and your'e
> querying the database for 100k times. Which is not good for computation, resource and response time complexity. To avoid this
> we use cache to handle frequently accessed results. But cacheing may come in different faces,
> suppose your'e caching a related video queryset, which is unique for each video. Now Imagine 100k users opens 100k
> videos and you have to store 100k combination of cached data which is disaster. And for example if a cache size is suppose 50kb
> then just imagine the storage will be used 50*100000 kb.** <br>
> 
> **So to avoid these circumstances and to utilize caching more efficiently, compressing the queryset comes in 
> handy while saving cache, yes there is a chance to lose some data while compressing but that isn't much to be noticed.**
> 
> <br>**To get you an overview, a raw queryset may be size of 100kb but when compressed it will become 10 time smaller eg: 10kb or less.**


## Requirements & Imports
**Note: It can be only used inside a django project. For others, Dunno!**

These packages are included by default.
```
zlib, json
# And Django/rest_framework as framework
```

## How to use

**Just Import the class and start using**

```python
from get_or_set_cache import GetOrSetCache
from example_serializer import ExampleSerializer
from django.views import View
from some_models import ExampleModel


class ExampleView(View):
    
    """
    Example class based view
    """
    
    def get(self, request):
        
        """
        Simple get method to demonstrate get and set cache.
        Imagine I'm accessing the Example model data with some key
        """
        
        key = request.GET.get('key', 'defaultkey')
        
        cache_data = GetOrSetCache(key).get_cached_data() 
        # Or if the cache data is compressed then 
        cache_data_compressed = GetOrSetCache(key).get_compressed_cached_data()
        
        # Now if there's no cache data with the given key then you can set up new cache data
        if not cache_data or cache_data_compressed:
            
            renew_time = 30*30 # The cache will last until this renew time 
            
            model_data = ExampleModel.objects.all()
            
            # Note after using .data it returns OrderedDict Data
            serialized_model_data = ExampleSerializer(model_data, many=True).data
            
            # Store only cache data without compressing
            store_cache_data = GetOrSetCache(key, serialized_model_data, renew_time).store_cache_data()
            
            # Store compressed cache data
            store_compressed_cache_data = GetOrSetCache(key, serialized_model_data, renew_time).store_compressed_cache_data()
            
            return serialized_model_data
        
        return cache_data or cache_data_compressed

```

## Hit a star If it helps you.

<p style="padding:2em; background:black; color:white; font-weight:bold; font-size:24px; text-align:center;">Happy Coding . . .</p>
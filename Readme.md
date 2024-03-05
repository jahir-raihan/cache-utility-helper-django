# Cache helper utility

**Just a simple class to simplify setting and getting `Django-Based`
`Redis` `compressed / uncompressed` cache data.**

## Requirements & Imports
**Note: It can be only used inside a django project. For others, Dunno!**

These packages are included by default.
```
zlib, json
# And Django as framework
```

## How to use

**Just Import the class and start using**

```python
from get_or_set_cache import GetOrSetCache
from example_serializer import ExampleSerializer
from django.views import View
from some_models import ExampleModel
from django.core import cache

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
        
        # Now if there's now cache data with the given key then you can set up new cache data
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
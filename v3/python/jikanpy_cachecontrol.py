"""
An example of how to transparently cache jikanpy requests using the
cachecontrol/requests modules
To install:
pip install --user cachecontrol[filecache] jikanpy
"""

import time

import requests
import jikanpy
from cachecontrol import CacheControl
from cachecontrol.heuristics import ExpiresAfter
from cachecontrol.caches.file_cache import FileCache

# define heuristic, how long requests should stay in cache
# you can modify this to fit whatever you want
# it accepts the same kwargs as datetime.timedelta:
# https://docs.python.org/3/library/datetime.html#datetime.timedelta
expires = ExpiresAfter(days=1)

# create session and mount file cache
session = CacheControl(requests.Session(), heuristic=expires, cache=FileCache("cache_dir"))

# use session for jikanpy
j = jikanpy.Jikan(session=session)

# the second request here is cached
print(j.anime(1)["title"])
print(j.anime(1)["title"])


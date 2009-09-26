#!/usr/bin/env python
"""
>>> import sys
>>> sys.path.insert(0, "../pyshardmanager")

>>> import pyshardmanager
>>> path = "test/files/shard.json"
>>> pyshardmanager.ShardManager(path, format="json") #doctest: +ELLIPSIS
<pyshardmanager.shardmanager.ShardManager object at ...>
>>> shardmanager = pyshardmanager.ShardManager(path, auto_reload=True)
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()


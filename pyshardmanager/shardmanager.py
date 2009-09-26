try:
    import json
except ImportError:
    import simplejson as json

loader = dict(
    json = lambda path: json.loads(open(path).read()),
)

class ShardManager(object):
    def __init__(self, path, format=None, auto_reload=None):
        if format == None:
            format = "json"
        if format not in loader.keys():
            raise #FIXME
        self.conf = loader[format](path)
        if auto_reload == None:
            auto_reload = False
        self.auto_reload = auto_reload


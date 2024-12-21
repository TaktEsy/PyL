import sys
import inspect
import pprint
def introspect(obj):
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith("__")]
    res = {
        'type' : type(obj),
        'attrs' : dir(obj),
        'meth': methods,
        'doc' : obj.__doc__
    }

    return pprint.pprint(res)

introspect(104)

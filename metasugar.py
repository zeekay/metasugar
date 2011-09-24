from collections import defaultdict
from inspect import getfullargspec

class member_table(dict):
    def __init__(self):
        self.registry = defaultdict(dict)

    def __setitem__(self, key, value):
        if hasattr(value, '__annotations__'):
            spec = getfullargspec(value)
            signature = tuple([spec.annotations[k] for k in spec.args[1:]])
            self.registry[key][signature] = value
            def wrapper(registry=self.registry[key][signature], spec=spec, *args, **kwargs):
                print(args, kwargs)
                signature = tuple(type(x) for x in args[1:])
                if kwargs:
                    signature += tuple(type(kwargs[k]) for k in spec.args if k in kwargs)
                return self.registry[key][signature](*args, **kwargs)
            value = wrapper
        dict.__setitem__(self, key, value)

class hax(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return member_table()

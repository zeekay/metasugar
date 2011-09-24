from metasugar import hax

class Bar:
    def method(self, x, y):
        return 'The meaning of {} is {}.'.format(x, y)

class Foo(metaclass=hax):
    def foo(self, x: str): return x+x
    def foo(self, x: int): return x*x
    def foo(self, x: str, y: int): return x*y
    def foo(self, x: Bar, y: str, z: int): return x.method(y, z)

f = Foo()

for args in ['foo'], [2], ['foo', 4], [Bar(), 'life', 42]:
    print(f.foo(*args))

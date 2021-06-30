from collections import deque
# https://docs.python.org/3/library/collections.html

class Counter:
    '''I count. That is all.'''
    all_counters = []
    def __init__(self, initial=0):
        """constructor, not return"""
        self.value = initial
        Counter.all_counters.append(self)

    def increment(self):
        self.value += 1

    def get(self):
        return self.value
  
c = Counter(42)
for i in range(8): c.increment()
print(c.get())

class MemorizingDict(dict):
    """
    This class remembers transferred keys and values
    """
    _history = deque(maxlen=10)

    def set(self, key, value):
        self._history.append(key)
        self[key] = value

    def get_history(self):
        # print(type(self._history)) -> collections.deque
        return self._history
    
    def help(self):
        return(f"Doc: {self.__doc__}Class_object = {self.__class__} \n\tDict_attributes = {self.__dict__}")


d = MemorizingDict({"something": 41})
d.set("Hi", 100050)
print(d.get_history())  # -> 1 

d = MemorizingDict()
d.set("Hello", 500010)
print(d.get_history())  # -> 2
print(d.help())         # help

# print(vars(Counter)) -> dict{attributes}

class SomeClass():
    __slots__ = ["someattribute"] # see name tuple, extends from name tuple
    def do_something(self):
        print("Doing something.")

print(SomeClass().do_something)   # related
print(SomeClass().do_something()) # 
print(SomeClass.do_something)   # unrelated


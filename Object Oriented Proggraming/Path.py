import os.path
  
# Path
path = 'repositres/Algorithms/Binary_search_iteration.py'
dirname = os.path.dirname(path)
   
print(dirname)

class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return("Path({})".format(self.current))
    
    @property
    def parent(self):
        return Path(dirname(self.current))

p = Path('repositres/Algorithms/Binary_search_iteration.py')
print(p.parent)
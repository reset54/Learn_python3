<<<<<<< HEAD
import os.path
  
# Path
path = 'repositres/Algorithms/Binary_search_iteration.py'
dirname = os.path.dirname(path)
   
print(dirname)

class Path:
    def __init__(self, current) -> None:
        self.current = current

    def __repr__(self: str) -> str:
        return("Path({})".format(self.current))
    
    @property
    def parent(self: str) -> str:
        pass

p = Path('repositres/Algorithms/Binary_search_iteration.py')
=======
import os.path
  
# Path
path = 'repositres/Algorithms/Binary_search_iteration.py'
dirname = os.path.dirname(path)
   
print(dirname)

class Path:
    def __init__(self, current) -> None:
        self.current = current

    def __repr__(self: str) -> str:
        return("Path({})".format(self.current))
    
    @property
    def parent(self: str) -> str:
        pass

p = Path('repositres/Algorithms/Binary_search_iteration.py')
>>>>>>> refs/remotes/origin/readme
print(p.parent)
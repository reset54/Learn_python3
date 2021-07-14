import sys
sys.path.append("/home/reset54/repositres/Object Oriented Proggraming") # add absolutepath in another dirrectory
import unittest
import Circle


class Test_circle(unittest.TestCase):
    def test_get_diameter(self): 
        self.assertEqual(Circle.Circle(30).get_diameter(), 60)
        self.assertEqual(Circle.Circle(1000).get_diameter(), 2000)
        self.assertEqual(Circle.Circle(0).get_diameter(), 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from math import pi
from main import circle_area, area_rectangle

class TestAreas(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(circle_area(3), pi * (3 ** 2))
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi * (2.5 ** 2))

    
if __name__ == '__main__':
    unittest.main()

import unittest
from core.coordinate import load_start_coordinate, format_coordinate

class CoordinateTests(unittest.TestCase):

    def test_load_valid_start_coordinate(self):
        content = "X=123456789, Y=1"
        x, y = load_start_coordinate(content)
        self.assertEqual(x, 123456789)
        self.assertEqual(y, 1)

    def test_format_coordinate(self):
        x, y = 123456789, 1
        formatted = format_coordinate(x, y)
        self.assertEqual(formatted, "X=123456789, Y=1")

if __name__ == '__main__':
    unittest.main()

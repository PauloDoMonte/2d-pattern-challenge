import unittest
from decimal import Decimal
from core.coordinate import load_start_coordinate, format_coordinate, load_start_termination

class CoordinateTests(unittest.TestCase):

    def test_load_valid_start_coordinate(self):
        content = "X=123456789, Y=1"
        x, y = load_start_coordinate(content)
        self.assertEqual(x, Decimal(123456789))
        self.assertEqual(y, Decimal(1))

    def test_load_start_coordinate_with_decimal(self):
        content = "X=123456789.123456789, Y=1.000000001"
        x, y = load_start_coordinate(content)
        self.assertEqual(x, Decimal("123456789.123456789"))
        self.assertEqual(y, Decimal("1.000000001"))

    def test_format_coordinate(self):
        x, y = Decimal("123456789.123456789"), Decimal("1.000000001")
        formatted = format_coordinate(x, y)
        self.assertEqual(formatted, "X=123456789.123456789, Y=1.000000001")

    def test_load_start_termination(self):
        content = "X=987654321, Y=2"
        x, y = load_start_termination(content)
        self.assertEqual(x, Decimal(987654321))
        self.assertEqual(y, Decimal(2))

if __name__ == '__main__':
    unittest.main()
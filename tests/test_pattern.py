import unittest
from core.pattern import generate_pattern, apply_pattern, reverse_pattern

class PatternTests(unittest.TestCase):

    def test_generate_pattern_returns_expected_number_of_points(self):
        pattern = generate_pattern(10)
        self.assertEqual(len(pattern), 10)
        for point in pattern:
            self.assertTrue((point["x"] & (point["x"] - 1)) == 0, f"X value {point['x']} is not a power of 2")
            self.assertTrue((point["y"] & (point["y"] - 1)) == 0, f"Y value {point['y']} is not a power of 2")

    def test_apply_pattern_increments_coordinates(self):
        pattern = [{"x": 2, "y": 4}]
        start_x, start_y = 0, 0
        result_x, result_y = apply_pattern(start_x, start_y, pattern, 1)
        self.assertEqual(result_x, 2)
        self.assertEqual(result_y, 4)

    def test_reverse_pattern_decrements_coordinates(self):
        pattern = [{"x": 2, "y": 4}]
        start_x, start_y = 2, 4
        result_x, result_y = reverse_pattern(start_x, start_y, pattern, 1)
        self.assertEqual(result_x, 0)
        self.assertEqual(result_y, 0)

if __name__ == '__main__':
    unittest.main()

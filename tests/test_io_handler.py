import unittest
import json
from core.io_handler import read_file, write_file, save_pattern, load_pattern

class IOHandlerTests(unittest.TestCase):

    def test_read_file_returns_content(self):
        content = read_file('data/start-coordinate.txt')
        self.assertTrue(content.startswith("X="))

    def test_write_file_creates_expected_content(self):
        test_content = "X=987654321, Y=2"
        write_file('data/test-output.txt', test_content)
        content = read_file('data/test-output.txt')
        self.assertEqual(content, test_content)

    def test_save_pattern_validates_points_are_powers_of_two(self):
        valid_pattern = [{"x": 2, "y": 4}, {"x": 8, "y": 16}]
        try:
            save_pattern(valid_pattern, 'data/test-pattern.json')
        except ValueError as e:
            self.fail(f"save_pattern raised ValueError unexpectedly: {e}")

        # Now test saving an invalid pattern
        invalid_pattern = [{"x": 3, "y": 4}, {"x": 8, "y": 5}]
        with self.assertRaises(ValueError):
            save_pattern(invalid_pattern, 'data/test-pattern.json')

    def test_load_pattern_validates_points_are_powers_of_two(self):
        valid_pattern = [{"x": 2, "y": 4}, {"x": 8, "y": 16}]
        with open('data/test-pattern.json', 'w') as f:
            json.dump(valid_pattern, f)

        loaded_pattern = load_pattern('data/test-pattern.json')
        self.assertEqual(loaded_pattern, valid_pattern)

        # Now test loading an invalid pattern
        invalid_pattern = [{"x": 3, "y": 4}, {"x": 8, "y": 5}]
        with open('data/test-invalid-pattern.json', 'w') as f:
            json.dump(invalid_pattern, f)

        with self.assertRaises(ValueError):
            load_pattern('data/test-invalid-pattern.json')

if __name__ == '__main__':
    unittest.main()

import unittest
import os
from core.io_handler import read_file, write_file
from main import run_goal_1, run_goal_2, START_COORD_FILE, TERMINATION_FILE, CALCULATED_START_FILE, PATTERN_FILE, GREEN_LINES_FILE

class MainTests(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        with open(START_COORD_FILE, 'w') as f:
            f.write("X=330, Y=1")
        with open(GREEN_LINES_FILE, 'w') as f:
            f.write("lower=2^5, upper=2^10")
        with open(TERMINATION_FILE, 'w') as f:
            f.write("X=2^330, Y=2^1")
        with open(PATTERN_FILE, 'w') as f:
            f.write('[{"x": "2^1", "y": "2^1"}]')

    def tearDown(self):
        if os.path.exists(START_COORD_FILE):
            os.remove(START_COORD_FILE)
        if os.path.exists(GREEN_LINES_FILE):
            os.remove(GREEN_LINES_FILE)
        if os.path.exists(TERMINATION_FILE):
            os.remove(TERMINATION_FILE)
        if os.path.exists(CALCULATED_START_FILE):
            os.remove(CALCULATED_START_FILE)
        if os.path.exists(PATTERN_FILE):
            os.remove(PATTERN_FILE)

    def test_run_goal_1(self):
        run_goal_1()
        self.assertTrue(os.path.exists(TERMINATION_FILE))
        with open(TERMINATION_FILE, 'r') as f:
            content = f.read().strip()
        self.assertTrue(content.startswith("X=2^"))
        self.assertTrue(content.endswith("Y=2^"))

    def test_run_goal_2(self):
        run_goal_2()
        self.assertTrue(os.path.exists(CALCULATED_START_FILE))
        with open(CALCULATED_START_FILE, 'r') as f:
            content = f.read().strip()
        self.assertTrue(content.startswith("X=2^"))
        self.assertTrue(content.endswith("Y=2^"))

if __name__ == '__main__':
    unittest.main()
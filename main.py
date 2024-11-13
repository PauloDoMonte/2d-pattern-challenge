import sys
import os
from core.pattern import generate_pattern, apply_pattern, reverse_pattern
from core.coordinate import load_start_coordinate, format_coordinate, load_start_termination
from core.io_handler import read_file, write_file, save_pattern, load_pattern, load_green_lines
from core.io_handler import save_root_diff, load_root_diff, write_file_termination

CONST_REPETITIONS = 1000

DATA_DIR = "data/"
START_COORD_FILE = os.path.join(DATA_DIR, "start-coordinate.txt")
GREEN_LINES_FILE = os.path.join(DATA_DIR, "green-lines.txt")
TERMINATION_FILE = os.path.join(DATA_DIR, "termination-coord.txt")
PATTERN_FILE = os.path.join(DATA_DIR, "2d-pattern.json")
CALCULATED_START_FILE = os.path.join(DATA_DIR, "start-coordinate-calculated.txt")


def validate_file_exists(file_path):
    """Check if the file exists."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' does not exist.")


def run_goal_1(repetitions=CONST_REPETITIONS):
    """Generate termination coordinate and pattern for Goal 1."""
    validate_file_exists(START_COORD_FILE)
    validate_file_exists(GREEN_LINES_FILE)

    start_coord = load_start_coordinate(read_file(START_COORD_FILE))
    lower_bound, upper_bound = load_green_lines(read_file(GREEN_LINES_FILE))

    pattern = generate_pattern(lower_bound, upper_bound)
    x, y, root_diff = apply_pattern(*start_coord, pattern, repetitions, lower_bound, upper_bound)

    save_pattern(pattern, PATTERN_FILE)
    save_root_diff(root_diff)
    write_file_termination(TERMINATION_FILE, (x, y))

    print("Goal 1 completed: Termination coordinate saved to 'termination-coord.txt'.")


def run_goal_2(repetitions=CONST_REPETITIONS):
    """Calculate the start coordinate from termination coordinate for Goal 2."""
    validate_file_exists(TERMINATION_FILE)
    validate_file_exists(PATTERN_FILE)

    termination_coord = load_start_termination(TERMINATION_FILE)
    pattern = load_pattern(PATTERN_FILE)
    root_diff = load_root_diff()

    lower_bound, upper_bound = load_green_lines(read_file(GREEN_LINES_FILE))
    start_coord = reverse_pattern(*termination_coord, pattern, repetitions, lower_bound, upper_bound, root_diff)

    write_file(CALCULATED_START_FILE, format_coordinate(*start_coord))
    print("Goal 2 completed: Start coordinate saved to 'start-coordinate-calculated.txt'.")


def print_usage():
    """Print usage instructions."""
    print("Usage:")
    print("  python main.py")
    print("    - This will run Goal 1, generating the 2D pattern and termination coordinate.")
    print("")
    print("  python main.py goal-2")
    print("    - This will run Goal 2, calculating the start coordinate from termination coordinate.")
    print("")
    print("Make sure the necessary files are in the 'data/' folder.")


def main():
    """Main entry point of the program."""
    if len(sys.argv) == 1:
        run_goal_1()
    elif len(sys.argv) == 2 and sys.argv[1] == "goal-2":
        run_goal_2()
    else:
        print("Error: Invalid arguments.")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()

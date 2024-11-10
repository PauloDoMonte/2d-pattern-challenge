import sys
from core.pattern import generate_pattern, apply_pattern, reverse_pattern
from core.coordinate import load_start_coordinate, format_coordinate
from core.io_handler import read_file, write_file, save_pattern, load_pattern
from core.utils import validate_file_exists, validate_coordinate_format, load_and_validate_start_coordinate, load_and_validate_green_lines

CONST_REPETITIONS = 1000

def run_goal_1(start_file, green_lines_file, repetitions=CONST_REPETITIONS):
    """Generate termination coordinate and pattern for Goal 1."""
    validate_file_exists(start_file, ".txt")
    validate_file_exists(green_lines_file, ".txt")
    
    start_coord = load_and_validate_start_coordinate(start_file)
    lower_bound, upper_bound = load_and_validate_green_lines(green_lines_file)
    
    pattern = generate_pattern(*start_coord, lower_bound, upper_bound)
    termination_coord = apply_pattern(*start_coord, pattern, repetitions, lower_bound, upper_bound)

    save_pattern(pattern, "data/2d-pattern.json")
    write_file("data/termination-coord.txt", format_coordinate(*termination_coord))
    
    print("Goal 1 completed: Termination coordinate saved to 'termination-coord.txt'.")

def run_goal_2(termination_file, pattern_file, repetitions=CONST_REPETITIONS):
    """Calculate the start coordinate from termination coordinate for Goal 2."""
    validate_file_exists(termination_file, ".txt")
    validate_file_exists(pattern_file, ".json")
    
    termination_coord = load_and_validate_start_coordinate(termination_file)
    
    pattern = load_pattern(pattern_file)
    start_coord = reverse_pattern(*termination_coord, pattern, repetitions)
    
    write_file("data/start-coordinate-calculated.txt", format_coordinate(*start_coord))
    print("Goal 2 completed: Start coordinate saved to 'start-coordinate-calculated.txt'.")

def print_usage():
    """Print usage instructions."""
    print("Usage:")
    print("  python main.py <start-coordinate.txt> <green-lines.txt>")
    print("    - This will generate the 2D pattern and termination coordinate.")
    print("    - The generated 2D pattern will be saved in 'data/2d-pattern.json'.")
    print("    - The termination coordinate will be saved in 'data/termination-coord.txt'.")
    print("")
    print("  python main.py goal-2 <termination-coord.txt> <2d-pattern.json>")
    print("    - This will calculate the start coordinate from the termination coordinate and the 2D pattern.")
    print("    - The calculated start coordinate will be saved in 'data/start-coordinate-calculated.txt'.")
    print("")
    print("To run the tests:")
    print("  python -m unittest discover -s tests")
    print("    - This will run all the unit tests in the 'tests' folder.")
    print("    - Ensure that the test files are properly set up and located in the 'tests' directory.")
    print("    - Test results will be displayed in the terminal.")

def main():
    """Main entry point of the program."""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == "goal-2" and len(sys.argv) == 4:
        termination_file = sys.argv[2]
        pattern_file = sys.argv[3]
        run_goal_2(termination_file, pattern_file)
    elif len(sys.argv) == 3:
        start_file = sys.argv[1]
        green_lines_file = sys.argv[2]
        run_goal_1(start_file, green_lines_file)
    else:
        print("Error: Invalid arguments.")
        print("For Goal 1, provide: <start-coordinate.txt> <green-lines.txt>")
        print("For Goal 2, provide: goal-2 <termination-coord.txt> <2d-pattern.json>")
        sys.exit(1)

if __name__ == "__main__":
    main()

import sys
import os
import re
from core.pattern import generate_pattern, apply_pattern, reverse_pattern
from core.coordinate import load_start_coordinate, format_coordinate
from core.io_handler import read_file, write_file, save_pattern, load_pattern

CONST_REPETITIONS = 300

def validate_file(file_path, expected_extension):
    """Validate if the file exists and has the correct extension."""
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)
    if not file_path.endswith(expected_extension):
        print(f"Error: File '{file_path}' is not a valid {expected_extension} file.")
        sys.exit(1)

def validate_coordinate_format(content):
    """Validate if the content is in the format X=<value>, Y=<value>."""
    pattern = r"^X=-?\d+, Y=-?\d+$"
    if not re.match(pattern, content.strip()):
        print("Error: Invalid coordinate format. Expected format is 'X=<value>, Y=<value>'.")
        sys.exit(1)

def run_goal_1(start_file):
    """Executes Goal 1: Generate termination coordinate and pattern."""
    validate_file(start_file, ".txt")
    
    start_content = read_file(start_file)
    validate_coordinate_format(start_content)
    
    start_coord = load_start_coordinate(start_content)
    
    pattern = generate_pattern()
    repetitions = CONST_REPETITIONS  # Arbitrary value for demonstration
    termination_coord = apply_pattern(*start_coord, pattern, repetitions)
    
    save_pattern(pattern, "data/2d-pattern.json")
    write_file("data/termination-coord.txt", format_coordinate(*termination_coord))
    print("Goal 1 completed: Termination coordinate saved to 'termination-coord.txt'.")

def run_goal_2(termination_file, pattern_file):
    """Executes Goal 2: Calculate start coordinate from termination coordinate."""
    validate_file(termination_file, ".txt")
    validate_file(pattern_file, ".json")
    
    termination_content = read_file(termination_file)
    validate_coordinate_format(termination_content)
    
    termination_coord = load_start_coordinate(termination_content)
    
    pattern = load_pattern(pattern_file)
    repetitions = CONST_REPETITIONS  # Same value as in Goal 1
    start_coord = reverse_pattern(*termination_coord, pattern, repetitions)
    
    write_file("data/start-coordinate-calculated.txt", format_coordinate(*start_coord))
    print("Goal 2 completed: Start coordinate saved to 'start-coordinate-calculated.txt'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py <start-coordinate.txt>")
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
        
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == "goal-2" and len(sys.argv) == 4:
        termination_file = sys.argv[2]
        pattern_file = sys.argv[3]
        run_goal_2(termination_file, pattern_file)
    elif len(sys.argv) == 2:
        start_file = sys.argv[1]
        run_goal_1(start_file)
    else:
        print("Error: Invalid arguments.")
        sys.exit(1)

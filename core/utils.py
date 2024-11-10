import os
import re
from .io_handler import read_file, load_green_lines
from .coordinate import load_start_coordinate

def validate_file_exists(file_path, expected_extension):
    """Check if the file exists and has the correct extension."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' does not exist.")
    if not file_path.endswith(expected_extension):
        raise ValueError(f"Error: File '{file_path}' must be a {expected_extension} file.")

def validate_coordinate_format(content):
    """Validate if the content is in the format X=<value>, Y=<value>."""
    pattern = r"^X=-?\d+, Y=-?\d+$"
    if not re.match(pattern, content.strip()):
        raise ValueError("Error: Invalid coordinate format. Expected format is 'X=<value>, Y=<value>'.")

def load_and_validate_start_coordinate(start_file):
    """Load and validate the start coordinate from a file."""
    start_content = read_file(start_file)
    validate_coordinate_format(start_content)
    return load_start_coordinate(start_content)

def load_and_validate_green_lines(green_lines_file):
    """Load and validate the green lines from a file."""
    green_lines_content = read_file(green_lines_file)
    return load_green_lines(green_lines_content)

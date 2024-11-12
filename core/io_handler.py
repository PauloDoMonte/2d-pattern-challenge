import json, math
from decimal import Decimal, getcontext

getcontext().prec = 1000000


def read_file(filename):
    """Reads the content of a file."""
    print(f"Reading file: {filename}")
    with open(filename, 'r') as f:
        content = f.read()
    return content


def write_file(filename, content):
    """Writes content to a file."""
    print(f"Writing to file: {filename}")
    with open(filename, 'w') as f:
        f.write(content)

def is_power_of_two(x):
    if x <= 0:
        return False
    
    d = Decimal(x)
    while d % 2 == 0:
        d /= 2
    
    return d == 1    


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return str(obj)  # Converte o Decimal para string
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")


def save_pattern(pattern, filename="data/2d-pattern.json"):
    """Saves the 2D pattern to a JSON file after validating the pattern format."""
    print(f"Saving pattern to {filename}...")

    for idx, point in enumerate(pattern):
        if not is_power_of_two(point["x"]):
            raise ValueError(f"Invalid x value at index {idx} is not a power of 2.")
        if not is_power_of_two(point["y"]):
            raise ValueError(f"Invalid y value at index {idx} is not a power of 2.")
    
    with open(filename, 'w') as f:
        json.dump(pattern, f, default=decimal_default, indent=4)
    print(f"Pattern saved to {filename}.")


def evaluate_power_of_two(expression):
    """Evaluates a string expression like '2^N' and returns the corresponding value."""
    base, exponent = expression.split('^')
    return Decimal(2) ** int(exponent)


def load_green_lines(content):
    """
    Load the coordinates of the green lines from a file.
    Expected format: lower=2^575100, upper=2^602100
    """
    print("Loading green lines...")
    lines = content.strip().split(',')

    lower_expr = lines[0].split('=')[1].strip()
    upper_expr = lines[1].split('=')[1].strip()
    
    lower_value = evaluate_power_of_two(lower_expr)
    upper_value = evaluate_power_of_two(upper_expr)

    return lower_value, upper_value


def load_pattern(filename="data/2d-pattern.json"):
    """Loads the 2D pattern from a JSON file and validates its contents."""
    print(f"Loading pattern from {filename}...")

    with open(filename, 'r') as f:
        pattern = json.load(f)

    for point in pattern:
        point["x"] = Decimal(point["x"])  # Directly convert x to Decimal
        point["y"] = Decimal(point["y"])  # Directly convert y to Decimal

        # Check if x and y are powers of 2
        if not is_power_of_two(int(point["x"])):  # Check with integer value
            raise ValueError(f"Invalid x value {point['x']} in loaded pattern: It is not a power of 2.")
        if not is_power_of_two(int(point["y"])):  # Check with integer value
            raise ValueError(f"Invalid y value {point['y']} in loaded pattern: It is not a power of 2.")


    print(f"Pattern loaded from {filename}.")
    return pattern

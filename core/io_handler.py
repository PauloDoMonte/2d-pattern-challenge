import json, math
from decimal import Decimal, getcontext

getcontext().prec = 100000000


def read_file(filename):
    """Reads the content of a file."""
    with open(filename, 'r') as f:
        content = f.read()
    return content


def write_file(filename, content):
    """Writes content to a file."""
    with open(filename, 'w') as f:
        f.write(content)

def write_file_termination(filename, content):
    """Writes content to a file in the format 2^N."""
    with open(filename, 'w') as f:
        x, y = content
        
        # Write the numbers as 2^N format
        f.write(f"X=2^{x}, Y=2^{y}\n")


def load_green_lines(content):
    """Load the coordinates of the green lines from a file."""
    lines = content.strip().split(',')

    lower_expr = lines[0].split('=')[1].strip()
    upper_expr = lines[1].split('=')[1].strip()

    return lower_expr, upper_expr


def save_pattern(pattern, filename="data/2d-pattern.json"):
    """Saves the 2D pattern to a JSON file as '2^x_exp' format."""
    pattern_with_powers = []

    for point in pattern:
        # Converting the exponents to '2^x_exp' and '2^y_exp'
        pattern_with_powers.append({
            "x": f"2^{point['x']}",
            "y": f"2^{point['y']}"
        })

    # Save the pattern to JSON
    with open(filename, 'w') as f:
        json.dump(pattern_with_powers, f, indent=4)


def load_pattern(filename="data/2d-pattern.json"):
    """Loads the 2D pattern from a JSON file and extracts the exponents."""
    try:
        with open(filename, 'r') as f:
            pattern = json.load(f)

        filtered_pattern = []
        for point in pattern:
            if "x" in point and "y" in point:
                # Extracting the exponent from the string '2^x_exp' and '2^y_exp'
                x_exp = int(point["x"].split('^')[1])  # Get the exponent after '2^'
                y_exp = int(point["y"].split('^')[1])

                filtered_pattern.append({
                    "x": x_exp,
                    "y": y_exp
                })

        return filtered_pattern

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
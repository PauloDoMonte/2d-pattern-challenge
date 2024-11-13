import json, math
from decimal import Decimal, getcontext

getcontext().prec = 1000000


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
    """Writes content to a file."""
    with open(filename, 'w') as f:
        # Escreve o número em notação científica com 3 casas decimais
        x, y = content
        f.write(f"X={x:.3E}, Y={y}\n")
        
        # Escreve o número por extenso
        f.write(f"X={x}, Y={y}\n")

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return str(obj)  
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")


def evaluate_power_of_two(expression):
    """Evaluates a string expression like '2^N' and returns the corresponding value."""
    base, exponent = expression.split('^')
    return Decimal(2) ** int(exponent)


def load_green_lines(content):
    """Load the coordinates of the green lines from a file."""
    lines = content.strip().split(',')

    lower_expr = lines[0].split('=')[1].strip()
    upper_expr = lines[1].split('=')[1].strip()
    
    lower_value = evaluate_power_of_two(lower_expr)
    upper_value = evaluate_power_of_two(upper_expr)

    return lower_value, upper_value

def save_pattern(pattern, filename="data/2d-pattern.json"):
    """Saves the 2D pattern to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(pattern, f, default=decimal_default, indent=4)


def load_pattern(filename="data/2d-pattern.json"):
    """Loads the 2D pattern from a JSON file."""
    try:
        with open(filename, 'r') as f:
            pattern = json.load(f)
        
        filtered_pattern = []
        for point in pattern:
            if "x" in point and "y" in point:
                point["x"] = Decimal(point["x"])
                point["y"] = Decimal(point["y"])
                filtered_pattern.append(point)

        return filtered_pattern

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_root_diff(root_diff, filename="data/2d-pattern.json"):
    """Saves the value of root_diff to the JSON file, without modifying existing data."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        if isinstance(root_diff, Decimal):
            root_diff = str(root_diff)

        data.append({"root_diff": root_diff})

    except FileNotFoundError:
        data = [{"root_diff": root_diff}]
    except json.JSONDecodeError:
        data = [{"root_diff": root_diff}]

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_root_diff(filename="data/2d-pattern.json"):
    """Loads the value of root_diff from the JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        for item in data:
            if "root_diff" in item:
                root_diff = item["root_diff"]
                if isinstance(root_diff, str):
                    root_diff = Decimal(root_diff)
                return root_diff
        
        return None

    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

import json

def read_file(filename):
    """Reads the content of a file."""
    print(f"Reading file: {filename}")
    with open(filename, 'r') as f:
        content = f.read()
    print(f"Read {len(content)} characters from {filename}.")
    return content

def write_file(filename, content):
    """Writes content to a file."""
    print(f"Writing to file: {filename}")
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Written {len(content)} characters to {filename}.")

def save_pattern(pattern, filename="data/2d-pattern.json"):
    """Saves the 2D pattern to a JSON file after validating the pattern format."""
    print(f"Saving pattern to {filename}...")

    for point in pattern:
        if (point["x"] & (point["x"] - 1)) != 0:  # Check if x is not a power of 2
            raise ValueError(f"Invalid x value {point['x']}: It is not a power of 2.")
        if (point["y"] & (point["y"] - 1)) != 0:  # Check if y is not a power of 2
            raise ValueError(f"Invalid y value {point['y']}: It is not a power of 2.")
    
    with open(filename, 'w') as f:
        json.dump(pattern, f)
    print(f"Pattern saved to {filename}.")

def load_pattern(filename="data/2d-pattern.json"):
    """Loads the 2D pattern from a JSON file and validates its contents."""
    print(f"Loading pattern from {filename}...")

    with open(filename, 'r') as f:
        pattern = json.load(f)

    for point in pattern:
        if (point["x"] & (point["x"] - 1)) != 0:
            raise ValueError(f"Invalid x value {point['x']} in loaded pattern: It is not a power of 2.")
        if (point["y"] & (point["y"] - 1)) != 0:
            raise ValueError(f"Invalid y value {point['y']} in loaded pattern: It is not a power of 2.")

    print(f"Pattern loaded from {filename}.")
    return pattern

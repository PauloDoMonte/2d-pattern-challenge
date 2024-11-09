def load_start_coordinate(content):
    """Parses the start coordinate."""
    print("Loading start coordinate...")
    coord = content.strip().split(',')
    x = int(coord[0].split('=')[1])
    y = int(coord[1].split('=')[1])
    print(f"Loaded coordinate: X={x}, Y={y}")
    return x, y

def format_coordinate(x, y):
    """Formats coordinate for display."""
    formatted = f"X={x}, Y={y}"
    print(f"Formatted coordinate: {formatted}")
    return formatted

#core/coordinate.py
import sys
from decimal import Decimal, getcontext

getcontext().prec = 1000000


def load_start_coordinate(content):
    """Parses the start coordinate."""
    print("Loading start coordinate...")
    coord = content.strip().split(',')
    x = Decimal(coord[0].split('=')[1])
    y = Decimal(coord[1].split('=')[1])
    return x, y

def format_coordinate(x, y):
    """Formats coordinate for display."""
    formatted = f"X={Decimal(x):.0f}, Y={Decimal(y):.0f}"
    return formatted

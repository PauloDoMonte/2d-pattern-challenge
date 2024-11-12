#core/coordinate.py


import sys
from decimal import Decimal, getcontext

getcontext().prec = 1000000


def load_start_coordinate(content):
    """Parses the start coordinate."""
    print("Loading start coordinate...")
    lines = content.strip().split('\n')
    
    coord_line = lines[0].strip()
    
    x = Decimal(coord_line.split(',')[0].split('=')[1].strip())
    y = Decimal(coord_line.split(',')[1].split('=')[1].strip())

    return x,y

def load_start_coordinate_(content):
    """Parses the start coordinate."""
    print("Loading start coordinate...")
    lines = content.strip().split('\n')
    
    coord_line = lines[1].strip()
    
    x = Decimal(coord_line.split(',')[0].split('=')[1].strip())
    y = Decimal(coord_line.split(',')[1].split('=')[1].strip())

    return x,y

def format_coordinate(x0, y0, x, y):
    """Formats coordinate for display."""
    formatted = f"X0={x0}, Y0={y0}\nX={x}, Y={y}"
    return formatted


def format_coordinate_(x, y):
    """Formats coordinate for display."""
    formatted = f"X={x}, Y={y}"
    return formatted


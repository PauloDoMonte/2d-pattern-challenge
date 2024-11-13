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

def load_start_termination(filename):
    """Loads the start coordinate from the second line of the file."""
    print("Loading start coordinate...")

    with open(filename, 'r') as f:
        # Lê todas as linhas do arquivo
        lines = f.readlines()

    # Pega a segunda linha do arquivo, que contém os números por extenso
    coord_line = lines[1].strip()

    # Extrai os valores de X e Y, que estão no formato "X=valor, Y=valor"
    x = Decimal(coord_line.split(',')[0].split('=')[1].strip())
    y = Decimal(coord_line.split(',')[1].split('=')[1].strip())

    return x, y


def format_coordinate(x, y):
    """Formats coordinate for display."""
    formatted = f"X={x}, Y={y}"
    return formatted


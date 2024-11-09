import random
from decimal import Decimal, getcontext

getcontext().prec = 1000000

MAX_POINTS = 100
MAX_EXPONENTS = 1000  
MAX_VALUE = Decimal(2) ** 128  

def generate_pattern(max_points=MAX_POINTS):
    """
    Generates a 2D pattern of points using powers of 2.
    """
    pattern = []
    exponents_used = 0

    while len(pattern) < max_points and exponents_used < MAX_EXPONENTS:
        x_exp = random.randint(0, 128)
        y_exp = random.randint(0, 128)
        x = Decimal(2) ** x_exp
        y = Decimal(2) ** y_exp

        pattern.append({"x": x, "y": y})
        exponents_used += 2

    return pattern

def apply_pattern(x, y, pattern, repetitions, lower_bound, upper_bound):
    """
    Applies the pattern for a given number of repetitions, adjusting x and y based on bounds.
    """
    termination_reached = False

    for rep in range(repetitions):
        if rep % 100 == 0:
            print(f"Repetition {rep}/{repetitions}...")
        for point in pattern:
            x += point["x"]
            y += point["y"]

            if lower_bound <= x <= upper_bound:
                termination_reached = True
                break

        if termination_reached:
            break

        if x > upper_bound:
            x = upper_bound
        elif x < lower_bound:
            x = lower_bound

    return x, y if termination_reached else (x, y)

def reverse_pattern(x, y, pattern, repetitions, lower_bound, upper_bound):
    """
    Reverses the pattern to compute the starting coordinates.
    """
    print(f"Starting reverse pattern calculation from termination coordinates...")
    
    for rep in range(repetitions):
        print(f"Repetition {rep + 1}/{repetitions}...")
        
        for i, point in enumerate(reversed(pattern)):
            # Convert point["x"] and point["y"] to Decimal if they are still strings
            point_x = Decimal(point["x"]) if isinstance(point["x"], str) else point["x"]
            point_y = Decimal(point["y"]) if isinstance(point["y"], str) else point["y"]

            x -= point_x
            y -= point_y

            if x > upper_bound:
                print(f"Adjusting x back from upper bound")
                x = upper_bound
            elif x < lower_bound:
                print(f"Adjusting x back from lower bound")
                x = lower_bound

    print(f"Reversed pattern complete. Starting coordinates")
    return x, y


def is_termination_between_green_lines(x, lower_bound, upper_bound):
    """
    Checks if x is between the green lines.
    """
    return lower_bound <= x <= upper_bound

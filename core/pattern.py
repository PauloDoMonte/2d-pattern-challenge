import random
from decimal import Decimal

MAX_POINTS = 5000
MAX_EXPONENTS = 500

def generate_pattern(lower_bound, upper_bound, max_points=MAX_POINTS):
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
    Applies the 2D pattern to the coordinates (x, y) for a given number of repetitions.
    Adjusts direction based on whether x is above or below the bounds, and stops when a limit is reached.
    """
    print("Starting apply_pattern...")

    direction = 'down'

    if x > upper_bound:
        direction = 'down'
        
    elif x < lower_bound:
        direction = 'up'

    for rep in range(repetitions):
        for point in pattern:
            if x == lower_bound or x == upper_bound:
                print(f"Limit reached: x, stopping pattern application.")
                return x, y

            if direction == 'down':
                x -= point["x"]
                y -= point["y"]
            elif direction == 'up':
                x += point["x"]
                y += point["y"]

    print("apply_pattern finished.")
    return x, y

def reverse_pattern(x, y, pattern, repetitions, lower_bound, upper_bound):
    """
    Reverses the application of the 2D pattern to the coordinates (x, y).
    Adjusts based on whether x is closer to the upper bound or lower bound:
    - If closer to the upper bound, apply 'up' direction (move back).
    - If closer to the lower bound, apply 'down' direction (move back).
    """
    print("Starting reverse_pattern...")

    if abs(x - upper_bound) < abs(x - lower_bound):
        direction = 'up'
        print(f"x is closer to upper bound, moving 'up'.")
    else:
        direction = 'down'
        print(f"x is closer to lower bound, moving 'down'.")

    for rep in range(repetitions):
        for point in reversed(pattern):
            if direction == 'up':
                x += point["x"]
                y += point["y"]
            elif direction == 'down':
                x -= point["x"]
                y -= point["y"]

    print("reverse_pattern finished.")
    return x, y

import random
from decimal import Decimal

MAX_POINTS = 1000
MAX_EXPONENTS = 500

def generate_pattern(initial_x, initial_y, lower_bound, upper_bound, max_points=MAX_POINTS):
    """
    Generates a 2D pattern of points using powers of 2, ensuring the first x stays within bounds
    and aligns to the nearest valid power of 2 within the bounds.
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
    x0, y0 = x, y
    adjustment_difference = 0

    if x < lower_bound:
        adjusted_x = lower_bound
        x = find_next_power_of_2(adjusted_x, direction='up', upper_bound=upper_bound)
        adjustment_difference = x - x0
    elif x > upper_bound:
        adjusted_x = upper_bound
        x = find_next_power_of_2(adjusted_x, direction='down', lower_bound=lower_bound)
        adjustment_difference = x - x0

    for rep in range(repetitions):
        for point in pattern:
            x += point["x"]
            y += point["y"]

    return adjustment_difference, y0, x, y

def reverse_pattern(x, y, pattern, repetitions, lower_bound, upper_bound):
    """
    Reverses the pattern to compute the starting coordinates, adjusting based on termination-coord.txt.
    """
    try:
        with open('data/termination-coord.txt', 'r') as file:
            lines = file.readlines()
            coord_line = lines[0].strip()
    
            x0 = Decimal(coord_line.split(',')[0].split('=')[1].strip())
            y0 = Decimal(coord_line.split(',')[1].split('=')[1].strip())
    except FileNotFoundError:
        x0, y0 = x, y

    adjustment_difference = x0

    for rep in range(repetitions):
        for point in reversed(pattern):
            x -= point["x"]
            y -= point["y"]

    if x == upper_bound:
        x = x - adjustment_difference
    elif x == lower_bound:
        x = x + adjustment_difference

    return x, y

def is_power_of_two(x):
    """Checks if the value is a power of 2."""
    if x <= 0:
        return False
    int_x = int(x)
    return (int_x & (int_x - 1)) == 0

def find_next_power_of_2(value, direction, lower_bound=None, upper_bound=None):
    """
    Finds the nearest power of 2 relative to the given value, either upwards or downwards,
    ensuring it stays within the specified bounds.
    """
    attempts = 0
    value = Decimal(value)
    
    if value <= 0:
        raise ValueError("Value must be greater than 0.")

    int_value = int(value.to_integral_value(rounding='ROUND_FLOOR'))

    if direction == 'up':
        next_power = 1 << int_value.bit_length()
    elif direction == 'down':
        next_power = 1 << (int_value.bit_length() - 1)
    else:
        raise ValueError("Direction must be 'up' or 'down'.")

    current = Decimal(next_power)

    while True:
        attempts += 1

        if lower_bound is not None and current < lower_bound:
            current *= 2
        elif upper_bound is not None and current > upper_bound:
            current /= 2
        else:
            if not is_power_of_two(current):
                pass
            else:
                return current

        if attempts > 1000:
            break

    return current

import random
from decimal import Decimal

MAX_POINTS = 1000
MAX_EXPONENTS = 500

def generate_pattern(lower_bound, upper_bound, max_points=MAX_POINTS):
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
    Applies the 2D pattern to the coordinates (x, y) for a given number of repetitions.
    """
    print("Starting apply_pattern...")
    x0, y0 = x, y

    adjusted_x, root_diff = find_next_power_of_2(x, lower_bound, upper_bound, direction='down')
    x = adjusted_x
    
    for rep in range(repetitions):
        for point in pattern:
            x += point["x"]
            y += point["y"]

    print("apply_pattern finished.")
    return x, y, root_diff

def reverse_pattern(x, y, pattern, repetitions, lower_bound, upper_bound, root_diff):
    """
    Reverses the application of the 2D pattern to the coordinates (x, y).
    """
    print("Starting reverse_pattern...")
    for rep in range(repetitions):
        for point in reversed(pattern):
            x -= point["x"]
            y -= point["y"]

    x = reverse_to_original(x, lower_bound, upper_bound, root_diff)

    print("reverse_pattern finished.")
    return x, y

def is_power_of_two(x):
    """
    Checks if the value is a power of 2.
    """
    if x <= 0:
        return False
    int_x = int(x)
    return (int_x & (int_x - 1)) == 0

def find_next_power_of_2(x, lower_bound, upper_bound, direction='up'):
    """
    Adjusts x to the nearest power of 2 within the bounds.
    """
    x_int = int(x)

    if direction == 'up':
        next_power = 1 << x_int.bit_length()
    elif direction == 'down':
        next_power = 1 << (x_int.bit_length() - 1)
    elif direction == 'nearest':
        next_power_up = 1 << x_int.bit_length()
        next_power_down = 1 << (x_int.bit_length() - 1)

        if abs(next_power_up - x) < abs(next_power_down - x):
            next_power = next_power_up
        else:
            next_power = next_power_down
    else:
        raise ValueError("Direction must be 'up', 'down', or 'nearest'.")

    root_diff = abs(next_power - x)

    return next_power, root_diff

def reverse_to_original(x, lower_bound, upper_bound, root_diff):
    """
    Reverses the adjustment of x by the root_diff to restore the original value.
    """
    print("Starting reverse_to_original...")
    if x > lower_bound:
        x += root_diff
    else:
        x -= root_diff

    print("reverse_to_original finished.")
    return x

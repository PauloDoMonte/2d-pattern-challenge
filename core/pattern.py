import random
from decimal import Decimal

MAX_POINTS = 1000
MAX_EXPONENTS = 500

def generate_pattern(initial_x, initial_y, lower_bound, upper_bound, max_points=MAX_POINTS):
    """
    Generates a 2D pattern of points using powers of 2, ensuring the first x stays within bounds
    and aligns to the nearest valid power of 2 within the bounds. The first adjustment point is saved in a file.
    """
    pattern = []
    exponents_used = 0

    if initial_x < lower_bound:
        adjusted_x = lower_bound + (lower_bound - initial_x)
        adjustment = find_next_power_of_2(adjusted_x, direction='up', upper_bound=upper_bound)
        with open("data/nivelate.txt", "w") as file:
            file.write(f"{adjustment - initial_x}\n")

    elif initial_x > upper_bound:
        adjusted_x = abs(upper_bound - (initial_x - upper_bound))
        adjustment = find_next_power_of_2(adjusted_x, direction='down', lower_bound=lower_bound)
        with open("data/nivelate.txt", "w") as file:
            file.write(f"{adjustment - initial_x}\n")
            
    else:
        pass

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
    with open("data/nivelate.txt", "r") as file:
        first_adjustment = Decimal(file.readline().strip())

    x += first_adjustment
    for rep in range(repetitions):
        if rep % 100 == 0:
            print(f"Repetition {rep}/{repetitions}...")

        for point in pattern:
            x += point["x"]
            y += point["y"]

    print(f"Termination reached")
    return x, y


def reverse_pattern(x, y, pattern, repetitions):
    """
    Reverses the pattern to compute the starting coordinates.
    """
    print(f"Starting reverse pattern calculation from termination coordinates...")
    
    with open("data/nivelate.txt", "r") as file:
        first_adjustment = Decimal(file.readline().strip())

    x -= first_adjustment
    for rep in range(repetitions):
        if rep % 100 == 0:
            print(f"Repetition {rep}/{repetitions}...")
        
        for point in reversed(pattern):
            x -= point["x"]
            y -= point["y"]

    print(f"Reversed pattern complete. Starting coordinates")
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
                print(f"Warning: The found value {current} is not a valid power of 2.")
            else:
                print(f"Valid power of 2 found in {attempts} attempts")
                return current

        if attempts > 10000:
            print("Exceeded maximum attempts.")
            break

    return current

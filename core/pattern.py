import random

MAX_POINTS = 100
MAX_EXPONENTS = 1000  
MAX_VALUE = 2**128  

def generate_pattern(max_points=MAX_POINTS):
    """
    Generates a 2D pattern with points represented as powers of 2 (2^N).
    """

    print("Generating pattern...")
    pattern = []
    exponents_used = 0 

    while len(pattern) < max_points and exponents_used < MAX_EXPONENTS:
        x_exp = random.randint(0, 128)  
        y_exp = random.randint(0, 128)  
        x = 2 ** x_exp
        y = 2 ** y_exp

        pattern.append({"x": x, "y": y})
        exponents_used += 2  

    print(f"Generated {len(pattern)} points in the pattern.")
    print(f"Used {exponents_used} exponents.")
    return pattern

def apply_pattern(x, y, pattern, repetitions):
    """
    Applies the pattern to calculate the termination coordinates.
    """

    print(f"Applying pattern for {repetitions} repetitions...")
    for rep in range(repetitions):
        if rep % 100 == 0:
            print(f"Repetition {rep}/{repetitions}...")
        for point in pattern:
            x += point["x"]
            y += point["y"]
            if is_termination_between_green_lines(x):
                print(f"Termination reached at {x}, {y}.")
                return x, y
    print(f"Finished applying pattern, final position: {x}, {y}.")
    return x, y

def reverse_pattern(x, y, pattern, repetitions):
    """
    Reverses the pattern to calculate the start coordinates.
    """

    print(f"Reversing pattern for {repetitions} repetitions...")
    for rep in range(repetitions):
        if rep % 100 == 0:
            print(f"Repetition {rep}/{repetitions}...")
        for point in reversed(pattern):
            x -= point["x"]
            y -= point["y"]
    print(f"Reversed pattern, initial position: {x}, {y}.")
    return x, y

def is_termination_between_green_lines(x):
    """
    Checks if x is between the green lines.
    """
    
    lower_bound = 2**575100
    upper_bound = 2**602100
    return lower_bound <= x <= upper_bound

import random

MAX_POINTS = 5000
MAX_EXPONENTS = 500
TOLERANCE=0

def generate_pattern(max_points=MAX_POINTS):
    """
    Generates a 2D pattern of points using powers of 2, working directly with exponents.
    """
    pattern = []
    exponents_used = 0

    while len(pattern) < max_points and exponents_used < MAX_EXPONENTS:
        x_exp = random.randint(1, 32) * 2 # Exponent for X
        y_exp = random.randint(1, 32) * 2 # Exponent for Y

        pattern.append({"x": x_exp, "y": y_exp})
        exponents_used += 2

    return pattern

def apply_pattern(x, y, pattern, repetitions, lower_bound, upper_bound, tolerance=TOLERANCE):
    """
    Applies the 2D pattern to the coordinates (x, y) for a given number of repetitions.
    Adjusts direction based on whether x is closer to the upper bound or lower bound,
    and stops when a limit is reached.
    If the limit is not reached within the tolerance, the function calls itself again
    to continue applying the pattern.
    """
    # Get the exponents of x and y
    x_exp = int(x.logb())
    y_exp = int(y.logb())
    print(f"Starting x: 2^{x_exp} y: 2^{y_exp}")
    print(f"Lower: {lower_bound}, Upper: {upper_bound}")

    # Converting lower and upper bounds from '2^N' strings to exponents
    lower_exp = int(lower_bound.split('^')[1])
    upper_exp = int(upper_bound.split('^')[1])

    # Determine the direction based on proximity to the bounds
    if x_exp > upper_exp:
        direction = 'down'
        print("X is greater than upper bound, moving down.")
    elif x_exp < lower_exp:
        direction = 'up'
        print("X is smaller than lower bound, moving up.")
    else:
        # If x is between the bounds, check which bound it is closer to
        if abs(x_exp - lower_exp) < abs(x_exp - upper_exp):
            direction = 'down'
            print(f"X is closer to the lower bound, moving down.")
        else:
            direction = 'up'
            print(f"X is closer to the upper bound, moving up.")

    for rep in range(repetitions):
        for point in pattern:
            # Get the point's x and y as exponents (not as values of 2^x and 2^y)
            point_x_exp = point["x"]
            point_y_exp = point["y"]
            
            # Check tolerance based on direction
            if direction == 'down' and abs(x_exp - lower_exp) <= tolerance:
                print(f"Limit reached for lower bound: x_exp={x_exp}, stopping pattern application.")
                return x_exp, y_exp
            elif direction == 'up' and abs(x_exp - upper_exp) <= tolerance:
                print(f"Limit reached for upper bound: x_exp={x_exp}, stopping pattern application.")
                return x_exp, y_exp

            # Apply the pattern to x and y
            if direction == 'down':
                x_exp -= point_x_exp
                y_exp -= point_y_exp
            elif direction == 'up':
                x_exp += point_x_exp
                y_exp += point_y_exp

    # If limit not reached, recursively call apply_pattern again
    print(f"Repetitions finished without reaching limit.")





def reverse_pattern(x, y, pattern, repetitions, lower_bound, upper_bound, tolerance=TOLERANCE):
    """
    Reverses the application of the 2D pattern to the coordinates (x, y).
    The goal is to revert x and y back to their initial values, especially y_exp -> 0.
    """
    print("\nStarting reverse_pattern...")

    # Get the exponents of x and y
    x_exp = x
    y_exp = y
    print(f"Starting reversing x: 2^{x_exp} y: 2^{y_exp}")
    print(f"Lower: {lower_bound}, Upper: {upper_bound}")

    lower_exp = int(lower_bound.split('^')[1])
    upper_exp = int(upper_bound.split('^')[1]) 
    
    # Add a tolerance threshold for y_exp
    target_y_exp = 0
    tolerance_threshold = 101  # Allow y_exp to be within a margin of error

    print(f"Initial target for y_exp is {target_y_exp}, with tolerance of {tolerance_threshold}.")

    for rep in range(repetitions):
        for point in reversed(pattern):  # Reverse the pattern
            point_x_exp = point["x"]
            point_y_exp = point["y"]

            # Apply the reverse of the pattern (opposite of apply_pattern)
            x_exp -= point_x_exp
            y_exp -= point_y_exp

            # Stop if y_exp is close to 0 (back to initial)
            if abs(y_exp - target_y_exp) <= tolerance_threshold:
                print(f"Reverted successfully to start: x: 2^{x_exp} y: 2^{y_exp}")
                return x_exp, y_exp

    print(f"Reversal incomplete, last values: x: 2^{x_exp}, y: 2^{y_exp}")
    return x_exp, y_exp


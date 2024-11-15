import random

MAX_POINTS = 5000
MAX_EXPONENTS = 500
TOLERANCE = 0


def generate_pattern(max_points=MAX_POINTS):
    pattern = []
    exponents_used = 0

    while len(pattern) < max_points and exponents_used < MAX_EXPONENTS:
        x_exp = random.randint(0, 128)
        y_exp = random.randint(0, 128)

        pattern.append({"x": x_exp, "y": y_exp})
        exponents_used += 1

    return pattern


def apply_pattern(x, y, pattern, repetitions, lower_bound, upper_bound, tolerance=TOLERANCE):
    x_exp = int(x.logb()) if hasattr(x, 'logb') else x
    y_exp = int(y.logb()) if hasattr(y, 'logb') else y
    print(f"Starting pattern application")

    try:
        lower_exp = int(lower_bound.split('^')[1])
        upper_exp = int(upper_bound.split('^')[1])
    except (IndexError, ValueError):
        raise ValueError("Lower and upper bounds must be in the format '2^N' where N is an integer.")

    if x_exp > upper_exp:
        direction = 'down'
    elif x_exp < lower_exp:
        direction = 'up'
    else:
        if abs(x_exp - lower_exp) < abs(x_exp - upper_exp):
            direction = 'down'
        else:
            direction = 'up'

    for _ in range(repetitions):
        if x_exp > upper_exp:
            return (x_exp, y_exp) if x_exp == upper_exp else None
        for point in pattern:
            point_x_exp = point["x"]
            point_y_exp = point["y"]

            if direction == 'down' and abs(x_exp - lower_exp) <= tolerance:
                return x_exp, y_exp
            elif direction == 'up' and abs(x_exp - upper_exp) <= tolerance:
                return x_exp, y_exp

            if direction == 'down':
                x_exp -= point_x_exp
                y_exp -= point_y_exp
            elif direction == 'up':
                x_exp += point_x_exp
                y_exp += point_y_exp

    print(f"Pattern application completed: x: 2^{x_exp}, y: 2^{y_exp}")
    return x_exp, y_exp


def reverse_pattern(x_exp, y_exp, pattern, repetitions, tolerance=TOLERANCE):
    target_y_exp = 0
    y_tolerance = 0

    print(f"Starting pattern reversal with coordinates: x: 2^{x_exp}, y: 2^{y_exp}")

    for _ in range(repetitions):
        for point in reversed(pattern):
            point_x_exp = point["x"]
            point_y_exp = point["y"]

            if y_exp > 0:
                x_exp -= point_x_exp
                y_exp -= point_y_exp
            else:
                x_exp += point_x_exp
                y_exp += point_y_exp

            if y_exp == target_y_exp:
                print(f"Pattern reversal completed: x: 2^{x_exp}, y: 2^{y_exp}")
                return x_exp, y_exp

    print(f"Pattern reversal incomplete: x: 2^{x_exp}, y: 2^{y_exp}")
    return x_exp, y_exp
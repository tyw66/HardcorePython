import math

def are_close_enough(a, b, tolerance=1e-10):
    return math.fabs(a - b) < tolerance

def is_close_to_zero(x, tolerance=1e-10):
    return are_close_enough(x, 0, tolerance)

def is_close_to_one(x, tolerance=1e-10):
    return are_close_enough(x, 1, tolerance)
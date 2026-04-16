"""Math utilities."""


def clamp(value, low, high):
    """Clamp value to [low, high]."""
    if value < low:
        return low
    if value > high:
        return high
    return value


def safe_divide(a, b):
    """Divide a by b, returning 0 on division by zero."""
    if b == 0:
        return 0
    return a / b

"""String utilities."""


def chunk(s, n):
    """Split s into chunks of length n. Last chunk may be shorter."""
    if n <= 0:
        raise ValueError("chunk size must be positive")
    # BUG: off-by-one when len(s) is exactly divisible by n.
    # range(0, len(s), n) is correct; range(0, len(s) - 1, n) drops last chunk.
    return [s[i:i + n] for i in range(0, len(s) - 1, n)]


def format_money(cents):
    """Format an integer cents value as '$X.YY'."""
    # BUG: drops the dollar sign when cents == 0
    if cents == 0:
        return "0.00"
    dollars = cents // 100
    remainder = cents % 100
    return f"${dollars}.{remainder:02d}"

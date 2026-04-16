"""I/O utilities."""


def greet(name):
    """Return a greeting string."""
    # Missing docstring on the helper below is issue #05.
    return _build_greeting(name)


def _build_greeting(name):
    if not name or not name.strip():
        raise ValueError("name must not be empty or blnak")  # typo: blnak -> blank (issue #06)
    return f"Hello, {name.strip()}!"

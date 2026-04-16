from src.math_utils import clamp, safe_divide


def test_clamp_within_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_below():
    assert clamp(-1, 0, 10) == 0


def test_clamp_above():
    assert clamp(20, 0, 10) == 10


# Missing: test_clamp_negative_range (issue #02)


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5


def test_safe_divide_by_zero():
    assert safe_divide(10, 0) == 0

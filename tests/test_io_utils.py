from src.io_utils import greet
import pytest


def test_greet_normal():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty():
    with pytest.raises(ValueError):
        greet("")

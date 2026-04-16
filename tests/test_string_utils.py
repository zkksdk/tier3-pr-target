from src.string_utils import chunk, format_money


def test_chunk_basic():
    assert chunk("abcdef", 2) == ["ab", "cd", "ef"]


def test_chunk_uneven():
    assert chunk("abcde", 2) == ["ab", "cd", "e"]


def test_format_money_normal():
    assert format_money(1050) == "$10.50"

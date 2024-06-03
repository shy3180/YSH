import pytest


def test_base_count():
    seq = "AATC"
    exp = {"A": 2, "C": 1, "T": 1}
    assert base_count(seq) == exp


# 아래는 Paramererize
from add import add


@pytest.makr.parametrize(
    ("seq", "expected"),
    [
        ("AATC", {"A": 2, "C": 1, "T": 1}),
        ("ACGTAAA", {"A": 4, "C": 1, "G": 1, "T": 1}),
    ],
)
def test_base_counter(seq, expected):
    assert base_count(seq) == expected

import pytest


def mat():
    A, B = map(int, input().split())
    return (A + B) * (A - B)

import math
import pytest
from lab8.task1.math_utils import factorial, is_prime, gcd, clamp


@pytest.mark.parametrize('n, expected', [(0, 1), (1, 1), (3, 6), (5, 120), (10, 3628800), (100, math.factorial(100))])
def test_factorial(n, expected):
    result = factorial(n)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize('n', [-1, -5, -100])
def test_factorial_negative(n):
    with pytest.raises(ValueError):
        factorial(n)


@pytest.mark.parametrize('n, expected', [(2, True), (3, True), (17, True), (4, False), (9, False), (25, False), (104729, True), (10**12, False)])
def test_is_prime(n, expected):
    result = is_prime(n)
    assert result is expected
    assert type(result) is bool


@pytest.mark.parametrize('n', [0, 1, -10])
def test_is_prime_invalid(n):
    with pytest.raises(ValueError):
        is_prime(n)


@pytest.mark.parametrize('a, b, expected', [(12, 18, 6), (17, 13, 1), (100, 25, 25), (0, 0, 0), (0, 7, 7), (7, 0, 7), (-12, 18, 6), (-12, -18, 6), (10**30, 10**20, 10**20)])
def test_gcd(a, b, expected):
    result = gcd(a, b)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize('value, lo, hi, expected', [(5, 0, 10, 5), (-2, 0, 10, 0), (20, 0, 10, 10), (0, 0, 10, 0), (10, 0, 10, 10), (3, 2, 2, 2), (-5, -10, -1, -5), (1.5, 0.0, 2.0, 1.5), (10**30, 0, 100, 100)])
def test_clamp(value, lo, hi, expected):
    result = clamp(value, lo, hi)
    assert result == pytest.approx(expected)
    assert isinstance(result, (int, float))


def test_clamp_invalid_bounds():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)

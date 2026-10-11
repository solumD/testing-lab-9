import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 5, 5),
        (0, 0, 0),
        (0.1, 0.2, 0.3),
    ],
)
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
        (6, -3, -2),
        (-6, -3, 2),
        (0, 5, 0),
        (0.3, 0.1, 3),
    ],
)
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [5, -5, 0, 0.5])
def test_divide_by_zero(calculator, a):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(a, 0)


@pytest.mark.parametrize(
    "number, expected",
    [
        (-7, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (9, False),
        (17, True),
        (25, False),
        (49, False),
        (97, True),
    ],
)
def test_is_prime_number(calculator, number, expected):
    assert calculator.is_prime_number(number) is expected

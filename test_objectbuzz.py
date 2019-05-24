import objectbuzz
import pytest


test_equal_pairs = (
    (1, 1), (3, 6), (5, 10)
)

test_not_equal_pairs = (
    (1, 2),
)

@pytest.mark.parametrize("a,b", test_equal_pairs)
def test_fizzbuzzer_equal(a: int, b: int):
    assert objectbuzz.FizzBuzzer(a) == objectbuzz.FizzBuzzer(b)

@pytest.mark.parametrize("a,b", test_not_equal_pairs)
def test_fizzbuzzer_not_equal(a: int, b: int):
    assert objectbuzz.FizzBuzzer(a) != objectbuzz.FizzBuzzer(b)

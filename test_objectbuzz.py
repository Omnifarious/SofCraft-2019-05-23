import objectbuzz


def test_fizz_1():
    assert objectbuzz.FizzBuzzer(1) == objectbuzz.FizzBuzzer(1)


def test_fizz_1_2():
    assert objectbuzz.FizzBuzzer(1) != objectbuzz.FizzBuzzer(2)

def test_fizz_3_6():
    assert objectbuzz.FizzBuzzer(3) == objectbuzz.FizzBuzzer(6)
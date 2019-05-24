import objectbuzz


fizz = objectbuzz.FizzBuzzer(3)
buzz = objectbuzz.FizzBuzzer(5)
fizzbuzz = objectbuzz.FizzBuzzer(15)
for i in range(1, 100):
    fbi = objectbuzz.FizzBuzzer(i)
    if fbi == fizz:
        print("Fizz")
    elif fbi == buzz:
        print("Buzz")
    elif fbi == fizzbuzz:
        print("FizzBuzz")
    else:
        print(i)

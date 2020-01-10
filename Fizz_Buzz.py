def fizz_buzz(number):
    fizz_check = number % 3
    buzz_check = number % 5

    if fizz_check == 0:
        print("Fizz")
    if buzz_check == 0:
        print("Buzz")
    if buzz_check != 0 and fizz_check != 0:
        print(number)

print("Name Jeff")
fizz_buzz(11)
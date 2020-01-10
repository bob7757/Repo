list_numbers = [16, 2, 16, 4, 4, 6]
list_numbers.sort()
number_compared = list_numbers[0]
for number in list_numbers[1:]:
    if number == number_compared:
        list_numbers.remove(number)
    number_compared = number
print(list_numbers)

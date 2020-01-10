entering = True
numbers_list = []
total = 0.0
count = 0
while entering:
    number_add = input("Please enter a number. To delete the last number type 'delete'. To average type 'done'.")
    if number_add.replace(".", "").isnumeric():
        numbers_list.append(number_add)
    elif number_add == "done":
        entering = False
    elif number_add == "delete":
        print(f"{numbers_list[-1]} removed.")
        numbers_list.pop()
    else:
        print(f"Please enter a number.")
else:
    for number in numbers_list:
        total += float(number)
        count += 1
final = input(f"The average of your numbers is {float(total / count)}! To see the list of numbers type 'list'.")
if final == 'list':
    print(numbers_list)
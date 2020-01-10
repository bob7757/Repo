weight = input("How much do you weigh? ")
if weight.isalpha():
	print("Please only enter numbers.") ;
else:
 weight = float(weight); unit = input("(L)b or (K)g?")
 unit = unit.lower()
 if unit == "l":
  print(f"Your weight is {weight / 2.2} Kg")
 elif unit == "k":
  print(f"Your weight is {weight * 2.2} Lb")
 else:
  print("please only enter L or K.")
minimum_number = 1
maximum_number = 1000
next_guess = 500
total_guesses = 0
print("Choose a number between 0 and 1000. I get 10 guesses!")
while total_guesses < 10:
 first_guess = input(f"Is your number (e)qual to (h)igher or (l)ower than {next_guess}?")
 first_guess = first_guess.lower()
 if first_guess == "h":
  minimum_number = next_guess + 1
  next_guess = (maximum_number - minimum_number) // 2 + minimum_number
  total_guesses += 1
 elif first_guess == "l":
  maximum_number = next_guess - 1
  next_guess = (maximum_number - minimum_number) // 2 + minimum_number
  total_guesses += 1
 elif first_guess == "e":
  print("Thanks for playing! You Lose!")
  break
 else:
   print(f"Please only enter 'e', 'h', or 'l', for equal, higher, or lower respectively." )
if first_guess != "e":
  print("Cheater!")
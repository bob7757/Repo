import random
secret_number = random.randint(1,10)
guesses = 0
guess_limit = 3
while guesses < guess_limit:
  guesses += 1
  guess = int(input("Guess a number between 1 and 10! "))
  if guess > 10 or guess < 1:
    guesses -= 1
    print("Please only enter numbers between 1 and 10.")
  if guess == secret_number:
    print("You Win!")
    break
else:
  print("You Suck, the Answer Was " + str(secret_number))
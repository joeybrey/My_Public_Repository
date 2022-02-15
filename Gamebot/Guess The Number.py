import random
import math

choose_range = input("What is the maximum number in the range you want to guess? \n")

guesses_left = math.ceil(int(choose_range) / 4)
print("You will have {} incorrect guesses.".format(guesses_left))

print("I'm thinking of a number. Go ahead and guess.")

number = random.randint(0, int(choose_range))


while guesses_left > 0:
	if 
	guess = int(input("Guess a number. \n"))
	if guess > number:
		guesses_left -= 1
		print("Your guess is high. You have {} guesses left. \n".format(guesses_left))
	if guess < number:
		guesses_left -= 1
		print("Your guess is low. You have {} guesses left. \n".format(guesses_left))
	if guess == number:
		print("You got it!")
else: 
	print("Sorry, game over. Play again!")

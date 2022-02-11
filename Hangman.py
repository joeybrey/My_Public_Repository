import random
from tkinter import Y

correct = []
incorrect = []

def none_incorrect():
	print(" 0 ")
	print("/|\ ")
	print(" /\ ")

def correct_guess():
	correct.append(guess)
	print("Good guess! {} is in the word.".format(guess))


def incorrect_guess():
	guesses_left = 6
	guesses_left -= 1
	print("Ooh sorry, it looks like {} is not in the word I'm thinking of. You have {} guesses left".format(str(guess), str(guesses_left)))
	incorrect.append(guess)
guesses_left = incorrect_guess()
def make_guess():
	if guess in correct:
		print("You've already guessed that letter, silly!")
	elif guess in incorrect:
		print("You've already guessed that letter, silly!")
	elif guess in word:
		correct_guess()
	else:
		incorrect_guess()

def post_guess():
	print("Here are the letters you got correct: {}".format(correct))
	print("Here are the letters you got incorrect: {}".format(incorrect))
	print("Make another guess!")

print("\nWelcome to hangman! I'm going to think of a word and I'll let you guess letters until you compose the word. You have 6 incorrect guesses. Let's play!")
ready_or_not = input("Ready? [Y/N] \n")
if ready_or_not.lower() == "y":
	while guesses_left > 0:
		words = ["jessica", "joey", "eva", "laney", "david", "marissa"]
		word = random.choice(words)
		guess = input("Guess a letter. \n")
		make_guess()
		post_guess()
		guess = input("Guess a letter. \n")
		make_guess()
		post_guess()
		guess = input("Guess a letter. \n")
		make_guess()
		post_guess()
		guess = input("Guess a letter. \n")
		make_guess()
		post_guess()
		guess = input("Guess a letter. \n")
		make_guess()
		post_guess()
		guess = input("Guess a letter. \n")
	if guesses_left == 0:
		print("It looks like you're all out of guesses! Good game. Please play again.")
elif ready_or_not.lower() == "n":
	print("Okay, come back whenever you are ready to play :) \n")	
else:
	print("Sorry, that is not a correct input. Please rerun the program and type 'y' or 'n'. \n ")
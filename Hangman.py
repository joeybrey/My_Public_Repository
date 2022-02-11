import random
from tkinter import Y

correct = []
incorrect = []

def none_incorrect():
	print(" 0 ")
	print("/|\ ")
	print(" /\ ")

def prompt_guess():
	guess = input("Guess a letter. \n")
	return guess

def correct_guess():
	correct.append(guess)
	print("Good guess! {} is in the word.".format(guess))

def incorrect_guess():
	already_guessed = "Oops, you've already guessed that letter! Guess another one."
	if guess not in word and guess not in correct:
		incorrect.append(guess)
		print("Ooh sorry, it looks like {} is not in the word I'm thinking of. Guess again.".format(guess))

def post_guess():
	print("Here are the letters you got correct: {}".format(correct))
	print("Here are the letters you got incorrect: {}".format(incorrect))
	print("Make another guess!")

print("Welcome to hangman! I'm going to think of a word and I'll let you guess letters until you compose the word. You have 6 incorrect letters. Let's play!")
ready_or_not = input("Ready? \n[Y/N] \n")
if ready_or_not.lower() == "y":
	words = ["jessica", "joey", "eva", "laney", "david", "marissa"]
	word = random.choice(words)
	prompt_guess()
	if guess in word:
		correct_guess()
	else:
		incorrect_guess()
elif ready_or_not.lower() == "n":
	print("Okay, come back whenever you are ready to play :) \n")	
else:
	print("Sorry, that is not a correct input. Please rerun the program and type 'y' or 'n'. \n ")
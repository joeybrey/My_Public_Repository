#MAKE GAMEBOT WITH MAD LIBS AND NUMBER GUESSING GAME

import random

correct = []
incorrect = []
guesses_left = 6
words = ["jessica", "joey", "eva", "laney", "david", "marissa"]
word = random.choice(words)
good_synonyms = ["fantastic", "great", "wonderful", "marvelous", "exceptional"]
def correct_guess(guess):
	if guess == word:
		print("Yes! You guessed the word! {} job.".format(random.choice(good_synonyms)))
def make_guess(guess):
	if guess in incorrect:
		print("You've already guessed {}, silly!".format(guess))
		print("Here are the letters you got correct: {}".format(correct))
		print("Here are the letters you got incorrect: {}".format(incorrect))
	elif guess in correct:
		print("You've already guessed {}, silly!".format(guess))
		print("Here are the letters you got correct: {}".format(correct))
		print("Here are the letters you got incorrect: {}".format(incorrect))
	elif guess in word:
		print("Yes! There is a(n) {} in the word!".format(guess))
		correct.append(guess)
		print("Here are the letters you got correct: {}".format(correct))
		print("Here are the letters you got incorrect: {}".format(incorrect))
	else:
		incorrect.append(guess)
		global guesses_left
		if guesses_left > 0:
			guesses_left -= 1
			print("Ooh sorry, it looks like {} is not in the word I'm thinking of. You have {} guesses left.".format(guess, str(guesses_left)))
			print("Here are the letters you got correct: {}".format(correct))
			print("Here are the letters you got incorrect: {}".format(incorrect))
			return guesses_left
print("\nWelcome to hangman! I'm going to think of a word and I'll let you guess letters until you compose the word. You have 6 incorrect guesses. Let's play!")	
ready_or_not = input("Ready? [Y/N] \n")
if ready_or_not.lower() == "y":
	while guesses_left > 0:
		guess = input("Guess a letter. \n\n")
		if guess == word:
			correct_guess(guess)
		else:
			make_guess(guess)
	else:
		print("You are all out of guesses! Thank you for playing.")
elif ready_or_not.lower() == "n":
	print("Okay, come back whenever you are ready to play :) \n")	
else:
	print("Sorry, that is not a correct input. Please rerun the program and type 'y' or 'n'. \n ")

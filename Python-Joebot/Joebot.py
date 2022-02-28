game_selection = input("Hi, I'm Joebot! What would you like to do? \n[A] Hangman \n[B] Tip Calculator \n[C] Repeat After Me \n[D] Budgeting \n[E] Mad Libs \n[F] Blackjack \n[G] Guess The Number")

if game_selection == "a":
	import hangman
elif game_selection == "b":
	import tip_calculator_function
elif game_selection == 'c':
	import repeat_after_me
elif game_selection == 'd':
	import month_to_month
elif game_selection == 'e':
	import mad_libs
elif game_selection == 'f':
	import blackjack
elif game_selection == 'g':
	import guess_the_number
	

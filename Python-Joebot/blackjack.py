import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(input("Welcome, have a seat. Ready to play some Blackjack?"))
print("Alright! Here is your first card...")

draw1 = random.choice(cards)

tally = 0

tally = tally + draw1
player_choice = input("What would you like to do? /n[1] Hit /n[2] ")

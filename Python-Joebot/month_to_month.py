bank_balance = int(input("What is your bank balance?\n"))
payday = int(input("How much will you get on payday?\n"))
paydays_left = int(input("How many paydays do you have left this month?\n"))
shared_credit_card = int(input("What is the balance of your shared credit card?\n"))
personal_credit_card = int(input("How much do you owe on your personal credit card?"))

save_this_month = bank_balance + (payday * paydays_left) - personal_credit_card - (shared_credit_card / 2)

print("You will have ${} left over at the end of this month".format(round(save_this_month, 2)))
if save_this_month > 0:
	print("Good Job!")
else:
	print("Make a budget for next month!")

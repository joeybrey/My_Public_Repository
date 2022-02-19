bank_balance = 0
payday = 0
paydays_left = 0
shared_credit_card = 0
apple_credit_card = 0

save_this_month = bank_balance + (payday * paydays_left) - apple_credit_card - (shared_credit_card / 2)
print(round(save_this_month, 2))

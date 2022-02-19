def bill(cost, tip):
	total = cost * (1 + tip)
	tip_total = tip * cost
	print("The bill is " + str(cost))
	print("The total tip is " + str(round(tip_total, 2)))
	print("The total bill is " + str(round(total, 2)))
bill(63.48, .225)

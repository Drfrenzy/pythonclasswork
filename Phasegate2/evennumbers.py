for number in range(999, 3001):

	number1 = number // 999

	number2 = number // 100 % 10

	number3= number // 10 % 10

	number4 = number % 10

	if(number1 % 2 == 0 and number2 % 2 == 0 and number3 % 2 == 0 and number4 % 2 == 0):

		print(number, end=", ")


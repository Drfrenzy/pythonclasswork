import math

def divide_or_square(number):
	if not isinstance(number, int):
		raise TypeError("Input must be an integer")
	if number % 5 == 0:
		return math.sqrt(number)
	else:
		return number % 5

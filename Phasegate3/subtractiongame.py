import random

print("WELCOME TO THE SUBTRACTION PROBLEM GAME")

correct_answer = 0
right_guess = 0
wrong_guess = 0
times = 1

while times <=10:
	random_number1 = random.randint(50, 100)
	random_number2 = random.randint(1, 50)

	print(f"Please Enter Answer to the question {random_number1} - {random_number2} = ")

	question_answer = int(input(""))

	correct_answer = random_number1 - random_number2
		
	if question_answer== correct_answer:
		print("Correct answer Good job!!!!")
		right_guess+=1
	else:
		print("Wrong answer work harder!!!!")
		wrong_guess+=1
	times+=1
  
print(f"total Right answer: {right_guess} times, total wrong answer: {wrong_guess} times")
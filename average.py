'''
   prompt user to input first number
   store as number 1
   prompt user to input second number
   store as number 2
   prompt user to input third number
   store as number 3
   sum all collected numbers together
   divide the sum of the numbers by 3
   print result
                            '''

number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))

 
sum = number1 + number2 + number3

average = sum / 3

print("the average of the numbers is:", round(average,0))
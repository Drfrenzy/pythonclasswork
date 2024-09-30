
User_Number = int(input("Please Enter Digits between 0 and 1000: "))
sum_of_userinput = 0


while User_Number > 0:
    sum_of_userinput += User_Number % 10  
    User_Number //= 10         

print("The sum of the digits is:", sum_of_userinput)

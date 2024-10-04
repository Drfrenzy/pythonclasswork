even_sum = 0
odd_sum = 0
sum = 0
for rang in range(10):
        number = int(input(f"Please Enter Number between the range 1 & 50 {rang + 1}: "))
        sum += number
        if (rang + 1) % 2 == 0:
         even_sum += number
        if (rang + 1) % 2 ==  1:
         odd_sum += number
Average = sum / 10
print("Sum of scores at even index:", even_sum)
print("Sum of scores at odd index:", odd_sum)
print("Average of all the Elements is: ", Average)
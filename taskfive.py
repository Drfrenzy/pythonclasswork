even_number_sum = 0
sum_scores = 0
for i in range(10):
        score = int(input(f"Enter score {i + 1}: "))
        sum_scores += score
        average = sum_scores / 2        
        if score % 2 == 0:
            even_number_sum += score

print("Sum of scores of even numbers:", even_number_sum)
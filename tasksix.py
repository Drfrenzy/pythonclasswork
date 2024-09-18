even_number_sum = 0
sum_scores = 0
for i in range(10):
        score = int(input(f"Enter score {i + 1}: "))
        sum_scores += score        
        if score % 2 == 0:
            even_number_sum += score
        average = even_number_sum / 2
print("Average of scores of even numbers:", average)
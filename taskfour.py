even_index_sum = 0
sum_scores = 0
for i in range(10):
        score = int(input(f"Enter score {i + 1}: "))
        sum_scores += score
        average = sum_scores / 2
        if (i + 1) % 2 == 0:
            even_index_sum += score
print("Sum of scores at even indexes:", even_index_sum)
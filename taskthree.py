sum_scores = 0
for i in range(10):
        score = int(input(f"Enter score {i + 1}: "))
        sum_scores += score
        average = sum_scores / 2
print("Sum:", sum_scores)
print("Average:", average)

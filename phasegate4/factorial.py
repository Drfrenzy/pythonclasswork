def findfactorial(number):
  sum_factorial = 0
  for digit in range(1, number):
    factorial = number * digit
    sum_factorial += (factorial)
  print("The total sum of the factors is: ", sum_factorial)

findfactorial(7)


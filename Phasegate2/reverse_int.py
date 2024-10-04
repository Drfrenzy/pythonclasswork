def reverse(numbers):
	reverse_number = ''
	for number in range(len(numbers)-1, -1, -1):
		reverse_number += numbers[number]
	return reverse_number
print(reverse('456'))

def is_palindrome(number):
   if(reverse(numbers) == reverse_numbers):
      print("Number is palindrome")
   else: 
     print("Number is not a palindrome")
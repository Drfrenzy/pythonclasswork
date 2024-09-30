
integer1 = int(input("Enter first digit: "))
integer2 = int(input("Enter second digit: "))
integer3 = int(input("Enter third digit: "))


if integer1 > integer2:
    integer1, integer2 = integer2, integer1
if integer1  > integer3:
    integer1, integer3 = integer3, integer1
if integer2 > integer3:
    integer2, integer3 = integer3, integer2

print("This are the Digits in increasing order:", integer1, integer2, integer3)

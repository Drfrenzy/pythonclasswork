number = 7
for line in range(1, number +1):
 for lenght in range(1, line, 1):
     if lenght % 2 == 0:
      print("*", end= " ")
     else: 
      print(lenght, end= " ")

 print()

for line in range(number, 0, -1):
 for lenght in range(1, line, 1):
     if lenght % 2 == 0:
      print("*", end= " ")
     else: 
      print(lenght, end= " ")

 print()




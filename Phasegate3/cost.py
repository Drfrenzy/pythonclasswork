cost_of_car: int(input("PLEASE ENTER THE COST OF THE CAR: "))

if cost_of_car > 0 and cost_of_car <= 2500000:
   Tarrif_5 = (5/100)* cost_of_car
   print("Duty charge percentage on your car is 5%: ", Tarrif_5)
elif cost_of_car > 2500000 and cost_of_car <= 5000000:
   Tarrif_10 = (10/100)* cost_of_car
   print("DUTY CHARGE PERCENTAGE ON YOUR CAR IS: ", Tarrif_10)
elif cost_of_car > 5000000 and cost_of_car <= 10000000:
   Tarrif_15 = (15/100)* cost_of_car
   print("DUTY CHARGE PERCENTAGE ON YOUR CAR IS: ", Tarrif_15)
elif cost_of_car > 10000000:
   Tarrif_20 = (20/100)* cost_of_car
   print("DUTY CHARGE PERCENTAGE ON YOUR CAR IS: ", Tarrif_20)


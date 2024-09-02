pizza_details = {
    1: {"name": "Sapa", "slices": 4, "price": 2000},
    2: {"name": "Small Money", "slices": 6, "price": 2400},
    3: {"name": "Big Boys", "slices": 8, "price": 3000},
    4: {"name": "Odogwu", "slices": 12, "price": 4200}
}


number_of_people = int(input("Enter number of people ordering for: "))


print("Select the pizza type desired:")
print("1. Sapa")
print("2. Small Money")
print("3. Big Boys")
print("4. Odogwu")

pizza_choice = int(input("Enter choice: "))


if pizza_choice not in pizza_details:
    print("Invalid choice entered.")
else:
    pizza = pizza_details[pizza_choice]
    slices_per_box = pizza["slices"]
    price_per_box = pizza["price"]

    
    boxes_needed = (number_of_people + slices_per_box - 1) // slices_per_box  # Ceiling division
    total_slices = boxes_needed * slices_per_box
    leftover_slices = total_slices - number_of_people
    total_cost = boxes_needed * price_per_box

   
    print(f"Pizza type selected: {pizza['name']}")
    print(f"Number of boxes of pizza to buy: {boxes_needed}")
    print(f"Number of leftover slices: {leftover_slices}")
    print(f"Total cost: NGN{total_cost}")

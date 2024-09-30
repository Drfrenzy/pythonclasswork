days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


Today = int(input("Please Enter Today's Date: "))
Number_days = int(input("Please Enter Number of Days after Today for a future day: "))

future_day = (Today + Number_days) % 7

print(f"Today is {days_of_the_week[Today]} and the future day is {days_of_the_week[future_day]}")
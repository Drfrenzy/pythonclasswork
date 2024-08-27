''' 
  prompt user to input principal amount
  store as principal amount
  prompt user to input annual interest
  store as annual interest
  prompt user to input duration
  store as duration
  calculate monthly rate using formula
  display the monthly rate
  
                                  '''
 

principal_amount = int(input("Enter Principal Amount: "))
annual_interest = float(input("Enter Annual interest rate: "))
duration = int(input("Enter duration of loan in years: "))
rate1 = annual_interest * ( 1 + annual_interest ) ** duration
rate2 = (1 + annual_interest )** duration - 1
rate_divide = rate1 / rate2
monthly_rate = principal_amount * rate_divide
print("Monthly interest rate is: #", round(monthly_rate,2))
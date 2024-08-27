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
 

principal_amount = float(input("Enter Principal Amount: "))
annual_interest = float(input("Enter Annual interest rate: "))
duration = int(input("Enter duration of loan in years: "))

monthly_rate = (annual_interest / 100) / 12
duration_of_loan = duration * 12
rate  = 1 + monthly_rate

total_rate = rate ** duration_of_loan
monthly_payment = (principal_amount * monthly_rate * total_rate) / (total_rate -1)
print("Monthly interest rate is: #", round(monthly_payment,2))
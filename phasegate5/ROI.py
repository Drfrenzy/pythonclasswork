investment_amount = float(input("Please Enter investment amount: " "#"))
number_of_years = int(input("Please Enter Number of years of investment: "))
percentage_annually = float(input("Please Enter percentage: "))

added_annually= 0
added_roi = 0
print(f"YEAR\tROI\t\t AMOUNT")

for roi in range(1, number_of_years+1):
 if investment_amount < 0:
   print("Invalid Amount")
   break
 ROI_annually = (percentage_annually / 100) * investment_amount
 added_annually += ROI_annually
 added_roi = investment_amount + ROI_annually
 investment_amount = added_roi
 print(f"{roi}\t#{added_annually:,.2f}\t#{added_roi:,.2f}") 
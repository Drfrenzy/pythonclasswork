print("PERSONAL INCOME TAX CALCULATOR")

print("""

       1 --> Single filers
       2 --> Married filling jointly
       3 --> Married filling separately
       4 --> Head of Household

                           """)
user_selection = int(input("Select Category you fall under: "))
salary_annually = int(input("Enter annual salary for calculation: "))

match user_selection: 
      case 1: if salary_annually > 0 and salary_annually <= 8_350:
                percentage10 = (10/100) * salary_annually
              elif salary_annually > 8_351 and salary_annually <= 33_950:
                percentage15 = (15/100) * salary_annually
              elif salary_annually > 33_951 and salary_annually <= 82_250:
                percentage15 = (25/100) * salary_annually
              elif salary_annually > 82_251 and salary_annually <= 171_550:
                percentage15 = (28/100) * salary_annually
              elif salary_annually > 171_551 and salary_annually <= 372_950:
                percentage15 = (33/100) * salary_annually
              elif salary_annually > 372_951
                percentage15 = (35/100) * salary_annually
              
      case 2: print("Married filing jointly")
      case 3: print("Married filing separately")
      case 4: print("Head of Household")
      case _: print("Invalid input please check input and try again")

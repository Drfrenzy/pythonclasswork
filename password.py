''' 
  prompt user to input username
  store as username
  prompt user to input password
  store password 
  count the number of letters in the variable
  use the len function 
  display the username
  display the result in asterisks
                                  '''

username = input("Enter your username: ")

userpassword = input("Enter your password: ")

count = len(userpassword)

password = "*"

display = count * password

print("Username:",  username)

print("Password:", display)
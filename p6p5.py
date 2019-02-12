password = str(input("Please set your password: "))
attempt = str(input("Please enter your password to log in: "))
if password == attempt:
    print("You have succesfully logged in.")
    exit()
else:
    print("Sorry, the password is wrong.")
    print("For security purposes, you will now be asked your password three times. Enter your password only once each time.")
    attempt = password
    y = 1
    while y <= 3 and attempt == password:
        attempt = str(input("Please enter your password to log in: "))
        y += 1

if attempt == password:
    print("You have succesfully logged in.")
    exit()

else:
    print("You have been denied access.")
    exit()



    

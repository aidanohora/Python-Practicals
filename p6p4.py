x = 1
password = str(input("Please set your password: "))
attempt = "notset" #this needs to be set now so that the loop can close early on a succesful attempt

while x <= 3 and attempt != password:
    attempt = str(input("Please enter your password to log in: "))
    x += 1

if password == attempt:
    print("You have succesfully logged in.")
    exit()
    
if x >= 3:
    print("You have been denied access")
    exit()

    

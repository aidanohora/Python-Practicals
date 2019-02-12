def isleapyear(year):
    '''takes a positive integer and returns True is a leap year
        Otherwise returns False'''
    if year % 4 != 0:
        return False
    elif year % 100 == 0:    
        if year % 400 != 0:
            return False
        else:
            return True
    else:
        return True  

year = int(input("Please enter a year (positive integers only): "))
if year <= 0:
    print("Error: Non-positive integer entered.")
elif isleapyear(year) == True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

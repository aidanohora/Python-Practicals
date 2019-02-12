firstno = int(input("Please enter a number: "))
secondno = int(input("Please enter another number: "))
thirdno = int(input("Please enter one more number: "))

if firstno%2 != 0:
    highestno = firstno

elif secondno%2 != 0 and secondno > firstno:
    highestno = secondno

elif thirdno%2 != 0 and thirdno > secondno:
    highestno = thirdno

                                        
if (firstno%2 != 0) or (secondno%2 != 0) or (thirdno%2 != 0):
    print(highestno)

else:
    print("No odd numbers have been entered.")
    exit()





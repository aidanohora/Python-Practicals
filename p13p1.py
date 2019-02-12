#Program to print out the largest of two numbers entered by the user
#Uses a function max

def max(a,b):
    """Function that returns the largest of its two arguements"""
    if a > b:
        return a
    else:
        return b

#Prompt user for two numbers
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))

largest = max(number1, number2)

print("Larger of ", number1, " and ", number2, " is ", largest)

print("Finished!")

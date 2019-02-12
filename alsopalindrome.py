import sys

def isPal(string):
    '''A function that takes a string to check if it's a palindrome
        return True if a palindrome or False otherwise'''
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and isPal(string[1:-1])

print("*** Program to check whether a string is a palindrome ***")
while True:
    string = str(input("Enter string (enter an empty string to exit): "))
    string =  string.lower()
    word = ""
    for i in string:
        if i in "abcdefghijklmnopqrstuvwxyz":
            word += str(i)
    string = word
    if string == "":
        print("Exiting program...")
        sys.exit(0)
    elif isPal(string) == True:
        print(string, "is a palindrome.")
    else:
        print(string, "is not a palindrome.")
        
        
        



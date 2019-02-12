import sys
def isPal(word):
    '''function to check if a string is a palindrome'''
    word = word.lower()
    newstring = ""
    for i in word:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            newstring += i
    if len(newstring) <= 1:
        return True
    else:
        return newstring[0] == newstring[-1] and isPal(newstring[1:-1])
stringinput = "string"
while len(stringinput)>0:
    stringinput = input("Enter a string to check if it's a palindrome (empty string to quit): ")
    if stringinput == "":
        print("Quitting program...")
        sys.exit(0)
    elif isPal(stringinput) == True:
        print(stringinput, "is a palindrome.")
    else:
        print(stringinput, "is not a palindrome.")
            

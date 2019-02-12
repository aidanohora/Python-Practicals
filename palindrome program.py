def isPal(string):
    '''function to check if a string is a palindrome'''
    string = string.lower()
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and isPal(string[1:-1])
        
word = "i"
while word != "":
    word = str(input("Please enter a word: "))
    if word == "":
        print("Empty string entered - exiting program...")
    elif isPal(word) == True:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
    
    

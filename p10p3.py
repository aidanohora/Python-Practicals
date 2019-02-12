import sys
word = input("Enter the word (enter nothing to end the program): ")
if word == "":
    print("Program exiting...")
    sys.exit()
count=0
while word!="":
    for i in word:
        if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
            count+=1
    print("The number of vowels is:",count)
    word = input("Enter the word: ")
    if word == "":
        print("Program exiting...")
        sys.exit()

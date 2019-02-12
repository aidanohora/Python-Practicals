number = int(input("Enter a number: "))

a = 0

while number >= 0:
    for i in range(1,number+1):
        a+=i
    print(a)
    a=0
    number = int(input("Enter a number: "))




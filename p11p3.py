stop_number = 1
c = 0
b = 0
a = 1

while stop_number >= 0:
    fibonacci = 0
    stop_number = int(input("Enter the number for which you wish to calculate the fibonacci series up to: "))
    a = 1
    b = 0
    c = 0
    while fibonacci < stop_number:
        c = a + b
        fibonacci = c
        if fibonacci < stop_number:
            print(fibonacci)
        a = c + b
        fibonacci = a
        if fibonacci < stop_number:
            print(fibonacci)
        b = a + c
        fibonacci = b
        if fibonacci < stop_number:
            print(fibonacci)



    
    


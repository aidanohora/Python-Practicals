N = int(input("Enter the integer to calculate the number of Catalan Numbers of: "))
n = 0
catalan = 1

if N == 0:
    print("Catalan Numbers:", int(catalan))


else:
    while n < N:
        catalan = ((2*((2*n)+1))/(n+2))*catalan
        n += 1
    print("Catalan Numbers:", int(catalan))



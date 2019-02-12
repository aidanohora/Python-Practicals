number = int(input("Please enter a positive integer: "))
sumoffactors = 0

for i in range (1, number + 1):
    for j in range (1, i):
        if i % j == 0:
            sumoffactors += j
    if sumoffactors == i:
        print(sumoffactors)
    sumoffactors = 0

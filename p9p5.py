n = int(input("Enter the number of possible toppings: "))
k = int(input("Enter the standard number of toppings: "))
x = n - k

if n == 0:
    N = 1
elif n == 1:
    N = 1
else:
    N = 1
    i = 1
    while i <= n:
        N *= i
        i += 1

if k == 0:
    K = 1
elif k == 1:
    K = 1
else:
    K = 1
    j = 1
    while j <= k:
        K *= j
        j += 1

if x == 0:
    X = 1
elif x == 1:
    X = 1
else:
    X = 1
    g = 1
    while g <= x:
        X *= g
        g += 1

total_combinations = N/(K*X)

print("Total number of combination toppings is", total_combinations)

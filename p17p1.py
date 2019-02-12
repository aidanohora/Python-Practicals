def findDivisors(num):
    """Finds the common divisors of num1 and num2
    Assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""

    divisors = (1, num)
    for i in range(2, (num//2)+1):
        if num % i == 0:
            divisors += (i,)

    return divisors

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Numbers should be > 0.")

else:
    divisors = findDivisors(number)
    print("The divisors of", number, "are:", divisors)

    total = 0
    for d in divisors:
        total += d
    print("Sum of the divisors of", number, "is:", total)

print("Finished!")

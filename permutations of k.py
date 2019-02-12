def factorial(number):
    
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1
        
    return(factorial)

k = int(input("Please enter a total number of items: "))
n = int(input("Please enter a number of items to be selected: "))

if n <= 0 or k <= 0:
    print("Error: Please only enter positive integers.")

else:
    factn = factorial(n)
    facta = factorial(n-k)

    permutations = factn / facta

    print("Number of permutations is: ", permutations) 
    

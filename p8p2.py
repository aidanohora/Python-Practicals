table_size = int(input("Enter the size of the table (must be an integer): "))

i = 1
while i <= table_size:
    j = 1
    while j <= table_size:
        print(i*j, " ", end = "")
        j += 1
    print()
    i += 1

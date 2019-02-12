table_size =int(input("blah"))
while table_size > 0:
    print("******************")
    for i in range (1, table_size+1, 1):
        for j in range(1, i+1, 1):
            print (1*j, " ", end = "")
        print()
    print("******************")
    print()
    table_size = int(input("blah"))
print("Program finished")

    

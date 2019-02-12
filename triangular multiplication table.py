import sys
table_size = 1
while table_size > 0:
    table_size = int(input("Enter table-size: "))
    if table_size <= 0:
        sys.exit()
    else:
        i=1
        while i<=table_size:
            j=1
            while j<=i:
                print(j*i, " ", end="")
                j+=1
            print()
            i+=1 
        print("*********")

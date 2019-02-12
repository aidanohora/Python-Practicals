euro_pound_conversion = 0.89 #According to google on 25.09.2018

euro_amount = float(input("Enter the amount in Euro to be converted: "))

if euro_amount < 0:
    print("Amount must be >= 0. Please try again.")

else:
    pound_amount = euro_amount*euro_pound_conversion
    print("Amount in pound sterling:", pound_amount)

income = float(input("Enter an amount of income: "))

if income < 0:
    print("Amount of income must be >= 0. Please try again.")
    
else:
    income_at_lower = (income/100)*60

    income_at_higher = (income/100)*40

    tax_due_lower = income_at_lower*0.23

    tax_due_higher = income_at_higher*0.41

    total_tax = tax_due_lower + tax_due_higher

    net_income = income - total_tax

    print("Initial amount:", income)

    print("Lower tax rate is 23%")

    print("Amount taxed at lower rate:", income_at_lower)

    print("Higher tax rate is 41%")

    print("Amount taxed at higher rate:", income_at_higher)

    print("Total tax due:", total_tax)

    print("Net income:", income - total_tax)





amount = float(input("Enter the amount before tax: "))
amount_taxed_at_higher_rate = amount*0.4
amount_taxed_at_lower_rate = amount*0.6
tax_from_lower_rate = amount_taxed_at_lower_rate*0.135
tax_from_higher_rate = amount_taxed_at_higher_rate*0.23
total_tax_due = tax_from_lower_rate + tax_from_higher_rate
print("Amount before tax:", amount)
print("Total tax:", total_tax_due) 
print("Amount with tax:", amount + total_tax_due)

income = float(input("Enter your income: "))
tax_rate = float(input("Enter the tax rate: "))
my_taxes = income * tax_rate
net_income = income - my_taxes 
print(f"Your net income is {net_income}") 
print(type(net_income))
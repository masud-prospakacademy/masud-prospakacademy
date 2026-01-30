
cash_str = input("Enter your total cash savings: ")
cash = float(cash_str)

gold_str = input("Enter the total value of your gold (in your local currency): ")
gold = float(gold_str)

business_str = input("Enter the value of your business inventory: ")
business = float(business_str)

total_wealth = cash + gold + business

# Calculate Zakat (2.5% is equivalent to 0.025)
zakat_due = total_wealth * 0.025


# We use :,.2f to add both a comma for thousands and 2 decimal places
print("-" * 30)
print(f"Total Zakatable Wealth: ${total_wealth:,.2f}")
print(f"Zakat Due (2.5%):        ${zakat_due:,.2f}")
print("-" * 30)
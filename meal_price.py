# Creative addition: I added an optional tip percentage that is calculated and included in the final total.

# Ask for meal prices
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))



# Ask for quantities
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate subtotal
subtotal = (child_price * num_children) + (adult_price * num_adults)

print(f"\nSubtotal: ${subtotal:.2f}\n")

# Ask for sales tax rate
tax_rate = float(input("What is the sales tax rate? "))

# Calculate sales tax and total
sales_tax = subtotal * (tax_rate / 100)
total = subtotal + sales_tax

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}\n")

# Creative addition: tip
tip_rate = float(input("What percentage would you like to tip? "))
tip_amount = total * (tip_rate / 100)
final_total = total + tip_amount

print(f"Tip: ${tip_amount:.2f}")
print(f"Final Total: ${final_total:.2f}\n")

# Ask for payment
payment = float(input("What is the payment amount? "))

# Calculate change
change = payment - final_total

print(f"Change: ${change:.2f}")

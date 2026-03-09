# Creative addition: I added input validation for prices and actions, and improved formatting so prices align neatly when displayed.

items = []
prices = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("Please enter an action: ")

    # ADD ITEM
    if action == "1":
        item = input("What item would you like to add? ")
        
        while True:
            try:
                price = float(input(f"What is the price of '{item}'? "))
                break
            except ValueError:
                print("Please enter a valid price.")

        items.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")

    # VIEW CART
    elif action == "2":
        if len(items) == 0:
            print("Your shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

    # REMOVE ITEM
    elif action == "3":
        if len(items) == 0:
            print("Your shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

            try:
                remove_index = int(input("Which item would you like to remove? ")) - 1
                if 0 <= remove_index < len(items):
                    items.pop(remove_index)
                    prices.pop(remove_index)
                    print("Item removed.")
                else:
                    print("Sorry, that is not a valid item number.")
            except ValueError:
                print("Please enter a valid number.")

    # COMPUTE TOTAL
    elif action == "4":
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    # QUIT
    elif action == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")

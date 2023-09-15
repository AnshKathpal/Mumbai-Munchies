from main import Snack
from inventory import Inventory

# Create an instance of the Inventory class
inventory = Inventory()

# Add snacks to the inventory
inventory.addSnack(1, "Chips", 1.99, True, 10)  # Example: Initial quantity is 10
inventory.addSnack(2, "Soda", 1.49, True, 15)  # Example: Initial quantity is 15
inventory.addSnack(3, "Candy", 0.99, False, 10)  # Example: Initial quantity is 0

# Get and print all snacks in the inventory
all_snacks = inventory.get_all_snacks()
for snack_details in all_snacks:
    print(snack_details)

# Record a sale
inventory.record_sale(1, 2)  # Record 2 units of Chips (Snack with ID 1)


# Get and print all snacks in the inventory again
all_snacks = inventory.get_all_snacks()
for snack_details in all_snacks:
    print(snack_details)

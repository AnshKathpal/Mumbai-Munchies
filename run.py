import pyfiglet
from inventory import Inventory
from main import select_user_role
import login


text = pyfiglet.figlet_format("Welcome to Mumbai Munchies", width=150)
updated = pyfiglet.figlet_format("Snack Updated")

# Create an instance of the Inventory class
inventory = Inventory()

if __name__ == "__main__":
    print(text)

    if login.login():
        # print("Login successful!")
        user_role = select_user_role()
        inventory.set_current_user_role(user_role)

        inventory.load_inventory_from_file("inventory_data.txt")

        while True:
            # Display menu options
            print("+--------------------+")
            print("+       Menu         +")
            print("+--------------------+")
            print("+ 1. Add Snack       +")
            print("+--------------------+")
            print("+ 2. Update Snack    +")
            print("+--------------------+")
            print("+ 3. Remove Snack    +")
            print("+--------------------+")
            print("+ 4. Record Sale     +")
            print("+--------------------+")
            print("+ 5. Show All Snacks +")
            print("+--------------------+")
            print("+ 6. Bulk Update     +")
            print("+--------------------+")
            print("+ 7. Bulk Remove     +")
            print("+--------------------+")
            print("+ 8. Save & Exit     +")
            print("+--------------------+")

            choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

            if choice == '1':
                if inventory.can_add_snack():
                    id = int(input("Enter Snack ID: "))
                    name = input("Enter Snack Name: ")
                    price = float(input("Enter Snack Price: "))
                    availability = input(
                        "Is the Snack Available (True/False): ")
                    quantity = int(input("Enter Snack Quantity: "))
                    category = input(
                        "Enter Category from (beverages/snacks/desserts): ")
                    inventory.addSnack(
                        id, name, price, availability, quantity, category)
                else:
                    print(
                        "---------------------------------------------------------------------")
                    print(
                        "Permission denied. You don't have the required role for this action.")
                    print(
                        "---------------------------------------------------------------------")

            elif choice == '2':
                if inventory.can_update_snack():
                    id = int(input("Enter Snack ID to update: "))
                    updated_availability = input(
                        "Enter Updated Availability (True/False): ").capitalize()
                    updated_quantity = int(input("Enter Updated Quantity: "))
                    for category, snacks in inventory.snacks.items():
                        for snack in snacks:
                            if snack.id == id:
                                snack_found = True
                                snack.update_availability(
                                    updated_availability, updated_quantity)
                                print(
                                    "--------------------------------------------")
                                print(
                                    f"Availability for Snack with ID {id} updated to {updated_availability} and quantity to {updated_quantity}.")
                                print(
                                    "--------------------------------------------")
                                print(updated)
                                break
                            else:
                                print(
                                    "--------------------------------------------")
                                print(
                                    f"No snack with ID {id} found in the inventory.")
                                print(
                                    "--------------------------------------------")
                else:
                    print(
                        "---------------------------------------------------------------------")
                    print(
                        "Permission denied. You don't have the required role for this action.")
                    print(
                        "---------------------------------------------------------------------")

            elif choice == '3':
                if inventory.can_remove_snack():
                    inventory.removeSnack(id)
                else:
                    print(
                        "---------------------------------------------------------------------")
                    print(
                        "Permission denied. You don't have the required role for this action.")
                    print(
                        "---------------------------------------------------------------------")

            elif choice == '4':
                if inventory.can_record_sale():
                    snack_id = int(input("Enter Snack ID for sale: "))
                    quantity_sold = int(input("Enter Quantity Sold: "))
                    inventory.record_sale(snack_id, quantity_sold)
                else:
                    print(
                        "---------------------------------------------------------------------")
                    print(
                        "Permission denied. You don't have the required role for this action.")
                    print(
                        "---------------------------------------------------------------------")

            elif choice == '5':
                all_snacks = inventory.get_all_snacks()
                for snack_details in all_snacks:
                    print("--------------------------------------------")
                    print(snack_details)
                    print("--------------------------------------------")

            elif choice == '6':
                if inventory.can_update_snack():
                    inventory.bulk_update_snacks()
                else:
                    print(
                        "---------------------------------------------------------------------")
                    print(
                        "Permission denied. You don't have the required role for this action.")
                    print(
                        "---------------------------------------------------------------------")

            elif choice == '7':
                if inventory.can_remove_snack():
                    inventory.bulk_remove_snacks()
                else:
                    print(
                        "---------------------------------------------------------------------")
                    print(
                        "Permission denied. You don't have the required role for this action.")
                    print(
                        "---------------------------------------------------------------------")

            elif choice == '8':
                print("--------------------------------------------")
                print("Exiting the program.")
                print("--------------------------------------------")
                inventory.save_inventory_to_file("inventory_data.txt")
                break

            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Login Failed, Exiting!")

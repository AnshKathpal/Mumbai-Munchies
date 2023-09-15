# from main import Snack
import pyfiglet
from inventory import Inventory
from main import select_user_role


text = pyfiglet.figlet_format("Welcome to Mumbai Munchies", width = 150)
updated = pyfiglet.figlet_format("Snack Updated")



#font_names = pyfiglet.FigletFont.getFonts()

#for font_name in font_names:
    #print(font_name)

# Create an instance of the Inventory class
inventory = Inventory()

user_role = select_user_role()  
inventory.set_current_user_role(user_role)  

inventory.load_inventory_from_file("inventory_data.txt")


while True:
    print("----------------------------------------------------------------------------")
    print(text)
    print("----------------------------------------------------------------------------")
    print("\nMenu:")
    print("----------")
    print("1. Add Snack")
    print("---------------")
    print("2. Update Snack")
    print("------------------")
    print("3. Remove Snack")
    print("------------------")
    print("4. Record Sale")
    print("-----------------")
    print("5. Show All Snacks")
    print("---------------------")
    print("6. Bulk Update")
    print("---------------------")
    print("7. Bulk Remove")
    print("---------------------")
    print("8. Exit")
    print("----------")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':

        if inventory.can_add_snack():

            id = int(input("Enter Snack ID: "))
            name = input("Enter Snack Name: ")
            price = float(input("Enter Snack Price: "))
            availability = input("Is the Snack Available (True/False): ")
            quantity = int(input("Enter Snack Quantity: "))
            category = input("Enter Category from (beverages/snacks/desserts): ")
            inventory.addSnack(id, name, price, availability, quantity ,category)
        else:
            print("---------------------------------------------------------------------")
            print("Permission denied. You don't have the required role for this action.")
            print("---------------------------------------------------------------------")

    elif choice == '2':

        if inventory.can_update_snack():

            id = int(input("Enter Snack ID to update: "))
            updated_availability = input("Enter Updated Availability (True/False): ").capitalize()  # Capitalize user input
            updated_quantity = int(input("Enter Updated Quantity: "))
            for snack in inventory.snacks:
                if snack.id == id:
                    snack.update_availability(updated_availability, updated_quantity)
                    print("--------------------------------------------")
                    print(f"Availability for Snack with ID {id} updated to {updated_availability} and quantity to {updated_quantity}.")
                    print("--------------------------------------------")
                    print("------------------------>")
                    print(updated)
                    print("------------------------>")
                    break
                else:
                    print("--------------------------------------------")
                    print(f"No snack with ID {id} found in the inventory.")
                    print("--------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("Permission denied. You don't have the required role for this action.")
            print("---------------------------------------------------------------------")

    elif choice == '3':

         if inventory.can_remove_snack():
            inventory.removeSnack(id)
         else:
            print("---------------------------------------------------------------------")
            print("Permission denied. You don't have the required role for this action.") 
            print("---------------------------------------------------------------------")  

    elif choice == '4':
        if inventory.can_record_sale():
            snack_id = int(input("Enter Snack ID for sale: "))
            quantity_sold = int(input("Enter Quantity Sold: "))
            inventory.record_sale(snack_id, quantity_sold)
        else:
            print("---------------------------------------------------------------------")
            print("Permission denied. You don't have the required role for this action.")
            print("---------------------------------------------------------------------")

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
            print("---------------------------------------------------------------------")
            print("Permission denied. You don't have the required role for this action.")
            print("---------------------------------------------------------------------") 


    elif choice == '7':  
        if inventory.can_remove_snack():
            inventory.bulk_remove_snacks()
        else:
            print("---------------------------------------------------------------------")
            print("Permission denied. You don't have the required role for this action.")
            print("---------------------------------------------------------------------")         

    elif choice == '8':
        print("--------------------------------------------")
        print("Exiting the program.")
        print("--------------------------------------------")
        inventory.save_inventory_to_file("inventory_data.txt")
        break

    else:
        print("Invalid choice. Please select a valid option.")

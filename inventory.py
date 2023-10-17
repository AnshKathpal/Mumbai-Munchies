# Inventory Management

from main import Snack, AdminRole, CanteenStaffRole, CashierRole
from sales import SalesRecord
import pyfiglet

added = pyfiglet.figlet_format("Snack Added")
already = pyfiglet.figlet_format("Snack Already Exists")
removed = pyfiglet.figlet_format("Snack Removed")
sale = pyfiglet.figlet_format("Snack Sold") 


class Inventory:
    def __init__(self):
        self.snacks = {}
        # self.snacks = []
        self.sales_records = []
        self.current_user_role = None
        # self.load_inventory_from_file("inventory_data.txt")

    def set_current_user_role(self, user_role):
        self.current_user_role = user_role

    def can_add_snack(self):
        if self.current_user_role:
            return self.current_user_role.can_add_snack()
        return False

    def can_update_snack(self):
        if self.current_user_role:
            return self.current_user_role.can_update_snack()
        return False

    def can_remove_snack(self):
        if self.current_user_role:
            return self.current_user_role.can_remove_snack()
        return False

    def can_record_sale(self):
        if self.current_user_role:
            return self.current_user_role.can_record_sale()
        return False

    def addSnack(self, id, name, price, availability, quantity, category):
        if category not in self.snacks:
            self.snacks[category] = []
        for snack in self.snacks[category]:
            if snack.id == id:
                print("------------------------------------------------")
                print(f"A snack with ID {id} already exists.")
                print("------------------------------------------------")
                print("------------------------")
                print(already)
                print("------------------------")
                return

        snack = Snack(id=id, name=name, price=price,
                      availability=availability, quantity=quantity, category=category)
        # self.snacks.append(snack)
        self.snacks[category].append(snack)
        print("------------------------------------------------")
        print(
            f"Snack with id {id} is added to {category} category in the inventory.")
        print("------------------------------------------------")
        print("------------------------>")
        print(added)
        print("------------------------>")

    def removeSnack(self, id):
        snack_details = self.get_all_snacks()
        if not snack_details:
            print("------------------------------------------------")
            print("No snacks in the inventory to remove.")
            print("------------------------------------------------")
            return
        print("------------------------------------------------")
        print("Snack Details:")
        for snack_detail in snack_details:
            print(snack_detail)
        print("------------------------------------------------")
        id = int(input("Enter the ID of the snack you want to remove: "))
        snack_to_remove = None
        for category, snacks in self.snacks.items():
            for snack in snacks:
                if snack.id == id:
                    snack_to_remove = snack
                    break
        if snack_to_remove:
            confirmation = input(
                f"Are you sure you want to remove snack with ID {id}? (yes/no): ").strip().lower()
            if confirmation == "yes":
                self.snacks[snack_to_remove.category].remove(snack_to_remove)
                print("------------------------------------------------")
                print(
                    f"Snack with ID {id} has been removed from the inventory.")
                print("------------------------------------------------")
                print("------------------------>")
                print(removed)
                print("------------------------>")
            else:
                print("------------------------------------------------")
                print("Snack removal canceled.")
                print("------------------------------------------------")
        else:
            print("------------------------------------------------")
            print(f"No snack with ID {id} found in the inventory.")
            print("------------------------------------------------")

    def bulk_update_snacks(self):
        print("Bulk Update Snacks:")
        category = input(
            "Enter Category to update (beverages/snacks/desserts): ").strip()
        if category not in self.snacks:
            print(f"No snacks found in the '{category}' category.")
            return

        updated_availability = input(
            "Enter Updated Availability (True/False): ").capitalize()
        updated_quantity = int(input(
            "Enter Updated Quantity: "))

        for snack in self.snacks[category]:
            snack.update_availability(updated_availability,updated_quantity)

        print("--------------------------------------------")
        print(
            f"Availability for all snacks in the '{category}' category updated to {updated_availability}.")
        print("--------------------------------------------")

    def bulk_remove_snacks(self):
        print("Bulk Remove Snacks:")
        snack_details = self.get_all_snacks()
        if not snack_details:
            print("------------------------------------------------")
            print("No snacks in the inventory to remove.")
            print("------------------------------------------------")
            return
        print("------------------------------------------------")
        print("Snack Details:")
        for snack_detail in snack_details:
            print(snack_detail)
        print("------------------------------------------------")
        category = input(
            "Enter Category to remove snacks from (beverages/snacks/desserts): ").strip()
        if category not in self.snacks:
            print(f"No snacks found in the '{category}' category.")
            return

        snacks_to_remove = self.snacks[category][:]
        # ids_to_remove = input("Enter IDs of snacks to remove (comma-separated): ").strip().split(',')
        # for id in ids_to_remove:
        #     id = int(id.strip())
        #     for snack in self.snacks[category]:
        #         if snack.id == id:
        #             snacks_to_remove.append(snack)
        #             break

        if snacks_to_remove:
            print("------------------------------------------------")
            print("Snacks to Remove:")
            for snack in snacks_to_remove:
                print(f"ID: {snack.id}, Name: {snack.name}")
            print("------------------------------------------------")

            confirmation = input(
                f"Are you sure you want to remove these snacks? (yes/no): ").strip().lower()
            if confirmation == "yes":
                for snack in snacks_to_remove:
                    self.snacks[category].remove(snack)
                print("------------------------------------------------")
                print("Selected snacks have been removed from the inventory.")
                print("------------------------------------------------")
                print("------------------------>")
                print(removed)
                print("------------------------>")
            else:
                print("------------------------------------------------")
                print("Snack removal canceled.")
                print("------------------------------------------------")
        else:
            print("------------------------------------------------")
            print("No matching snacks found in the inventory.")
            print("------------------------------------------------")

    def get_all_snacks(self):
        snack_details = []
        for category, snacks in self.snacks.items():
            for snack in self.snacks[category]:
                snack_details.append(
                    f" Catagory: {category} -> ID: {snack.id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.available}, Quantity: {snack.quantity}")
        return snack_details

    def record_sale(self, snack_id, quantity_sold):
        snack_found = False
        for category, snacks in self.snacks.items():
            for snack in snacks:
                if snack.id == snack_id:
                    snack_found = True
                    if snack.available == "Yes":
                        if quantity_sold <= 0:
                            print("------------------------------------------------")
                            print(
                                "Invalid quantity. Please enter a positive quantity.")
                            print("------------------------------------------------")
                            return
                        elif snack.quantity < quantity_sold:
                            print("------------------------------------------------")
                            print("Not enough snacks available.")
                            print("------------------------------------------------")
                            return
                    total_amount = snack.price * quantity_sold
                    sale_record = SalesRecord(
                        id=len(self.sales_records) + 1,
                        snack_id=snack.id,
                        quantity=quantity_sold,
                        total_amount=total_amount
                    )
                    self.sales_records.append(sale_record)
                    snack.quantity -= quantity_sold
                    print("------------------------>")
                    print(sale)
                    print("------------------------>")
                    print("------------------------------------------------")
                    print(f"Sale recorded. Total amount: ${total_amount:.2f}")
                    print("------------------------------------------------")
                    return
                if not snack_found:
                    print("------------------------------------------------")
                    print(
                        f"No snack with ID {snack_id} found in the inventory.")
                    print("------------------------------------------------")

    def save_inventory_to_file(self, filename):
        with open(filename, 'w') as file:
            for category, snacks in self.snacks.items():
                 for snack in snacks:
                    file.write(
                    f"{snack.id},{snack.name},{snack.price},{snack.available},{snack.quantity},{snack.category}\n")

    def load_inventory_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    values = line.strip().split(',')
                    if len(values) == 6:
                        id, name, price, available, quantity, category = values
                        id = int(id)
                        price = float(price)
                        quantity = int(quantity)
                        snack = Snack(id, name, price, available, quantity, category)
                        if category not in self.snacks:
                            self.snacks[category] = []
                        self.snacks[category].append(snack)
        except FileNotFoundError:
            pass

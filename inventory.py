# Inventory Management

from main import Snack
from sales import SalesRecord
import pyfiglet

added = pyfiglet.figlet_format("Snack Added")
already = pyfiglet.figlet_format("Snack Already Exists")
removed = pyfiglet.figlet_format("Snack Removed")
sale = pyfiglet.figlet_format("Snack Sold")


class Inventory:
    def __init__(self):
        self.snacks = []
        self.sales_records = []
        self.load_inventory_from_file("inventory_data.txt")

    def addSnack(self, id, name, price, availability, quantity):
        for snack in self.snacks:
            if snack.id == id:
                print("------------------------------------------------")
                print(f"A snack with ID {id} already exists.")
                print("------------------------------------------------")
                print("------------------------")
                print(already)
                print("------------------------")
                return

        snack = Snack(id=id, name=name, price=price, availability=availability, quantity=quantity)
        self.snacks.append(snack)
        print("------------------------------------------------")
        print(f"Snack with id {id} is added to the inventory.")
        print("------------------------------------------------")
        print("------------------------>")
        print(added)
        print("------------------------>")

    def removeSnack(self, id):
        for snack in self.snacks:
            if snack.id == id:
                self.snacks.remove(snack)
                print("------------------------------------------------")
                print(f"Snack with ID {id} has been removed from the inventory.")
                print("------------------------------------------------")
                print("------------------------>")
                print(removed)
                print("------------------------>")
                break
        else:
            print("------------------------------------------------")
            print(f"No snack with ID {id} found in the inventory.")
            print("------------------------------------------------")

    def get_all_snacks(self):
        snack_details = []
        for snack in self.snacks:
            snack_details.append(
                f"ID: {snack.id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.available}, Quantity: {snack.quantity}")
        return snack_details

    def record_sale(self, snack_id, quantity_sold):
        for snack in self.snacks:
            if snack.id == snack_id:
                if snack.available == "Yes":
                    if quantity_sold <= 0:
                        print("------------------------------------------------")
                        print("Invalid quantity. Please enter a positive quantity.")
                        print("------------------------------------------------")
                        return
                elif snack.quantity < quantity_sold:
                    print("------------------------------------------------")
                    print("Not enough snacks available.")
                    print("------------------------------------------------")
                else:
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
                break
        else:
            print("------------------------------------------------")
            print(f"No snack with ID {snack_id} found in the inventory.")
            print("------------------------------------------------")

    def save_inventory_to_file(self, filename):
        with open(filename, 'w') as file:
            for snack in self.snacks:
                file.write(f"{snack.id},{snack.name},{snack.price},{snack.available},{snack.quantity}\n")

    def load_inventory_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    id, name, price, available, quantity = line.strip().split(',')
                    id = int(id)
                    price = float(price)
                    quantity = int(quantity)
                    snack = Snack(id, name, price, available, quantity)
                    self.snacks.append(snack)
        except FileNotFoundError:
            pass


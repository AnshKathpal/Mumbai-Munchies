# Inventory Management

from main import Snack
from sales import SalesRecord
import pyfiglet

added = pyfiglet.figlet_format("Snack Added")
already = pyfiglet.figlet_format("Snack Already Exists")


class Inventory:
    def __init__(self):
        self.snacks = []
        self.sales_records = []

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

        snack = Snack(id=id, name=name, price=price,
                      availability=availability, quantity=quantity)
        self.snacks.append(snack)
        print("------------------------------------------------")
        print(f"Snack with id {id} is added to the inventory.")
        print("------------------------------------------------")
        print("------------------------")
        print(added)
        print("------------------------")

    def removeSnack(self, id):

        for snack in self.snacks:
            if snack.id == id:
                self.snacks.remove(snack)
                print(
                    f"Snack with ID {id} has been removed from the inventory.")
                break
        else:
            print(f"No snack with ID {id} found in the inventory.")

    def get_all_snacks(self):
        snack_details = []
        for snack in self.snacks:
            snack_details.append(
                f"ID: {snack.id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.available} Quantity: {snack.quantity}")
        return snack_details

    def record_sale(self, snack_id, quantity_sold):
        # Find the snack with the specified ID
        for snack in self.snacks:
            if snack.id == snack_id:
                if snack.available == "Yes":
                    if quantity_sold <= 0:
                        print("Invalid quantity. Please enter a positive quantity.")
                elif snack.quantity < quantity_sold:
                    print("Not enough snacks available.")
                else:
                    # Calculate the total amount for the sale
                    total_amount = snack.price * quantity_sold
                    # Create a new sales record
                    sale_record = SalesRecord(
                        id=len(self.sales_records) + 1,
                        snack_id=snack.id,
                        quantity=quantity_sold,
                        total_amount=total_amount
                    )
                    # Add the sales record to the list
                    self.sales_records.append(sale_record)
                    # Update the snack's quantity
                    snack.quantity -= quantity_sold
                    print(
                        f"Sale recorded. Total amount: ${total_amount:.2f}")
            else:
                print("This snack is not available for sale.")
            break
        else:
            print(f"No snack with ID {snack_id} found in the inventory.")

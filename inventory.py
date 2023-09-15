# Inventory Management

from main import Snack


class Inventory:
    def __init__(self):
        self.snacks = []

    def addSnack(self, id, name, price, availability):

        for snack in self.snacks:
            if snack.id == id:
                print(f"A snack with ID {id} already exists.")
                return

        snack = Snack(id=id, name=name, price=price, availability=availability)
        self.snacks.append(snack)
        print(f"Snack with id {id} is added to the inventory.")

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
                f"ID: {snack.id}, Name: {snack.name}, Price: {snack.price}, Availability: {snack.availability}")
        return snack_details

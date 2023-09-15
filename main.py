class Snack:
    def __init__(self, id, name, price, availability, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.available = availability
        self.quantity = quantity

    def update_availability(self,updated_availability, updated_quantity):
        self.available = updated_availability
        self.quantity = updated_quantity

    def get_details(self):
        return f"Snack(Snack_Id={self.id}, Snack Name={self.name}, Snack Price={self.price}, Snack Availability={self.availability} Snack Quantity = {self.quantity})"
    
    def __str__(self):
        return self.get_details()
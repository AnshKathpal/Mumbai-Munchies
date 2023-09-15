class Snack:
    def __init__(self, id, name, price, available):
        self.id = id
        self.name = name
        self.price = price
        self.available = available


    def update_availability(self,updated_availability):
        self.available = updated_availability

    def get_details(self):
        return f"Snack(Snack_Id={self.id}, Snack Name={self.name}, Snack Price={self.price}, Snack Availability={self.available})"
    
    def __str__(self):
        return self.get_details()
class AdminRole: 
    def __init__(self):
        self.role_name = "Admin"

    def can_add_snack(self):
        return True
    def can_update_snack(self):
        return True
    def can_remove_snack(self):
        return True
    def can_record_sale(self):
        return True
    

class CanteenStaffRole:
    def __init__(self):
        self.role_name = "Canteen Staff"

    def can_add_snack(self):
        return True

    def can_update_snack(self):
        return False

    def can_remove_snack(self):
        return False

    def can_record_sale(self):
        return False    
    

class CashierRole:
    def __init__(self):
        self.role_name = "Cashier"

    def can_add_snack(self):
        return False

    def can_update_snack(self):
        return False

    def can_remove_snack(self):
        return False

    def can_record_sale(self):
        return True
    

def select_user_role():
    while True:
        print("+-----------------------+")
        print("|    Available Roles    |")
        print("+-----------------------+")
        print("| 1. Admin              |")
        print("| 2. Canteen Staff      |")
        print("| 3. Cashier            |")
        print("+-----------------------+")
        role_choice = input("Select your role (1/2/3): ")
        if role_choice == '1':
            return AdminRole()
        elif role_choice == '2':
            return CanteenStaffRole()
        elif role_choice == '3':
            return CashierRole()
        else:
            print("--------------------------------------------------")
            print("Invalid role choice. Please select a valid role.")  
            print("--------------------------------------------------")  





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
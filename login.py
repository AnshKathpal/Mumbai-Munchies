users = [
    {"username": "ansh", "password": "ansh"},
    {"username": "admin", "password": "admin"}
]


def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter Password: ")

        user_found = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                user_found = True
                print("Login Successful!!")
                return True
                break
        if not user_found:
            print("Invalid username or password. Please try again.")
            retry = input("Do you want to retry? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Exiting login.")
                return False

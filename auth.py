import database
import file_handler
def client_register():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    database.clients[database.client_id] = {
        "name": name,
        "email": email,
        "password": password
    }
    
    print("Client Registered Successfully")
    print("Your Client ID:", database.client_id)

    database.client_id += 1
    file_handler.save_data()

def freelancer_register():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    skill = input("Enter Skill: ")

    database.freelancers[database.freelancer_id] = {
        "name": name,
        "email": email,
        "password": password,
        "skill": skill
    }
    
    print("Freelancer Registered Successfully")
    print("Your Freelancer ID:", database.freelancer_id)

    database.freelancer_id += 1
    file_handler.save_data()

def client_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    for client_id, details in database.clients.items():
        if details["email"] == email and details["password"] == password:
            print("Login Successful")
            return client_id
    print("Invalid Credentials")
    return None
def freelancer_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    for freelancer_id, details in database.freelancers.items():
        if details["email"] == email and details["password"] == password:
            print("Login Successful")
            return freelancer_id

    print("Invalid Credentials")
    return None

def view_clients():
    if not database.clients:
        print("No Clients Found")
        return

    for client_id, details in database.clients.items():
        print(client_id, details)

def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == "harshini" and password == "harshini123":
        print("Admin Login Successful")
        return True

    print("Invalid Admin Credentials")
    return False
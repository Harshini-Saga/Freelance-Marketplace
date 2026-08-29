# auth.py

import database

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
print("Client ID:", database.client_id)

database.client_id += 1
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
print("Freelancer ID:", database.freelancer_id)

database.freelancer_id += 1

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

def view_clients():
    if not database.clients:
        print("No Clients Found")
    return


for client_id, details in database.clients.items():
    print(client_id, details)


def view_freelancers():
    if not database.freelancers:
        print("No Freelancers Found")
    return
for freelancer_id, details in database.freelancers.items():
    print(freelancer_id, details)


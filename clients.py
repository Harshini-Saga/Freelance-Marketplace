# client.py

import database

def post_project(client_id):
    title = input("Enter Project Title: ")
    description = input("Enter Description: ")
    budget = float(input("Enter Budget: "))

    database.projects[database.project_id] = {
        "title": title,
        "description": description,
        "budget": budget,
        "client_id": client_id,
        "status": "Open"
    }

print("Project Posted Successfully")
print("Project ID:", database.project_id)

database.project_id += 1

def view_my_projects(client_id):
    found = False
    for project_id, project in database.projects.items():
        if project["client_id"] == client_id:
            found = True
            print("\nProject ID:", project_id)
            print("Title:", project["title"])
            print("Description:", project["description"])
            print("Budget:", project["budget"])
            print("Status:", project["status"])

    if not found:
        print("No Projects Found")

def view_bids(client_id):
    found = False
    for project_id, project in database.projects.items():
        if project["client_id"] == client_id:
            if project_id in database.bids:
                found = True
                print("\nProject ID:", project_id)
                print("Project Title:", project["title"])

                for bid in database.bids[project_id]:
                    print("Freelancer ID:", bid["freelancer_id"])
                    print("Bid Amount:", bid["bid_amount"])
                    print("-" * 20)

    if not found:
        print("No Bids Found")

def hire_freelancer(client_id):
    project_id = int(input("Enter Project ID: "))
    freelancer_id = int(input("Enter Freelancer ID: "))
    if project_id in database.projects:
        database.hired_projects[project_id] = {
            "client_id": client_id,
            "freelancer_id": freelancer_id
        }

        database.projects[project_id]["status"] = "Assigned"

        print("Freelancer Hired Successfully")
    else:
        print("Invalid Project ID")


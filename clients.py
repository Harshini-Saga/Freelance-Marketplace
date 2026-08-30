# client.py
import file_handler
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
    file_handler.save_data()
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

    if project_id not in database.projects:
        print("Invalid Project ID")
        return

    if database.projects[project_id]["client_id"] != client_id:
        print("This project does not belong to you")
        return

    if project_id not in database.bids:
        print("No Bids Available")
        return

    print("\n===== FREELANCERS WHO BID =====")

    for bid in database.bids[project_id]:
        freelancer_id = bid["freelancer_id"]

        if freelancer_id in database.freelancers:
            freelancer = database.freelancers[freelancer_id]

            print("\nFreelancer ID:", freelancer_id)
            print("Name:", freelancer["name"])
            print("Skill:", freelancer["skill"])
            print("Bid Amount:", bid["bid_amount"])

    freelancer_id = int(input("\nEnter Freelancer ID to Hire: "))

    if freelancer_id not in database.freelancers:
        print("Invalid Freelancer ID")
        return

    database.hired_projects[project_id] = {
        "client_id": client_id,
        "freelancer_id": freelancer_id
    }

    database.projects[project_id]["status"] = "Assigned"

    file_handler.save_data()

    print("Freelancer Hired Successfully")
def check_project_status(client_id):
    found = False

    for project_id, project in database.projects.items():
        if project["client_id"] == client_id:
            found = True

            print("\nProject ID:", project_id)
            print("Title:", project["title"])
            print("Status:", project["status"])

            if project["status"].lower() == "completed":

                if project_id in database.reviews:
                    print("Review already submitted")
                    continue

                choice = input("Would you like to rate the freelancer? (yes/no): ")

                if choice.lower() == "yes":

                    freelancer_id = database.hired_projects[project_id]["freelancer_id"]

                    rating = int(input("Enter Rating (1-5): "))
                    review = input("Enter Review: ")

                    database.reviews[project_id] = {
                        "client_id": client_id,
                        "freelancer_id": freelancer_id,
                        "rating": rating,
                        "review": review
                    }

                    file_handler.save_data()
                    print("Review Submitted Successfully")

    if not found:
        print("No Projects Found")


# admin.py

import database

def view_clients():
    if not database.clients:
        print("No Clients Found")
        return
    print("\n--- Clients ---")
    for client_id, details in database.clients.items():
        print("Client ID:", client_id)
        print("Name:", details["name"])
        print("Email:", details["email"])
        print("-" * 30)
def view_freelancers():
    if not database.freelancers:
        print("No Freelancers Found")
        return

    print("\n--- Freelancers ---")
    for freelancer_id, details in database.freelancers.items():
        print("Freelancer ID:", freelancer_id)
        print("Name:", details["name"])
        print("Email:", details["email"])
        print("Skill:", details["skill"])
        print("-" * 30)

def view_projects():
    if not database.projects:
        print("No Projects Found")
        return
    print("\n--- Projects ---")
    for project_id, project in database.projects.items():
        print("Project ID:", project_id)
        print("Title:", project["title"])
        print("Budget:", project["budget"])
        print("Status:", project["status"])
        print("Client ID:", project["client_id"])
        print("-" * 30)
def view_bids():
    if not database.bids:
        print("No Bids Found")
        return

    print("\n--- Bids ---")
    for project_id, bid_list in database.bids.items():
        print("Project ID:", project_id)

        for bid in bid_list:
            print("Freelancer ID:", bid["freelancer_id"])
            print("Bid Amount:", bid["bid_amount"])

        print("-" * 30)


def view_hired_projects():
    if not database.hired_projects:
        print("No Hired Projects Found")
        return

    print("\n--- Hired Projects ---")
    for project_id, details in database.hired_projects.items():
        print("Project ID:", project_id)
        print("Client ID:", details["client_id"])
        print("Freelancer ID:", details["freelancer_id"])
        print("-" * 30)

def view_reviews():
    if not database.reviews:
        print("No Reviews Found")
        return

    print("\n--- Reviews ---")

    for project_id, review in database.reviews.items():
        print("Project ID:", project_id)
        print("Freelancer ID:", review["freelancer_id"])
        print("Rating:", review["rating"])
        print("Review:", review["review"])
        print("-" * 30)
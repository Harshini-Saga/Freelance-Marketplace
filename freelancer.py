import database
import file_handler
def view_projects():
    if not database.projects:
        print("No Projects Available")
        return

    for project_id, project in database.projects.items():
        if project["status"] == "Open":
            print("\nProject ID:", project_id)
            print("Title:", project["title"])
            print("Description:", project["description"])
            print("Budget:", project["budget"])
            print("Status:", project["status"])


def apply_bid(freelancer_id):
    project_id = int(input("Enter Project ID: "))
    bid_amount = float(input("Enter Bid Amount: "))

    if project_id not in database.projects:
        print("Invalid Project ID")
        return

    if database.projects[project_id]["status"] != "Open":
        print("Project is not open for bidding")
        return

    if project_id in database.bids:
        for bid in database.bids[project_id]:
            if bid["freelancer_id"] == freelancer_id:
                print("You have already applied for this project")
                return

    bid = {
        "freelancer_id": freelancer_id,
        "bid_amount": bid_amount
    }

    if project_id not in database.bids:
        database.bids[project_id] = []

    database.bids[project_id].append(bid)

    file_handler.save_data()

    print("Bid Submitted Successfully")


def my_bids(freelancer_id):
    found = False

    for project_id, bid_list in database.bids.items():
        for bid in bid_list:
            if bid["freelancer_id"] == freelancer_id:
                found = True
                print("\nProject ID:", project_id)
                print("Bid Amount:", bid["bid_amount"])

    if not found:
        print("No Bids Found")


def update_status(freelancer_id):
    project_id = int(input("Enter Project ID: "))
    status = input("Enter Status (In Progress/Completed): ")

    if status not in ["In Progress", "Completed"]:
        print("Invalid Status")
        return

    if project_id in database.hired_projects:
        if database.hired_projects[project_id]["freelancer_id"] == freelancer_id:
            database.projects[project_id]["status"] = status
            file_handler.save_data()
            print("Project Status Updated")
        else:
            print("You are not assigned to this project")
    else:
        print("Project not assigned")
def view_assigned_projects(freelancer_id):
    found = False

    for project_id, details in database.hired_projects.items():
        if details["freelancer_id"] == freelancer_id:
            found = True

            project = database.projects[project_id]

            print("\nProject ID:", project_id)
            print("Title:", project["title"])
            print("Description:", project["description"])
            print("Budget:", project["budget"])
            print("Status:", project["status"])

            if project_id in database.bids:
                for bid in database.bids[project_id]:
                    if bid["freelancer_id"] == freelancer_id:
                        print("Your Bid Amount:", bid["bid_amount"])

    if not found:
        print("No Assigned Projects")
def view_reviews(freelancer_id):
    found = False

    for project_id, review in database.reviews.items():
        if review["freelancer_id"] == freelancer_id:
            found = True

            print("\nProject ID:", project_id)
            print("Rating:", review["rating"])
            print("Review:", review["review"])

    if not found:
        print("No Reviews Found")
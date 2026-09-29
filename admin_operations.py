from db import cursor

def view_clients():

    cursor.execute("SELECT * FROM clients")

    clients = cursor.fetchall()

    for client in clients:

        print("\n------------------------")
        print("Client ID :", client["client_id"])
        print("Name      :", client["name"])
        print("Email     :", client["email"])
        print("------------------------")
def view_freelancers():

    cursor.execute("SELECT * FROM freelancers")

    freelancers = cursor.fetchall()

    if freelancers:

        for freelancer in freelancers:

            print("\n------------------------")
            print("Freelancer ID :", freelancer["freelancer_id"])
            print("Name          :", freelancer["name"])
            print("Email         :", freelancer["email"])
            print("Skill         :", freelancer["skill"])
            print("------------------------")

    else:
        print("No Freelancers Found")

def view_projects():

    cursor.execute("SELECT * FROM projects")

    projects = cursor.fetchall()

    if projects:

        for project in projects:

            print("\n------------------------")
            print("Project ID  :", project["project_id"])
            print("Client ID   :", project["client_id"])
            print("Title       :", project["title"])
            print("Description :", project["description"])
            print("Budget      :", project["budget"])
            print("Status      :", project["status"])
            print("Work Status :", project["work_status"])
            print("------------------------")

    else:
        print("No Projects Found")
def view_bids():

    cursor.execute("SELECT * FROM bids")

    bids = cursor.fetchall()

    if bids:

        for bid in bids:

            print("\n------------------------")
            print("Bid ID        :", bid["bid_id"])
            print("Project ID    :", bid["project_id"])
            print("Freelancer ID :", bid["freelancer_id"])
            print("Bid Amount    :", bid["bid_amount"])
            print("------------------------")

    else:
        print("No Bids Found")
def view_hired_projects():

    query = """
    SELECT *
    FROM hired_projects
    """

    cursor.execute(query)

    projects = cursor.fetchall()

    if projects:

        for project in projects:

            print("\n------------------------")
            print("Hire ID       :", project["hire_id"])
            print("Project ID    :", project["project_id"])
            print("Freelancer ID :", project["freelancer_id"])
            print("Hired Date    :", project["hired_date"])
            print("------------------------")

    else:
        print("No Hired Projects Found")
def view_reviews():

    cursor.execute("SELECT * FROM reviews")

    reviews = cursor.fetchall()

    if reviews:

        for review in reviews:

            print("\n------------------------")
            print("Review ID     :", review["review_id"])
            print("Freelancer ID :", review["freelancer_id"])
            print("Client ID     :", review["client_id"])
            print("Rating        :", review["rating"])
            print("Review        :", review["review_text"])
            print("------------------------")

    else:
        print("No Reviews Found")
def admin_login():

    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    query = """
    SELECT * FROM admin
    WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))

    admin = cursor.fetchone()

    if admin:
        print("Admin Login Successful")
        return True

    print("Invalid Admin Credentials")
    return False

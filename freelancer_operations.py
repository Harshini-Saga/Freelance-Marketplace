from db import cursor, conn

def register_freelancer():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    skill = input("Enter Skill: ")

    query = """
    INSERT INTO freelancers(name, email, password, skill)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, password, skill))
    conn.commit()

    print("Freelancer Registered Successfully")


def freelancer_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = """
    SELECT * FROM freelancers
    WHERE email = %s AND password = %s
    """

    cursor.execute(query, (email, password))

    freelancer = cursor.fetchone()

    if freelancer:
        print(f"Welcome {freelancer['name']}")
        return freelancer
    else:
        print("Invalid Email or Password")
        return None
from db import cursor

def view_projects():

    query = "SELECT * FROM projects"

    cursor.execute(query)

    projects = cursor.fetchall()

    if projects:

        for project in projects:

            print("\n------------------------")
            print("Project ID :", project["project_id"])
            print("Title      :", project["title"])
            print("Description:", project["description"])
            print("Budget     :", project["budget"])
            print("Status     :", project["status"])
            print("Work Status:", project["work_status"])
            print("------------------------")

    else:
        print("No Projects Available")
def my_bids(freelancer_id):

    query = """
    SELECT *
    FROM bids
    WHERE freelancer_id = %s
    """

    cursor.execute(query, (freelancer_id,))
    bids = cursor.fetchall()

    if bids:

        for bid in bids:

            print("\n------------------------")
            print("Bid ID     :", bid["bid_id"])
            print("Project ID :", bid["project_id"])
            print("Amount     :", bid["bid_amount"])
            print("------------------------")

    else:
        print("No Bids Found")
def view_assigned_projects(freelancer_id):

    query = """
    SELECT hp.hire_id,
           p.project_id,
           p.title,
           p.description,
           p.budget,
           hp.hired_date
    FROM hired_projects hp
    JOIN projects p
    ON hp.project_id = p.project_id
    WHERE hp.freelancer_id = %s
    """

    cursor.execute(query, (freelancer_id,))
    projects = cursor.fetchall()

    if projects:

        for project in projects:

            print("\n------------------------")
            print("Hire ID     :", project["hire_id"])
            print("Project ID  :", project["project_id"])
            print("Title       :", project["title"])
            print("Description :", project["description"])
            print("Budget      :", project["budget"])
            print("Hired Date  :", project["hired_date"])
            print("------------------------")

    else:
        print("No Assigned Projects")
def update_status(freelancer_id):

    project_id = int(input("Enter Project ID: "))

    check_query = """
    SELECT *
    FROM hired_projects
    WHERE project_id = %s
    AND freelancer_id = %s
    """

    cursor.execute(check_query, (project_id, freelancer_id))

    assigned_project = cursor.fetchone()

    if not assigned_project:
        print("You can update status only for assigned projects.")
        return

    print("\n1. In Progress")
    print("2. Completed")

    choice = input("Enter Choice: ")

    if choice == "1":
        status = "In Progress"

    elif choice == "2":
        status = "Completed"

    else:
        print("Invalid Choice")
        return

    update_query = """
    UPDATE projects
    SET work_status = %s
    WHERE project_id = %s
    """

    cursor.execute(update_query, (status, project_id))
    conn.commit()

    print("Status Updated Successfully")
def view_reviews(freelancer_id):

    query = """
    SELECT rating, review_text
    FROM reviews
    WHERE freelancer_id = %s
    """

    cursor.execute(query, (freelancer_id,))
    reviews = cursor.fetchall()

    if reviews:

        for review in reviews:

            print("\n------------------------")
            print("Rating :", review["rating"])
            print("Review :", review["review_text"])
            print("------------------------")

    else:
        print("No Reviews Found")
from db import cursor, conn

def place_bid(freelancer_id):

    project_id = int(input("Enter Project ID: "))

    # Check project exists
    cursor.execute(
        "SELECT * FROM projects WHERE project_id = %s",
        (project_id,)
    )

    project = cursor.fetchone()

    if not project:
        print("Invalid Project ID")
        return

    bid_amount = float(input("Enter Bid Amount: "))

    query = """
    INSERT INTO bids(project_id, freelancer_id, bid_amount)
    VALUES(%s, %s, %s)
    """

    cursor.execute(
        query,
        (project_id, freelancer_id, bid_amount)
    )

    conn.commit()

    print("Bid Placed Successfully")
from db import cursor, conn

def register_client():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = """
    INSERT INTO clients(name, email, password)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, password))
    conn.commit()

    print("Client Registered Successfully")


def client_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = """
    SELECT * FROM clients
    WHERE email = %s AND password = %s
    """

    cursor.execute(query, (email, password))

    client = cursor.fetchone()

    if client:
        print(f"Welcome {client['name']}")
        return client
    else:
        print("Invalid Email or Password")
        return None
from db import cursor, conn

def post_project(client_id):
    title = input("Enter Project Title: ")
    description = input("Enter Project Description: ")
    budget = float(input("Enter Budget: "))

    query = """
    INSERT INTO projects(client_id, title, description, budget)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (client_id, title, description, budget)
    )

    conn.commit()

    print("Project Posted Successfully")
def view_my_projects(client_id):

    query = """
    SELECT * FROM projects
    WHERE client_id = %s
    """

    cursor.execute(query, (client_id,))
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
        print("No Projects Found")
def view_bids(client_id):

    project_id = int(input("Enter Project ID: "))

    query = """
    SELECT *
    FROM bids
    WHERE project_id = %s
    """

    cursor.execute(query, (project_id,))
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
from datetime import date

def hire_freelancer(client_id):

    project_id = int(input("Enter Project ID: "))
    freelancer_id = int(input("Enter Freelancer ID: "))

    query = """
    INSERT INTO hired_projects
    (project_id, freelancer_id, hired_date)
    VALUES(%s, %s, %s)
    """

    cursor.execute(
        query,
        (project_id, freelancer_id, date.today())
    )

    update_query = """
    UPDATE projects
    SET status = 'Assigned'
    WHERE project_id = %s
    """

    cursor.execute(update_query, (project_id,))

    conn.commit()

    print("Freelancer Hired Successfully")
def check_project_status(client_id):

    query = """
    SELECT project_id,
           title,
           status,
           work_status
    FROM projects
    WHERE client_id = %s
    """

    cursor.execute(query, (client_id,))
    projects = cursor.fetchall()

    if projects:

        for project in projects:

            print("\n------------------------")
            print("Project ID  :", project["project_id"])
            print("Title       :", project["title"])
            print("Status      :", project["status"])
            print("Work Status :", project["work_status"])
            print("------------------------")

    else:
        print("No Projects Found")
def give_review(client_id):

    project_id = int(input("Enter Project ID: "))

    query = """
    SELECT hp.freelancer_id
    FROM hired_projects hp
    JOIN projects p
    ON hp.project_id = p.project_id
    WHERE p.project_id = %s
    AND p.client_id = %s
    AND p.work_status = 'Completed'
    """

    cursor.execute(query, (project_id, client_id))

    result = cursor.fetchone()

    if not result:
        print("Review can be given only after project completion.")
        return

    freelancer_id = result["freelancer_id"]

    check_query = """
    SELECT *
    FROM reviews
    WHERE client_id = %s
    AND freelancer_id = %s
    """

    cursor.execute(
        check_query,
        (client_id, freelancer_id)
    )

    existing_review = cursor.fetchone()

    if existing_review:
        print("You have already reviewed this freelancer.")
        return

    rating = float(input("Enter Rating (1-5): "))
    review_text = input("Enter Review: ")

    insert_query = """
    INSERT INTO reviews
    (freelancer_id, client_id, rating, review_text)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(
        insert_query,
        (freelancer_id, client_id, rating, review_text)
    )

    conn.commit()

    print("Review Added Successfully")
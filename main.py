from client_operations import (
    register_client,
    client_login,
    post_project,
    view_my_projects,
    view_bids,
    hire_freelancer,
    check_project_status,
    give_review
)

from freelancer_operations import (
    register_freelancer,
    freelancer_login,
    view_projects,
    place_bid,
    my_bids,
    view_assigned_projects,
    update_status,
    view_reviews
)

from admin_operations import (
    admin_login,
    view_clients,
    view_freelancers,
    view_projects as admin_view_projects,
    view_bids as admin_view_bids,
    view_hired_projects,
    view_reviews as admin_view_reviews
)
while True:

    print("\n===== FREELANCE MARKETPLACE =====")
    print("1. Client")
    print("2. Freelancer")
    print("3. Admin")
    print("4. Exit")

    choice = input("Enter Choice: ")

    # CLIENT
    if choice == "1":

        while True:

            print("\n--- Client Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            c = input("Enter Choice: ")

            if c == "1":
                register_client()

            elif c == "2":

                client = client_login()

                if client:

                    while True:

                        print("\n--- Client Dashboard ---")
                        print("1. Post Project")
                        print("2. View My Projects")
                        print("3. View Bids")
                        print("4. Hire Freelancer")
                        print("5. Check Project Status")
                        print("6. Give Review")
                        print("7. Logout")

                        op = input("Enter Choice: ")

                        if op == "1":
                            post_project(client["client_id"])

                        elif op == "2":
                            view_my_projects(client["client_id"])

                        elif op == "3":
                            view_bids(client["client_id"])

                        elif op == "4":
                            hire_freelancer(client["client_id"])

                        elif op == "5":
                            check_project_status(client["client_id"])

                        elif op == "6":
                            give_review(client["client_id"])

                        elif op == "7":
                            break

                        else:
                            print("Invalid Choice")

            elif c == "3":
                break

            else:
                print("Invalid Choice")

    # FREELANCER
    elif choice == "2":

        while True:

            print("\n--- Freelancer Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            f = input("Enter Choice: ")

            if f == "1":
                register_freelancer()

            elif f == "2":

                freelancer = freelancer_login()

                if freelancer:

                    while True:

                        print("\n--- Freelancer Dashboard ---")
                        print("1. View Projects")
                        print("2. Place Bid")
                        print("3. My Bids")
                        print("4. View Assigned Projects")
                        print("5. Update Status")
                        print("6. View Reviews")
                        print("7. Logout")

                        op = input("Enter Choice: ")

                        if op == "1":
                            view_projects()

                        elif op == "2":
                            place_bid(freelancer["freelancer_id"])

                        elif op == "3":
                            my_bids(freelancer["freelancer_id"])

                        elif op == "4":
                            view_assigned_projects(
                                freelancer["freelancer_id"]
                            )

                        elif op == "5":
                            update_status(
                                freelancer["freelancer_id"]
                            )

                        elif op == "6":
                            view_reviews(
                                freelancer["freelancer_id"]
                            )

                        elif op == "7":
                            break

                        else:
                            print("Invalid Choice")

            elif f == "3":
                break

            else:
                print("Invalid Choice")

    # ADMIN
    elif choice == "3":

        if admin_login():

            while True:
            # admin dashboard

                print("\n--- Admin Dashboard ---")
                print("1. View Clients")
                print("2. View Freelancers")
                print("3. View Projects")
                print("4. View Bids")
                print("5. View Hired Projects")
                print("6. View Reviews")
                print("7. Back")

                a = input("Enter Choice: ")

                if a == "1":
                    view_clients()

                elif a == "2":
                    view_freelancers()

                elif a == "3":
                    admin_view_projects()

                elif a == "4":
                    admin_view_bids()

                elif a == "5":
                    view_hired_projects()

                elif a == "6":
                    admin_view_reviews()

                elif a == "7":
                    break

                else:
                    print("Invalid Choice")

        else:
            print("Invalid Admin Credentials")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
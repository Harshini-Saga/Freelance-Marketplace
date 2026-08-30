import auth
import clients
import freelancer
import admin
import file_handler
file_handler.load_data()
while True:
    print("\n===== FREELANCE MARKETPLACE =====")
    print("1. Client")
    print("2. Freelancer")
    print("3. Admin")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        while True:
            print("\n--- Client Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            c = input("Enter Choice: ")

            if c == "1":
                auth.client_register()

            elif c == "2":
                client_id = auth.client_login()

                if client_id is not None:
                    while True:
                        print("\n--- Client Dashboard ---")
                        print("1. Post Project")
                        print("2. View My Projects")
                        print("3. View Bids")
                        print("4. Hire Freelancer")
                        print("5. View Project Status")
                        print("6. Logout")

                        op = input("Enter Choice: ")

                        if op == "1":
                            clients.post_project(client_id)

                        elif op == "2":
                            clients.view_my_projects(client_id)

                        elif op == "3":
                            clients.view_bids(client_id)

                        elif op == "4":
                            clients.hire_freelancer(client_id)

                        elif op == "5":
                            clients.check_project_status(client_id)

                        elif op == "6":
                            break

            elif c == "3":
                break

    elif choice == "2":
        while True:
            print("\n--- Freelancer Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            f = input("Enter Choice: ")

            if f == "1":
                auth.freelancer_register()

            elif f == "2":
                freelancer_id = auth.freelancer_login()

                if freelancer_id is not None:
                    while True:
                        print("\n--- Freelancer Dashboard ---")
                        print("1. View Projects")
                        print("2. Apply Bid")
                        print("3. My Bids")
                        print("4. View Assigned Projects")
                        print("5. Update Status")
                        print("6. View Reviews")
                        print("7. Logout")

                        op = input("Enter Choice: ")

                        if op == "1":
                            freelancer.view_projects()

                        elif op == "2":
                            freelancer.apply_bid(freelancer_id)

                        elif op == "3":
                            freelancer.my_bids(freelancer_id)

                        elif op == "4":
                            freelancer.view_assigned_projects(freelancer_id)

                        elif op == "5":
                            freelancer.update_status(freelancer_id)

                        elif op == "6":
                            freelancer.view_reviews(freelancer_id)

                        elif op == "7":
                            break

            elif f == "3":
                break

    elif choice == "3":

        if auth.admin_login():

            while True:
                print("\n--- Admin Menu ---")
                print("1. View Clients")
                print("2. View Freelancers")
                print("3. View Projects")
                print("4. View Bids")
                print("5. View Hired Projects")
                print("6. View Reviews")
                print("7. Back")

                a = input("Enter Choice: ")

                if a == "1":
                    admin.view_clients()

                elif a == "2":
                    admin.view_freelancers()

                elif a == "3":
                    admin.view_projects()

                elif a == "4":
                    admin.view_bids()

                elif a == "5":
                    admin.view_hired_projects()

                elif a == "6":
                    admin.view_reviews()

                elif a == "7":
                    break

    elif choice == "4":
        file_handler.save_data()
        print("Thank You")
        break

    else:
        print("Invalid Choice")
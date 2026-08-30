import pickle
import database

def save_data():
    data = {
        "clients": database.clients,
        "freelancers": database.freelancers,
        "projects": database.projects,
        "bids": database.bids,
        "hired_projects": database.hired_projects,
        "reviews": database.reviews,
        "client_id": database.client_id,
        "freelancer_id": database.freelancer_id,
        "project_id": database.project_id
    }

    with open("marketplace.dat", "wb") as file:
        pickle.dump(data, file)


def load_data():
    try:
        with open("marketplace.dat", "rb") as file:
            data = pickle.load(file)

            database.clients = data["clients"]
            database.freelancers = data["freelancers"]
            database.projects = data["projects"]
            database.bids = data["bids"]
            database.hired_projects = data["hired_projects"]
            database.reviews = data["reviews"]

            database.client_id = data["client_id"]
            database.freelancer_id = data["freelancer_id"]
            database.project_id = data["project_id"]

    except FileNotFoundError:
        pass
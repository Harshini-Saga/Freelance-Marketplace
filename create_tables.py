from db import cursor, conn

# Clients Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
""")

# Freelancers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS freelancers(
    freelancer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    skill VARCHAR(100)
)
""")

# Projects Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects(
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    title VARCHAR(100),
    description TEXT,
    budget DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'Open',
    FOREIGN KEY(client_id) REFERENCES clients(client_id)
)
""")
from db import cursor, conn

# Bids Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bids(
    bid_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT,
    freelancer_id INT,
    bid_amount DECIMAL(10,2),
    FOREIGN KEY(project_id) REFERENCES projects(project_id),
    FOREIGN KEY(freelancer_id) REFERENCES freelancers(freelancer_id)
)
""")

# Hired Projects Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS hired_projects(
    hire_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT,
    freelancer_id INT,
    hired_date DATE,
    FOREIGN KEY(project_id) REFERENCES projects(project_id),
    FOREIGN KEY(freelancer_id) REFERENCES freelancers(freelancer_id)
)
""")

# Reviews Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews(
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    freelancer_id INT,
    client_id INT,
    rating INT,
    review_text TEXT,
    FOREIGN KEY(freelancer_id) REFERENCES freelancers(freelancer_id),
    FOREIGN KEY(client_id) REFERENCES clients(client_id)
)
""")

conn.commit()
print("Remaining Tables Created Successfully")
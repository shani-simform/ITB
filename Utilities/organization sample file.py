import random
import pandas as pd
from openpyxl import Workbook

# Define roles
roles = [
    "CMS Browser", "CMS Data Entry", "CMS Manager", "CMS Owner", "Dashboard User",
    "District Settings Admin", "Fidelity Checker", "LMS Manager", "LMS Publisher",
    "Local System Admin", "Resource Browser", "Resource Publisher", "Workshops User"
]

# Sample data
titles = ["Principal", "Vice Principal", "Teacher", "Administrator"]

# first_names = [
#     "Evan", "Julian", "Christian", "Oliver", "Jason", "Isaac", "Sam", "Keith",
#     "Leonard", "Isaac", "David", "Brian", "Jake", "Alexander", "Adrian", "Matt",
#     "Joshua", "Edward", "Piers", "Tim"
# ]
#
# last_names = [
#     "Nash", "Mackenzie", "Hemmings", "Baker", "Rampling", "Berry", "Peake",
#     "Manning", "Sutherland", "Murray", "Duncan", "Terry", "Morgan", "Mackay",
#     "Stewart", "Turner", "Vaughan", "McGrath", "Gill", "Cameron"
# ]

first_names = [
    "Jack", "Joe", "Austin", "Evan", "Sam", "Steven", "Nicholas", "Warren",
    "Dominic", "Leonard", "Gordon", "Phil", "Thomas", "Keith", "Brian", "Gordon",
    "Sean", "Edward", "Charles", "Brandon", "Jacob", "Charles", "Colin", "Max",
    "Simon", "Blake", "Anthony", "Connor", "Nicholas", "Stephen", "Frank", "Eric",
    "Piers", "Richard", "Brian", "Gordon", "Alan", "Christian", "Andrew", "Harry",
    "Eric", "Jacob", "Carl", "Colin", "David", "Carl", "Piers", "Keith", "Victor", "Colin"
]

last_names = [
    "Blake", "Thomson", "Glover", "Glover", "Wallace", "Bower", "Lee", "Harris",
    "Campbell", "Fisher", "James", "Lambert", "Rees", "Davidson", "McLean", "Walsh",
    "Gray", "Fraser", "Baker", "Skinner", "Cameron", "Short", "Butler", "King",
    "Alsop", "Reid", "Parsons", "Short", "Mitchell", "Welch", "Hart", "Walker",
    "Simpson", "Ball", "Black", "Welch", "Russell", "Hill", "Jackson", "Abraham",
    "Rutherford", "Chapman", "Langdon", "Gibson", "Russell", "Alsop", "Ogden", "Hughes",
    "Ferguson", "Dickens"
]

def generate_organizations(num_records):
    return [[f"School {i}", f"{i} Main St", "Cleveland", 1000+i, "New York", f"Contact {i}", "Director", "123-456-7890", f"contact{i}@example.com"] for i in range(1, num_records+1)]

# def generate_organizations(num_records):
#     return [[f"School {i}", f"{i} Main St", "Cleveland", 1000+i, "NY", f"Contact {i}", "Director", "123-456-7890", f"contact{i}@example.com"] for i in range(1, num_records+1)]


def generate_titles():
    return [[title] for title in titles]

def generate_users(num_records, orgs):
    users = []
    used_emails = set()
    while len(users) < num_records:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}{len(used_emails)+100}@example.com"
        if email not in used_emails:
            used_emails.add(email)
            org = random.choice(orgs)[0]
            title = random.choice(titles)
            assigned_roles = random.sample(roles, random.randint(2, 4))
            users.append([first_name, last_name, email, org, title, ", ".join(assigned_roles)])
    return users

# User input for record counts
num_records_org = 10 # Adjust this number as needed
num_records_users = 100  # Adjust this number as needed
num_records_parent_org = 1 # Adjust this number as needed


# Generate data
sheet1_data = generate_organizations(num_records_parent_org)
sheet2_data = generate_organizations(num_records_org)
sheet3_data = generate_titles()
sheet4_data = generate_users(num_records_users, sheet2_data)

# Create DataFrames
df1 = pd.DataFrame(sheet1_data, columns=["Location Name", "Address", "City", "Zip", "State", "Main Contact", "Title", "Phone", "Email"])
df2 = pd.DataFrame(sheet2_data, columns=["Location Name", "Address", "City", "Zip", "State", "Main Contact", "Title", "Phone", "Email"])
df3 = pd.DataFrame(sheet3_data, columns=["Titles"])
df4 = pd.DataFrame(sheet4_data, columns=["First Name", "Last Name", "Email", "Org", "Title", "Roles"])

# Save to Excel
with pd.ExcelWriter("organization_setup_50k.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Parent Org Setup", index=False)
    df2.to_excel(writer, sheet_name="Child Org Setup", index=False)
    df3.to_excel(writer, sheet_name="Titles", index=False)
    df4.to_excel(writer, sheet_name="Users", index=False)

print("Excel file 'organization_setup1.xlsx' created successfully.")
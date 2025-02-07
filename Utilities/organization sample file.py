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
last_names = ["John", "Jane", "Robert", "Emily", "Michael", "Sarah", "David", "Laura"]
first_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Davis", "Miller", "Wilson"]

def generate_organizations(num_records):
    return [[f"School {i}", f"{i} Main St", "Cleveland", 1000+i, "NY", f"Contact {i}", "Director", "123-456-7890", f"contact{i}@example.com"] for i in range(1, num_records+1)]

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
        email = f"{first_name.lower()}.{last_name.lower()}{len(used_emails)}@example.com"
        if email not in used_emails:
            used_emails.add(email)
            org = random.choice(orgs)[0]
            title = random.choice(titles)
            assigned_roles = random.sample(roles, random.randint(2, 4))
            users.append([first_name, last_name, email, org, title, ", ".join(assigned_roles)])
    return users

# User input for record counts
num_records_org = 500 # Adjust this number as needed
num_records_users = 500  # Adjust this number as needed
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
with pd.ExcelWriter("organization_setup1.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Parent Org Setup", index=False)
    df2.to_excel(writer, sheet_name="Child Org Setup", index=False)
    df3.to_excel(writer, sheet_name="Titles", index=False)
    df4.to_excel(writer, sheet_name="Users", index=False)

print("Excel file 'organization_setup1.xlsx' created successfully.")
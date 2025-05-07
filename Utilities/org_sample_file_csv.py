import csv
import random

num_records_parent = 50
num_records_child = 100
data_parent = []
data_child = []

unique_ids_parent = set()
unique_ids_child = set()
unique_emails = set()

for i in range(num_records_parent):
    sourced_id = str(i)
    while sourced_id in unique_ids_parent:
        sourced_id = str(random.randint(1000, 9999))
    unique_ids_parent.add(sourced_id)

    data_parent.append({
        "sourcedId": sourced_id,
        "name": f"Blinkit {i}",
        "type": "school" if i != 0 else "district",
        "identifier": str(random.randint(1000000, 9999999)),
        "metadata.address1": f"{random.randint(100, 999)} Random Street",
        "metadata.city": "Clifton",
        "metadata.postCode": "7011",
        "metadata.state": "New Jersey"
    })

fields_parent = ["sourcedId", "status", "dateLastModified", "name", "type", "identifier", "parentSourcedId",
                 "metadata.address1", "metadata.address2", "metadata.city", "metadata.postCode", "metadata.state"]

with open("SampleOneRosterOrgFile10.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields_parent)
    writer.writeheader()
    for row in data_parent:
        row.setdefault("status", "")
        row.setdefault("dateLastModified", "")
        row.setdefault("parentSourcedId", "")
        row.setdefault("metadata.address2", "")
        writer.writerow(row)

org_sourced_ids = [entry["sourcedId"] for entry in data_parent if entry["type"] == "school"]

for i in range(num_records_child):
    sourced_id = str(random.randint(10000, 99999))
    while sourced_id in unique_ids_child:
        sourced_id = str(random.randint(10000, 99999))
    unique_ids_child.add(sourced_id)

    email = f"user{i}@classlink.k12.nj.us"
    while email in unique_emails:
        email = f"user{random.randint(100, 999)}@classlink.k12.nj.us"
    unique_emails.add(email)

    data_child.append({
        "sourcedId": sourced_id,
        "enabledUser": "TRUE",
        "orgSourcedIds": random.choice(org_sourced_ids),
        "role": "teacher",
        "username": f"user{i}",
        "userIds": f"{{FED:{sourced_id}}}",
        "givenName": f"User{i}",
        "familyName": "Teacher",
        "middleName": "M",
        "identifier": str(random.randint(1000, 9999)),
        "email": email,
        "sms": "",
        "phone": "",
        "agentSourcedIds": "",
        "grades": str(random.randint(1, 12)),
        "password": ""
    })

fields_child = ["sourcedId", "status", "dateLastModified", "enabledUser", "orgSourcedIds", "role", "username",
                "userIds", "givenName", "familyName", "middleName", "identifier", "email", "sms", "phone",
                "agentSourcedIds", "grades", "password"]

with open("SampleOneRosterUsersFile10.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields_child)
    writer.writeheader()
    for row in data_child:
        row.setdefault("status", "")
        row.setdefault("dateLastModified", "")
        writer.writerow(row)

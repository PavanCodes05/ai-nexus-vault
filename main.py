import json

filename = "passwords.json"

def new_password():
    new_data = dict()

    id = int(input("Enter the id: "))
    service_name = input("Enter the service name (eg: gmail): ")
    username = input("Enter the username/id: ")
    password = input("Enter the password: ")

    new_data["id"] = id
    new_data["service_name"] = service_name
    new_data["username"] = username
    new_data["password"] = password

    # Read the passwords -> modify (by adding new data) -> rewrite on the same

    # Read
    with open(filename, 'r') as f:
        data = json.load(f)

    # Modify
    data["entries"].append(new_data)

    # Write the data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def find_password():
    service = input("enter the service: ")

    # Read
    with open(filename, 'r') as f:
        data = json.load(f)

    for entry in data["entries"]:
        if entry["service_name"] == service:
            print(entry["password"])


choice = int(input("pick a choice:\n 1. New password\n 2. Search for service\n ENTER YOUR CHOICE: "))

if choice == 1:
    new_password()
elif choice == 2:
    find_password()
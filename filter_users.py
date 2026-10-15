import json


def load_users():
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(name):
    users = load_users()
    return [user for user in users if user.get("name", "").lower() == name.lower()]


def filter_users_by_email(email):
    """Return users whose email matches, ignoring letter case."""
    users = load_users()
    return [user for user in users if user.get("email", "").lower() == email.lower()]


def filter_users_by_age(age):
    """Return users with an exact age match."""
    users = load_users()
    return [user for user in users if user.get("age") == age]


def main():
    filter_option = input("What would you like to filter by? (name, email, age): ").strip().lower()

    if filter_option == "name":
        value = input("Enter a name: ").strip()
        results = filter_users_by_name(value)
    elif filter_option == "email":
        value = input("Enter an email: ").strip()
        results = filter_users_by_email(value)
    elif filter_option == "age":
        try:
            value = int(input("Enter an age: ").strip())
        except ValueError:
            print("Age must be a number.")
            return
        results = filter_users_by_age(value)
    else:
        print("Unsupported filter option. Choose name, email, or age.")
        return

    if results:
        for user in results:
            print(user)
    else:
        print("No matching users found.")


if __name__ == "__main__":
    main()

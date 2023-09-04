import os
import json

JSONS_PATH = "/server/Resources/jsons/"
USERS_PATH = "users.json"
ROLES_PATH = "roles.json"


def load_users_from_json():
    """
    Load user data from a JSON file into a dictionary.
    Returns:
        dict: A dictionary where keys are usernames and values are user data dictionaries.
              For example: {'user1': {'username': 'user1', 'password': 'password1'}, ...}
    """
    users = {}  # Initialize an empty dictionary to store user data.

    json_file_path = os.getcwd() + JSONS_PATH + USERS_PATH

    if "endpoint_tests" in json_file_path:
        json_file_path = json_file_path.replace("endpoint_tests", "ServerSide")

    try:
        with open(json_file_path, 'r') as users_file:
            users_data = json.load(users_file)  # Load user data from the JSON file.

            for user_data in users_data:
                username = users_data[user_data].get('username')  # Get the username from user data.
                users[username] = users_data[user_data]  # Add the user data to the dictionary using the username as the key.

        return users  # Return the populated dictionary.

    except FileNotFoundError:
        # Handle the case where the JSON file does not exist.
        print(f"ERROR: JSON file not found at path: {json_file_path}")
        return {}  # Return an empty dictionary in case of an error.


def load_roles_from_json():
    """
    Load role data from a JSON file into a dictionary.
    Returns:
        dict: A dictionary where keys are role names and values are role data dictionaries.
              For example: {'role1': {'name': 'role1', 'description': 'Description1'}, ...}
    """
    roles = {}  # Initialize an empty dictionary to store role data.

    json_file_path = os.getcwd() + JSONS_PATH + ROLES_PATH
    if "endpoint_tests" in json_file_path:
        json_file_path = json_file_path.replace("endpoint_tests", "ServerSide")
    try:
        with open(json_file_path, 'r') as roles_file:
            roles_data = json.load(roles_file)  # Load role data from the JSON file.

            for role_data in roles_data:
                role_name = role_data.get('name')  # Get the role name from role data.
                roles[role_name] = role_data  # Add the role data to the dictionary using the role name as the key.

        return roles  # Return the populated dictionary.

    except FileNotFoundError:
        # Handle the case where the JSON file does not exist.
        print(f"ERROR: JSON file not found at path: {json_file_path}")
        return {}  # Return an empty dictionary in case of an error.


def save_users_to_json(users):
    """
    Save user data to a JSON file.

    Args:
        users (dict): A dictionary containing user data to be saved to the JSON file.
                      Keys should be usernames, and values should be user data dictionaries.

    Returns:
        bool: True if the data was successfully saved, False otherwise.
    """
    path = os.getcwd() + JSONS_PATH + USERS_PATH
    if "endpoint_tests" in path:
        path = path.replace("endpoint_tests", "ServerSide")
    try:
        with open(path, 'w') as users_file:
            # Convert the users dictionary to a JSON string and write it to the file.
            json.dump(users, users_file, indent=4)
        return True  # Return True if the data was successfully saved.
    except Exception as e:
        # Handle any exceptions that may occur during file writing.
        print(f"ERROR: Unable to save data to JSON file. {str(e)}")
        return False  # Return False if an error occurs.
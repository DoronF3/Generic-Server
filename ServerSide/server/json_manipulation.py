import os
import json

JSONS_PATH = "/server/Resources/jsons/"

def load_users_from_json(json_file_path):
    """
    Load user data from a JSON file into a dictionary.

    Args:
        json_file_path (str): The path to the JSON file containing user data.

    Returns:
        dict: A dictionary where keys are usernames and values are user data dictionaries.
              For example: {'user1': {'username': 'user1', 'password': 'password1'}, ...}
    """
    users = {}  # Initialize an empty dictionary to store user data.

    json_file_path = os.getcwd() + JSONS_PATH + json_file_path

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


def load_roles_from_json(json_file_path):
    """
    Load role data from a JSON file into a dictionary.

    Args:
        json_file_path (str): The path to the JSON file containing role data.

    Returns:
        dict: A dictionary where keys are role names and values are role data dictionaries.
              For example: {'role1': {'name': 'role1', 'description': 'Description1'}, ...}
    """
    roles = {}  # Initialize an empty dictionary to store role data.

    json_file_path = os.getcwd() + JSONS_PATH + json_file_path
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
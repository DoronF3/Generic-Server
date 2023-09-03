import os
import json

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from logging import FileHandler, WARNING

from server import create_app
from server.routes import initialize_routes, initiate_resources, create_dict

# Other imports here


# Define paths
PATH_TO_CONFIG = "/server_config.json"


def config(path):
    """
    Reads a configuration file and extracts server information.

    This function takes a file path to a JSON configuration file and extracts relevant
    server information from it. The server information includes the host, port, and
    other settings. The function returns a list containing the extracted server info.

    :param path: A string representing the path to the configuration file.
    :return: A list containing server information including host, port, and endpoints.
             Returns None if the configuration file does not exist.
    """
    returned_list = []  # The list to hold extracted server information.

    # Check if the file exists.
    if not os.path.exists(os.getcwd() + path):
        return None

    # Open the configuration file to read its contents.
    with open(os.getcwd() + path, "r") as f:
        config_file = json.load(f)

    # Extract server information from the configuration dictionary.
    info_dict = config_file["server"]  # Dictionary containing server info.

    # Iterate over the server information dictionary and add each value to the list.
    for info in info_dict:
        returned_list.append(info_dict[info])

    # Add the endpoints dictionary to the list.
    returned_list.append(config_file["endpoints"])

    return returned_list


def init():
    """

    """

    # Initialize and run the server
    app = Flask(__name__)  # sets the main run target
    api = Api(app)  # flask way of setting the API
    file_handler = FileHandler('errorlog.txt')  # creates a runtime error log file
    file_handler.setLevel(WARNING)

    returned_list = config(PATH_TO_CONFIG)
    host = returned_list[0]  # Host IP.
    port = returned_list[1]  # Port number.
    authorization = returned_list[2]  # Authorization token.
    resource_dict = create_dict(returned_list[3])  # The endpoint list.

    app = create_app()

    initiate_resources(app, resource_dict)

    CORS(app)

    initialize_routes(api, resource_dict)

    app.run(host=host, port=port, debug=True)  # if true restart app if code is changed


if __name__ == "__main__":
    init()

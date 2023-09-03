from flask import Flask
from datetime import datetime, timedelta
from flask_session import Session

def create_app():
    """
    Creates and configures a Flask application instance.

    :return: The configured Flask app instance.
    """
    app = Flask(__name__)  # Create a Flask app instance
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the secret key

    # import additional structure files
    # from .auth import auth

    # Import additional blueprints or routes here
    # from .module import blueprint_name

    # Register blueprints (commented out in your code)
    # app.register_blueprint(blueprint_name, url_prefix='/path_prefix')

    return app  # Return the configured Flask app instance

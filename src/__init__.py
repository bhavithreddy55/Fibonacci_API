from flask import Flask

from src.utils.constants import UNEXPECTED_ERROR_MESSAGE
from src.utils.response import error_response


def create_app():
    app = Flask(__name__)

    from src.fib_app.routes import fibonacci_bp

    # Register the Blueprint
    app.register_blueprint(fibonacci_bp, url_prefix='/api')

    # Global error handler for ValueError
    @app.errorhandler(ValueError)
    def handle_value_error(error):
        """
        Handle ValueError and return a standardized error response.

        Args:
            error (ValueError): The error to handle.

        Returns:
            Response: A JSON response with the error message and status code.
        """
        return error_response(message=str(error), status_code=400)

    # Global error handler for unexpected errors
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """
        Handle unexpected errors and return a standardized error response.

        Args:
            error (Exception): The error to handle.

        Returns:
            Response: A JSON response with the error message and status code.
        """
        return error_response(message=UNEXPECTED_ERROR_MESSAGE, errors=str(error), status_code=500)

    return app

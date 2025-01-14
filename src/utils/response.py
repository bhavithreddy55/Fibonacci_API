from flask import jsonify

def success_response(data=None, message="Success", status_code=200):
    """
    Create a standardized success response.

    Args:
        data (any, optional): The data to include in the response. Defaults to None.
        message (str, optional): A success message. Defaults to "Success".
        status_code (int, optional): The HTTP status code. Defaults to 200.

    Returns:
        Response: A JSON response with the specified data, message, and status code.
    """
    response = {
        "status": "success",
        "message": message,
        "data": data
    }
    return jsonify(response), status_code


def error_response(message="An error occurred", status_code=400, errors=None):
    """
    Create a standardized error response.

    Args:
        message (str, optional): An error message. Defaults to "An error occurred".
        status_code (int, optional): The HTTP status code. Defaults to 400.
        errors (list, optional): A list of errors for additional details. Defaults to None.

    Returns:
        Response: A JSON response with the specified error message, status code, and optional errors.
    """
    response = {
        "status": "error",
        "message": message,
        "errors": errors if errors else []
    }
    return jsonify(response), status_code

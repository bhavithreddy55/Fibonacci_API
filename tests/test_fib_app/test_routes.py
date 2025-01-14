from src.utils.constants import FIBONACCI_SUCCESS_MESSAGE, MISSING_PARAMETER_MESSAGE, NON_NEGATIVE_MESSAGE

def test_valid_input(client):
    """
    Test valid input for the Fibonacci API.
    Asserts the response status code and JSON structure.
    """
    # Make a GET request with a valid input (n=10)
    response = client.get('/api/fibonacci?n=10')

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert the response JSON matches the expected structure
    assert response.json == {
        "status": "success",
        "message": FIBONACCI_SUCCESS_MESSAGE,
        "data": {
            "input": 10,
            "result": 55
        }
    }


def test_missing_parameter(client):
    """
    Test the Fibonacci API with a missing 'n' parameter.
    Asserts the response status code and error message.
    """
    # Make a GET request without the 'n' parameter
    response = client.get('/api/fibonacci')

    # Assert the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Assert the response JSON contains the correct error message
    assert response.json == {
        "status": "error",
        "message": MISSING_PARAMETER_MESSAGE,
        "errors": []
    }


def test_negative_input(client):
    """
    Test the Fibonacci API with a negative input.
    Asserts the response status code and error message.
    """
    # Make a GET request with a negative input (n=-5)
    response = client.get('/api/fibonacci?n=-5')

    # Assert the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Assert the response JSON contains the correct error message
    assert response.json == {
        "status": "error",
        "message": NON_NEGATIVE_MESSAGE,
        "errors": []
    }


def test_invalid_input(client):
    """
    Test the Fibonacci API with an invalid input (non-integer).
    Asserts the response status code and error message.
    """
    # Make a GET request with an invalid input (n=abc)
    response = client.get('/api/fibonacci?n=abc')

    # Assert the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Assert the response JSON contains the correct error message
    assert response.json == {
        "status": "error",
        "message": MISSING_PARAMETER_MESSAGE,
        "errors": []
    }

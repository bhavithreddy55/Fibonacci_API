import pytest

@pytest.fixture
def client():
    """
    Fixture to create a test client for the Flask app.
    Yields a test client for making requests.
    """
    # Import the Flask app factory function
    from src import create_app

    # Create the Flask app instance
    app = create_app()

    # Enable testing mode
    app.config['TESTING'] = True

    # Create and yield the test client
    with app.test_client() as client:
        yield client

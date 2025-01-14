import os
from flask.cli import load_dotenv
from src import create_app

# Load environment variables from a .env file (if it exists)
load_dotenv()

# Create the Flask application instance
app = create_app()

# Get the host and port from environment variables, or use defaults
HOST = os.getenv('HOST', '0.0.0.0')  # Default to '0.0.0.0' if HOST is not set
PORT = int(os.getenv('PORT', 5000))  # Default to 5000 if PORT is not set

# Run the Flask application
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
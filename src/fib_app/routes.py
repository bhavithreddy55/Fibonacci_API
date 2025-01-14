from flask import Blueprint

from src.fib_app.resource import FibonacciAPI

# Create a Blueprint for the Fibonacci API
fibonacci_bp = Blueprint('fibonacci', __name__)

# Register the FibonacciAPI view with the Blueprint
fibonacci_bp.add_url_rule('/fibonacci', view_func=FibonacciAPI.as_view('fibonacci'))

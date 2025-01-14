from flask.views import MethodView
from flask import request

from src.fib_app.validators import InputValidator
from src.utils.common import Fibonacci
from src.utils.constants import FIBONACCI_SUCCESS_MESSAGE
from src.utils.response import success_response


class FibonacciAPI(MethodView):
    """
    A class-based view to handle Fibonacci API requests.
    """

    def __init__(self):
        # Initialize the Fibonacci class
        self.fibonacci_calculator = Fibonacci()

    def get(self):
        """
        Handle GET requests to compute the nth Fibonacci number.

        Query Parameters:
            n (int): The position in the Fibonacci sequence.

        Returns:
            JSON: A standardized JSON response containing the input and the result.
        """
        try:
            # Get the 'n' parameter from the query string
            n = request.args.get('n', type=int)

            # Validate the input using the InputValidator class
            InputValidator.validate_input(n)

            # Compute the Fibonacci number using the Fibonacci class
            result = self.fibonacci_calculator.compute(n)

            # Return the result as a success response
            return success_response(data={"input": n, "result": result},
                                    message=FIBONACCI_SUCCESS_MESSAGE)

        except ValueError as e:
            # Handle ValueError (e.g., invalid input)
            raise e

        except Exception as e:
            # Handle unexpected errors
            raise e

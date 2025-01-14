from src.utils.constants import MISSING_PARAMETER_MESSAGE, NON_NEGATIVE_MESSAGE


class InputValidator:
    """
    A class to validate input for the Fibonacci API.
    """

    @staticmethod
    def validate_input(n):
        """
        Validate the input for the Fibonacci API.

        Args:
            n (int or None): The input value to validate.

        Raises:
            ValueError: If the input is invalid.
        """
        if n is None:
            raise ValueError(MISSING_PARAMETER_MESSAGE)

        if n < 0:
            raise ValueError(NON_NEGATIVE_MESSAGE)
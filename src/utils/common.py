class Fibonacci:
    """
    A class to compute Fibonacci numbers.
    """

    def compute(self, n):
        """
        Compute the nth Fibonacci number.

        Args:
            n (int): The position in the Fibonacci sequence.

        Returns:
            int: The nth Fibonacci number.

        Raises:
            ValueError: If n is negative.
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

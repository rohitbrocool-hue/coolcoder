"""
Sample Python module for coolcoder repository.
This module demonstrates basic Python coding practices and patterns.
"""


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.result = 0

    def add(self, a, b):
        """Add two numbers and return the result."""
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        """Subtract two numbers and return the result."""
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        self.result = a * b
        return self.result

    def divide(self, a, b):
        """Divide two numbers and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result

    def get_result(self):
        """Return the last calculated result."""
        return self.result


def greet(name):
    """Greet a person with a friendly message."""
    return f"Hello, {name}! Welcome to coolcoder."


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence


def main():
    """Main function to demonstrate the module functionality."""
    print("Welcome to coolcoder sample!")
    
    # Calculator example
    calc = Calculator()
    print(f"\n10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    
    # Greeting example
    print(f"\n{greet('Developer')}")
    
    # Fibonacci example
    print(f"\nFibonacci sequence (first 10 terms): {fibonacci(10)}")


if __name__ == "__main__":
    main()

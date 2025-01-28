import time

class AnalyticalEngine:
    def __init__(self):
        self.store = {}  # Memory to store intermediate results
        self.intermediate_states = False  # Toggle to display computation steps
        self.delay = 0.4  # Delay for intermediate states

    def set_intermediate_states(self, display):
        self.intermediate_states = display
        state = "enabled" if display else "disabled"
        print(f"Intermediate states are now {state}.")

    def mill(self, operation, *operands):
        if operation == "add":
            return sum(operands)
        elif operation == "subtract":
            return operands[0] - operands[1]
        elif operation == "multiply":
            result = 1
            for op in operands:
                result *= op
            return result
        elif operation == "divide":
            return operands[0] // operands[1]

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        if self.intermediate_states:
            print(f"Calculating factorial({n})")
            time.sleep(self.delay)  # Add delay between steps
        return self.mill("multiply", n, self.factorial(n - 1))

    def fibonacci(self, n):
        if n in self.store:
            return self.store[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if self.intermediate_states:
            print(f"Calculating Fibonacci({n})")
            time.sleep(self.delay)  # Add delay between steps
        result = self.mill("add", self.fibonacci(n - 1), self.fibonacci(n - 2))
        self.store[n] = result
        return result

    def simulate(self):
        print("Welcome to the Analytical Engine Simulator!")
        print("Choose a task:")
        print("1. Calculate Factorial")
        print("2. Calculate Fibonacci")
        print("3. Toggle Intermediate States")
        print("4. Exit")

        while True:
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                n = int(input("Enter a number to calculate factorial: "))
                print(f"Factorial of {n}: {self.factorial(n)}")
            elif choice == "2":
                n = int(input("Enter the position for Fibonacci sequence: "))
                print(f"Fibonacci({n}): {self.fibonacci(n)}")
            elif choice == "3":
                self.set_intermediate_states(not self.intermediate_states)
            elif choice == "4":
                print("Exiting the simulator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    engine = AnalyticalEngine()
    engine.simulate()

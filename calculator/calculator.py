class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Cannot divide by zero"


def main():
    calculator = SimpleCalculator()

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input.")
        return

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter choice (1-4): "))
    except ValueError:
        print("Error: Invalid choice.")
        return

    if choice not in [1, 2, 3, 4]:
        print("Error: Invalid choice.")

    else:
        result = 0
        if choice == 1:
            result = calculator.add(num1, num2)
        elif choice == 2:
            result = calculator.subtract(num1, num2)
        elif choice == 3:
            result = calculator.multiply(num1, num2)
        elif choice == 4:
            result = calculator.divide(num1, num2)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()

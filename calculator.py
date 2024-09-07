def get_number(prompt):
    
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():

    while True:
        operation = input("Enter an operation (+, -, *, /): ").strip()
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def calculate(num1, num2, operation):

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def main():

    while True:
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()

        result = calculate(num1, num2, operation)

        print("The result of {} {} {} is: {}".format(num1, operation, num2, result))

        continue_calculating = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculating != 'yes':
            print("ByeBye!")
            break

if __name__ == "__main__":
    main()

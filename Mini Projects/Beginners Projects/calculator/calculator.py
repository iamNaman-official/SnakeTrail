import os
import art
from datetime import datetime
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculator(a,b, opr):
    match opr:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero is not allowed."



def start_calculator():
    clear_screen()
    print(art.logo)
    isCalculate = True
    history = []

    a = float(input("Enter first number: "))
    while isCalculate:
        opr = input("Enter operator (+, -, *, /): ")
        while opr not in ["+", "-", "*", "/"]:
            try:
                print("Invalid operator. Please enter a valid operator (+, -, *, /).")
                print("Choose from the following operators: +, -, *, /")
                opr = input("Enter operator (+, -, *, /): ")
            except ValueError:
                print("Invalid input. Please enter a valid operator (+, -, *, /).")

        b = float(input("Enter another number: "))
        result = calculator(a, b, opr)

        print(f"The result of {a} {opr} {b} is: {result}")

        print("-" * 20)
        print("Saving the calculation to history...")
        history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Result == ({a} {opr} {b} = {result})")
        with open("history.txt", "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Result == ({a} {opr} {b} = {result})\n")
        print("-" * 20)        

        user_input = int(input(f"What you want to do with the current value {result}? \n 1.for Continue Calculation: \n 2.for Start New Calculation \n 3.for Stop Calculation:\n Enter your choice (1, 2, or 3): "))
        while user_input not in [1, 2, 3]:
            print("Invalid input. Please enter 1, 2 or 3.")
            user_input = int(input(f"What you want to do with the current value {result}? \n 1.for Continue Calculation: \n 2.for Start New Calculation \n 3.for Stop Calculation:\n Enter your choice (1, 2, or 3): "))
            
        if user_input == 1:
            a = result
            clear_screen()
            print("Current Value: ", a)
            print("-" * 20)
        elif user_input == 2:
            start_calculator()
            return
        else:
            isCalculate = False
            print("Thank you for using the calculator. Goodbye!")
    print("-" * 20)
    print("Do you want to see the history of calculations?")
    if input("Enter 'yes' to see history, anything else to skip: ").lower() == "yes":
        clear_screen()
        try:
            print("Calculation History:")
            with open("history.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No history available.")

if __name__ == "__main__":
    start_calculator()            

import math


def display_menu():
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")


def get_operand(prompt, previous_result):
    value = input(prompt)
    if value.upper() == "RESULT":
        return previous_result
    try:
        return float(value)
    except ValueError:
        print("Error: invalid input!")
        return None


def main():
    current_result = 0.0
    total_sum = 0.0
    num_calculations = 0

    while True:
        print(f"\nCurrent Result: {current_result}")
        display_menu()

        while True:  # Loop for valid menu input
            menu_selection = input("\nEnter Menu Selection: ")

            if not menu_selection.isdigit():
                print("Error: Invalid selection!")
                continue

            menu_selection = int(menu_selection)

            if menu_selection == 0:
                print("Thanks for using this calculator. Goodbye!")
                return  # **EXIT immediately (stops function execution)**

            if menu_selection in range(1, 8):
                break  # **Valid input, break the input loop**

            print("Error: Invalid selection!")

        if menu_selection == 7:
            if num_calculations == 0:
                print("Error: No calculations yet to average!")
                continue  # **Go back to menu selection**
            else:
                average = total_sum / num_calculations
                print(f"Sum of calculations: {total_sum:.2f}")
                print(f"Number of calculations: {num_calculations}")
                print(f"Average of calculations: {average:.2f}")
                continue  # **Back to menu selection**

        first_operand = get_operand("Enter first operand: ", current_result)
        if first_operand is None:
            continue
        second_operand = get_operand("Enter second operand: ", current_result)
        if second_operand is None:
            continue

        if menu_selection == 1:
            current_result = first_operand + second_operand
        elif menu_selection == 2:
            current_result = first_operand - second_operand
        elif menu_selection == 3:
            current_result = first_operand * second_operand
        elif menu_selection == 4:
            if second_operand == 0:
                print("Error: invalid input!")
                continue
            current_result = first_operand / second_operand
        elif menu_selection == 5:
            current_result = second_operand ** first_operand
        elif menu_selection == 6:
            if first_operand <= 0 or first_operand == 1 or second_operand <= 0:
                print("Error: invalid input!")
                continue
            current_result = math.log(second_operand, first_operand)

        total_sum += current_result
        num_calculations += 1


if __name__ == "__main__":
    main()

# imports


# global vars


# functions
def welcome():
    print("+-*/" * 10)
    print("Welcome to Simple Calculator.")
    print("+-*/" * 10)
    print("\n")

def calculator():
    print("+-*/" * 10)
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[x] Quit")
    print("\n")


# instructions
welcome()

while (True):
    calculator()

    user_operation = input("Choose an option: ")
    print("\n")

    if (user_operation == "x"):
        break

    num1 = float(input("Enter first numbner: "))
    num2 = float(input("Enter second numbner: "))
    print("\n")
    result = 0.0

    if (user_operation == "1"):
        result = num1 + num2
        print(str(num1) + " + " + str(num2) + " = " + str(result))
        print("\n")

    elif (user_operation == "2"):
        result = num1 - num2
        print(str(num1) + " - " + str(num2) + " = " + str(result))
        print("\n")

    elif (user_operation == "3"):
        result = num1 * num2
        print(str(num1) + " * " + str(num2) + " = " + str(result))
        print("\n")

    elif (user_operation == "4"):
        if (num2 != 0):
            result = num1 / num2
            print(str(num1) + " / " + str(num2) + " = " + str(result))
            print("\n")
        else:
            print("Cannot divide by 0!")
            print("\n")

print("Good bye!")
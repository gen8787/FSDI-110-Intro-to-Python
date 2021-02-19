
calc_to_run = "0"

def init():
    print("\n")
    print("[1] - Age Calculator")
    print("[2] - Tip Calculator")
    print("[q] - Quit")
    print("\n")



# A G E   C A L C U L A T I O N

def age_calculator():
    print("\n")
    print("*** Age Calculator ***")

    current_year = 2021
    birth_year = int(input("Enter your birth year: "))
    age = current_year - birth_year

    print("You are either " + str(age - 1) + " or " + str(age) + " years old!")
    print("\n")
    input("Press any key to continue...")



# T I P   C A L C U L A T O R

def tip_calculator():
    print("\n")
    print("*** Tip Calculator ***")

    amount = float(input("What is the total bill? : $"))
    tip_percent = int(input("What % tip would you like to give? : "))
    print("\n")

    tip = "%.2f" % float(tip_percent / 100 * amount)
    grand_total = ("%.2f" % round(float(((tip_percent / 100 +1) * amount)), 2))

    print(f"Tip amount: ${tip}")
    print(f"Grand Total: $ {grand_total}")
    print("\n")
    input("Press any key to continue...")



# I N S T R U C T I O N S
while (True):
    init()
    calc_to_run = str(input("Select a calculator: "))

    if (calc_to_run == "q"):
        print("Closing...")
        print("\n")
        break
    elif (calc_to_run == "1"):
        age_calculator()
    elif (calc_to_run == "2"):
        tip_calculator()
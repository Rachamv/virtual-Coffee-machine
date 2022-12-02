from coffee_maker import report
from money_machine import report


def process_admin():
    """This function for refill the coffee resources and turn off the machine."""
    import CoffeeMaker()
    while True:
        check = input("What would you like to do? Homepage, refill or off: ").lower()
        if check == "homepage":
            return None
        elif check == "refill":
            coffee_maker.resources["water"] = 300
            coffee_maker.resources["milk"] = 200
            coffee_maker.resources["coffee"] = 100
        elif check == "off":
            return "quit"
        else:
            print("Invalid Input")


class Admin:

    def __init__(self):
        """This function for report"""
        print("Welcome to the Admin panel")
        Admin.report()
        Admin.report()
        process_admin()

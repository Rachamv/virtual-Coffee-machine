"""This is a virtual Coffee machine"""
# TODO print logo
from art import logo
from test import MENU, resources
from replit import clear

print(logo)
profit = 0


def set_profit(x):
    """To save data on profit"""
    global profit
    profit = profit + x


def process_admin():
    """This function for report and refill the coffee resources """
    print("Welcome to the Admin panel")
    check = input("What would you like to do? Report or refill: ").lower()
    if check == "report":
        return process_report()
    elif check == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        choice()
    elif check == "off":
        exit()


#  TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def choice():
    """To get user input if they would like to get another cup of coffee"""
    # clear()
    order_again = input("Would you like to order again? Y or N : ").lower()
    if order_again == "y":
        return start()
    elif order_again == "admin":
        return process_admin()
    else:
        print("Thanks see  you again")


# TODO Print report
def process_report():
    """Report on resources and profit"""
    print("Current Resources")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${round(profit, 2)}")
    process_admin()


# TODO Make Coffee.
def process_making(user_choice):
    """Deduct the required ingredients from the resources and turn off the machine."""
    if user_choice in MENU:
        check_resources(user_choice)
        for item in resources:
            resources[item] -= MENU[user_choice]["ingredients"][item]
        process_coins(user_choice)
    else:
        print("Invalid Input"
              )  # Turn off the Coffee Machine by entering “off” to the prompt
        start()

def get_player_int(text):

  valid_user_input = False
  while not valid_user_input:
    a_string = input(text)
  
    try:
      user_input = int(a_string)

      if user_input > 0:
        valid_user_input = True
      else:
        print("You must enter a positive integer...")
  
    except:
      print("I'm terribly sorry, but we require an integer...")
 
  return user_input

# TODO Process coins.
def process_coins(user_choice):
    """calculate the total money and check for change or refund """
    
    quarters = get_player_int("Please insert quarters: ") * 0.25
    dime = get_player_int("Please insert dimes: ") * 0.1
    nickle = get_player_int("Please insert nickles: ") * 0.05
    penny = get_player_int("Please insert nickles: ") * 0.01

    total = (quarters + dime + nickle + penny)

    if total == MENU[user_choice]["cost"]:
        print(f"Enjoy your {user_choice} ☕")
        set_profit(MENU[user_choice]['cost'])
        choice()
    elif total > MENU[user_choice]["cost"]:
        charge = total - MENU[user_choice]['cost']
        print(f"Enjoy your {user_choice} ☕")
        print(f"Here is your change ${round(charge, 2)}")
        set_profit(MENU[user_choice]['cost'])
        choice()
    else:
        print(f"Sorry that's not enough money. Money refunded.${total}")
        choice()

    return None

# TODO Check resources sufficient?
def check_resources(user_choice):
    """TO check if resources are sufficient."""
    for item in resources:
        if resources[item] >= MENU[user_choice]["ingredients"][item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            start()


def start():
    """To get user choice of coffee """
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    process_making(user_choice)


start()
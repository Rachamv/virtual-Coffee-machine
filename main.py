"""This is a virtual Coffee machine"""
from art import logo
from data import MENU, resources
from time import sleep
from replit import clear


profit = 0


def set_profit(x):
  """To save data on profit"""
  global profit
  profit = profit + x
    

def choice():
  """To get user input if they would like to get another cup of coffee"""
  print(logo)
  while True:
    order_again = input("Would you like to order again? Y or N : ").lower()
    if order_again.lower() == "y":
      return True
    elif order_again.lower() == "n":
      return False
    else:
        print("Invalid Input.") 

        
def process_admin():
  """This function for report and refill the coffee resources and turn off the machine."""
  while True:  
    print("Welcome to the Admin panel")
    """Report on resources and profit"""
    print("Current Resources")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${round(profit, 2)}")
    check = input("What would you like to do? Homepage, refill or off: ").lower()
    if check == "homepage":
      return None
    elif check == "refill":
      resources["water"] = 300
      resources["milk"] = 200
      resources["coffee"] = 100
    elif check == "off":
      return "quit"
    else:
      print("Invalid Input") 


def process_making(user_choice, coffee):
  """Deduct the required ingredients from the resources."""
  for item in resources:
    resources[item] -= coffee[item]
  print(f"Enjoy your {user_choice} ☕")
  sleep(2)
  clear()
  return None


def get_player_int(text):

  valid_user_input = False
  while not valid_user_input:
    a_string = input(text)
  
    try:
      user_input = int(a_string)

      if user_input >= 0:
        valid_user_input = True
      else:
        print("You must enter a positive integer...")
  
    except:
      print("I'm terribly sorry, but we require an integer...")
  return user_input


def process_coins(coffee):
  """calculate the total money and check for change or refund """
  coin_types = [ ('quarters' , 0.25),
                 ('dimes'    , 0.10),
                 ('nickels ' , 0.05),
                 ('pennies'  , 0.01) ]

  total = 0
  for a_coin, a_value in coin_types:
    total += get_player_int(f"Please insert {a_coin}: ") * a_value

    if total == coffee["cost"]:
        set_profit(coffee['cost'])
        return None
    elif total > coffee["cost"]:
        change = total - coffee['cost']
        print(f"Here is your change ${round(change, 2)}")
        set_profit(coffee['cost'])
        return None
    else:
        pass
        
  print(f"Sorry that's not enough money. Money refunded.${total}")
  sleep(2)
  clear()
  return None


def check_resources(coffee):
  """TO check if resources are sufficient."""

  enough_of_everything = True
  
  for item in resources:
    if resources[item] < coffee[item]:
      print(f"Sorry there is not enough {item}.")
      enough_of_everything = False
      
  return enough_of_everything
            
def main():
  """To get user choice of coffee """

  while True: #main game loop
    print(logo)
    print("Here is what we offer:\nespresso: $1.5 \nlatte: $2.5 \ncappuccino: $3.0 \n")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    access = ["espresso", "latte", "cappuccino", "admin"]
    if user_choice in access:
        if user_choice == "admin":
            if process_admin() == "quit":
              break
            if choice():
              pass
            else:
              break #player opted to quit.
        else:
            coffee = MENU[user_choice]
            if check_resources(coffee["ingredients"]):
              payment = process_coins(coffee)
              if payment != 0:
                process_making(user_choice, coffee["ingredients"])
                if choice():
                  pass
                else:
                  break #player opted to quit.
            else:
              sleep(2)
              clear()
    else:
        print("Invaild input")

  print("\n<   <  < Thank you we will be expecting you  at Coffee Machine V2.0 >  >   >\n")

  return None
if __name__ == "__main__":
  main()
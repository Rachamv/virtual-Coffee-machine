class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = [ ('quarters' , 0.25),
                    ('dimes'    , 0.10),
                    ('nickels ' , 0.05),
                    ('pennies'  , 0.01) ]

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def get_player_int(self, text):
        """To get a positive integer from users"""
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
    

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += self.get_player_int(f"Please insert {coin}?: ") * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

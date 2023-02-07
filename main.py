import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    order = input("What size sandwich would you like to order (small, medium, large): ")
    ingredients = recipes[order]["ingredients"]
    cost = recipes[order]["cost"]
    if sandwich_maker_instance.check_resources(ingredients):
        print(f"Your order of a {order} sandwich costs {cost}.")
        coins = cashier_instance.process_coins()
        if cashier_instance.transaction_result(coins, cost):
            sandwich_maker_instance.make_sandwich(order, ingredients)
            print("Enjoy your sandwich!")
        else:
            print("Insufficient payment. Please try again.")
    else:
        print("Ingredients not available to make your sandwich. Please try again.")

if __name__=="__main__":
    main()
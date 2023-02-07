from data import recipes


class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if self.machine_resources.get(ingredient, 0) < ingredients[ingredient]:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(recipes[sandwich_size]["ingredients"]):
            for ingredient in order_ingredients:
                self.machine_resources[ingredient] -= order_ingredients[ingredient]
            return f"Your {sandwich_size} sandwich is being made."
        else:
            return "Ingredients are not sufficient to make sandwich."
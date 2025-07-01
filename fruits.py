class Fruit:
    def __init__(self, name, colour, weight):
        self.name = name
        self.colour = colour
        self.weight = weight
        self.ripe = False

    def describe(self):
        print(f"This is a {self.colour} {self.name}  that weighs {self.weight}g.")

    def ripen(self):
        self.ripe = True
        print(f"The {self.name} is now ripe.")

    def check_ripeness(self):
        if self.ripe:
            print(f"The {self.name} is ripe and ready to eat!")
        else:
            print(f"The {self.name} is not ripe yet.")

    def eat(self):
        if self.ripe:
            print(f"You eat the {self.name}. Delicious!")
        else:
            print(f"The {self.name} isn't ripe yet. Better wait.")



mango = Fruit("Mango", "Orange", 250)

mango.describe()
mango.check_ripeness()
#mango.ripen()
mango.check_ripeness()
mango.eat()


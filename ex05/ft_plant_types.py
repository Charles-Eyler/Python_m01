class Plant:
    weekly_growth = 0

    def __init__(self, name, height, age, growth):
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def show(self):
        print(f"{self._name}: {self._height}cm, \
{self._age} days old")

    def grow(self):
        self._height = round(self._height + self._growth, 2)

    def age(self):
        self._age += 1

    def set_height(self, height):
        if height == 0:
            print(f"{self._name}: Error, height can't be 0")
            print("Height uptade rejected")
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height uptade rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age):
        if age == 0:
            print(f"{self._name}: Error, age can't be 0")
            print("Age uptade rejected")
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age uptade rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


class Flower(Plant):
    def __init__(self, name, heigth, age, growth, bloom, color):
        super().__init__(name, heigth, age, growth)
        self._color = color
        self._bloom = bloom

    def bloom(self):
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def show(self):
        super().show()
        print(f"Color: {rose._color}")
        self.bloom()


class Tree(Plant):
    def __init__(self, name, heigth, age, growth, trunk_diameter):
        super().__init__(name, heigth, age, growth)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of"
              f" {self._height}cm long and {self._trunk_diameter}cm wide")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")
        print("[asking the oak to produce shade]")


class Vegetable(Plant):
    def __init__(self, name, heigth, age, growth, harvest_season,
                 nutricional_value):
        super().__init__(name, heigth, age, growth)
        self._nutricional_value = nutricional_value
        self._harvest_season = harvest_season

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutricional value: {self._nutricional_value}")

    def grow(self):
        super().grow()
        self._nutricional_value += 1


rose = Flower("Rose", 15.0, 10, 0.5, False, "red")
oak = Tree("Oak", 200.0, 365, 0.1, 5.0)
tomato = Vegetable("Tomato", 5.0, 10, 0.3, "April", 0)


def ft_plant_types():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose._bloom = True
    rose.show()
    print("\n=== Tree")
    oak.show()
    oak.produce_shade()
    print("\n==== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    day = 1
    while day <= 20:
        tomato.grow()
        day += 1
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()

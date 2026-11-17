class Plant:
    def __init__(self, name, height, age, growth):
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth
        self._stats = Plant.PlantStatistics()

    def show(self):
        print(f"{self._name}: {self._height}cm,"
              f" {self._age} days old")
        self._stats._show_counter += 1

    def grow(self):
        self._height = round(self._height + self._growth, 2)
        self._stats._grow_counter += 1

    def age(self):
        self._age += 1
        self._stats._age_counter += 1

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

    class PlantStatistics:
        def __init__(self):
            self._grow_counter = 0
            self._show_counter = 0
            self._age_counter = 0
            self._shade_counter = 0

    @staticmethod
    def age_verification(age) -> str:
        year_older = False
        if age <= 365:
            year_older = False
        else:
            year_older = True
        return f"Is {age} days more than one year? -> {year_older}"

    @classmethod
    def new_plant(cls):
        anonymous = cls("Unknown plant", 0.0, 0, 0)
        return anonymous


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
        print(f"Color: {self._color}")
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

    def grow(self) -> None:
        super().grow()
        self._stats._shade_counter += 1


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


class Seed(Flower):
    def __init__(self, name, heigth, age, growth, bloom, color):
        super().__init__(name, heigth, age, growth, bloom, color)
        self._seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self):
        super().bloom()
        if self._bloom:
            self._seeds += 45


def plant_statistics(plant_name) -> None:
    print(f"[Statistics for {plant_name._name}]")
    print(f"Stats: {plant_name._stats._grow_counter} grow,"
          f" {plant_name._stats._age_counter}"
          f" age, {plant_name._stats._show_counter} show")


rose = Flower("Rose", 15.0, 10, 0.5, False, "red")
oak = Tree("Oak", 200.0, 365, 0.2, 5.0)
sunflower_seed = Seed("Sunflower", 80.0, 45, 1.5, False, "yellow")


def ft_garden_analytics() -> None:
    print("=== Garden Plant Types ===")
    print("=== Check Year Old ===")
    print(Plant.age_verification(30))
    print(Plant.age_verification(400))
    print("\n=== Flower")
    rose.show()
    plant_statistics(rose)
    print("[asking the rose to bloom]")
    rose._bloom = True
    rose.show()
    plant_statistics(rose)
    print("\n=== Tree")
    oak.show()
    plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    plant_statistics(oak)
    print("\n==== Seed")
    sunflower_seed.show()
    plant_statistics(sunflower_seed)
    print("[make sunflower grow, age and bloom]")
    sunflower_seed._height = 108.5
    sunflower_seed._age = 64
    sunflower_seed._bloom = True
    sunflower_seed.grow()
    sunflower_seed.age()
    sunflower_seed.show()
    plant_statistics(sunflower_seed)
    print("\n==== Anonymous")
    anonymous = Plant.new_plant()
    anonymous.show()
    plant_statistics(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()

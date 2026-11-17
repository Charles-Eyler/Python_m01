class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age_days = age
        self.growth = growth

    def show(self):
        print(f"Created: {self.name}: {self.height}cm, "
              f"{self.age_days} days old")

    def grow(self):
        self.height = round(self.height + self.growth, 2)

    def age(self):
        self.age_days += 1


plant1 = Plant("Rose", 25.0, 30, 0.5)
plant2 = Plant("Oak", 200.0, 365, 0.1)
plant3 = Plant("Cactus", 5.0, 90, 1)
plant4 = Plant("Sunflower", 80.0, 45, 0.5)
plant5 = Plant("Fern", 15, 120, 0.2)


def ft_plant_growth():
    print("=== Plant Factory Output ===")
    Plant.show(plant1)
    Plant.show(plant2)
    Plant.show(plant3)
    Plant.show(plant4)
    Plant.show(plant5)


if __name__ == "__main__":
    ft_plant_growth()

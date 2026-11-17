class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Catcus", 15, 120)


def ft_garden_data():
    Plant.show(plant1)
    Plant.show(plant2)
    Plant.show(plant3)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()

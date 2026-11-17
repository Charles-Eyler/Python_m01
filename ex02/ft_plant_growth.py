class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age_days = age
        self.growth = growth

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self):
        self.height = round(self.height + self.growth, 2)

    def age(self):
        self.age_days += 1


plant1 = Plant("Rose", 25, 30, 0.8)


def ft_plant_growth() -> None:
    weekly_growth = 0
    for curr_day in range(7):
        print(f"=== Day {curr_day + 1} ===")
        plant1.show()
        weekly_growth += plant1.growth
        plant1.grow()
        plant1.age()
    print(f"Growth this week {round(weekly_growth, 2)}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()

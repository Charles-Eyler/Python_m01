class Plant:
    weekly_growth = 0

    def __init__(self, name, height, age, growth):
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def show(self):
        print(f"Plant Created: {self._name}: {self._height}cm, "
              f"{self._age} days old\n")

    def grow(self):
        self._height = round(self._height + self._growth, 2)

    def age(self):
        self.age += 1

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


plant1 = Plant("Rose", 15.0, 10, 0.5)


def valid_input():
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")


def invalid_input():
    plant1.set_height(-1)
    plant1.set_age(-1)
    print("\n")


def ft_garden_security():
    print("=== Garden Security System ===\n")
    plant1.show()
    valid_input()
    invalid_input()
    print(f"Current state: {plant1._name}: {plant1._height}cm, "
          f"{plant1._age} days old")


if __name__ == "__main__":
    ft_garden_security()

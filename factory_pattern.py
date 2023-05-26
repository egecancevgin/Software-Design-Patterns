class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"The {self.brand} car is driving.")


class CarFactory:
    def create_car(self, brand):
        if brand == "Toyota":
            return Car(brand)
        elif brand == "Honda":
            return Car(brand)
        elif brand == "BMW":
            return Car(brand)
        else:
            raise ValueError("Invalid car brand.")


# Usage example
factory = CarFactory()

car1 = factory.create_car("Toyota")
car1.drive()  # Output: The Toyota car is driving.

car2 = factory.create_car("Honda")
car2.drive()  # Output: The Honda car is driving.

car3 = factory.create_car("BMW")
car3.drive()  # Output: The BMW car is driving.

car4 = factory.create_car("Tesla")  # Raises ValueError

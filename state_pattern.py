class Car:
    def __init__(self, brand):
        self.brand = brand
        self.state = ParkedState(self)  # Initialize the car's state to Parked

    def change_state(self, state):
        self.state = state

    def drive(self):
        self.state.drive()

    def park(self):
        self.state.park()

    def refuel(self):
        self.state.refuel()


class CarState:
    def __init__(self, car):
        self.car = car

    def drive(self):
        raise NotImplementedError()

    def park(self):
        raise NotImplementedError()

    def refuel(self):
        raise NotImplementedError()


class ParkedState(CarState):
    def drive(self):
        print(f"The {self.car.brand} car is now driving.")
        self.car.change_state(DrivingState(self.car))

    def park(self):
        print("The car is already parked.")

    def refuel(self):
        print("The car needs to be parked before refueling.")


class DrivingState(CarState):
    def drive(self):
        print("The car is already driving.")

    def park(self):
        print(f"The {self.car.brand} car is now parked.")
        self.car.change_state(ParkedState(self.car))

    def refuel(self):
        print("The car needs to be parked before refueling.")


# Usage example
car = Car("Toyota")
car.drive()  # Output: The Toyota car is now driving.
car.drive()  # Output: The car is already driving.
car.park()  # Output: The Toyota car is now parked.
car.park()  # Output: The car is already parked.
car.refuel()  # Output: The car needs to be parked before refueling.
car.drive()  # Output: The Toyota car is now driving.

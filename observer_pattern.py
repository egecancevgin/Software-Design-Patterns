# Subject (Observable)
class Car:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def drive(self):
        self.notify("Car is driving...")

# Observer
class Driver:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")

# Usage example:
car = Car()

driver1 = Driver("Ege")
driver2 = Driver("Can")
driver3 = Driver("Efe")

car.attach(driver1)
car.attach(driver2)
car.attach(driver3)

car.drive()

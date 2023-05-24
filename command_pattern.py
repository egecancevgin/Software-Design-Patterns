# Command interface
class Command:
    def execute(self):
        pass


# Concrete commands
class SitCommand(Command):
    def __init__(self, dog):
        self.dog = dog
    
    def execute(self):
        self.dog.sit()


class FetchCommand(Command):
    def __init__(self, dog):
        self.dog = dog
    
    def execute(self):
        self.dog.fetch()


# Receiver class
class Dog:
    def sit(self):
        print("Dog is sitting.")
    
    def fetch(self):
        print("Dog is fetching.")


# Invoker class
class RemoteController:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()


def main():
     # Client code
     dog = Dog()
     sit_command = SitCommand(dog)
     fetch_command = FetchCommand(dog)

     remote = RemoteController()
     remote.set_command(sit_command)
     remote.press_button()  # Dog is sitting.

     remote.set_command(fetch_command)
     remote.press_button()  # Dog is fetching.

if __name__ == '__main__':
    main()
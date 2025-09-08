import random


class Robot:
    used_names = set()

    def __init__(self):
        self.name = None
        self.get_name()
    
    def get_name(self):
        while self.name is None or self.name in Robot.used_names:
            letters = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(2)]
            digits = [random.choice("0123456789") for _ in range(3)]
            self.name = "".join(letters + digits)
        Robot.used_names.add(self.name)
        return self.name

    def reset(self):
        self.name = None
        self.get_name()
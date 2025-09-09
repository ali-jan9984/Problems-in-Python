import string, random


class Robot:
    def __init__(self):
        self.name = self.get_name()

    def reset(self):
        self.name = self.get_name()

    def get_name(self):
        random.seed()
        letters = random.choices(string.ascii_uppercase, k = 2)
        digits = random.choices(string.digits, k = 3)
        return "".join(letters + digits)
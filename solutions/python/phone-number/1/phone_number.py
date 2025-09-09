import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self._clean(number)
        self.area_code = self.number[0:3]

    def _clean(self, raw_number):
        if re.search(r'[a-zA-Z]', raw_number):
            raise ValueError("letters not permitted")

        valid_characters = set("0123456789 -().+")
        for i, ch in enumerate(raw_number):
            if ch == '+' and i != 0:
                raise ValueError("punctuations not permitted")
            if ch not in valid_characters:
                raise ValueError("punctuations not permitted")

        digits = "".join(ch for ch in raw_number if ch.isdigit())

        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        if digits[0] == '0':
            raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
            raise ValueError("area code cannot start with one")
        if digits[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
            raise ValueError("exchange code cannot start with one")

        return digits

    def pretty(self):
        area = self.number[0:3]
        exchange = self.number[3:6]
        subscriber = self.number[6:]
        return f"({area})-{exchange}-{subscriber}"
class PhoneNumber:
    def __init__(self, number: str) -> None:
        self.number = self._clean(number)
        self.area_code = self.number[0:3]


    def _clean(self, raw_number: str) -> str:
        digits = self._extract_digits(raw_number)
        digits = self._normalize_country_code(digits)
        self._validate_nanp_rules(digits)
        return digits


    def _extract_digits(self, raw_number: str) -> str:
        if any(c.isalpha() for c in raw_number):
            raise ValueError("letters not permitted")
        if set(raw_number) - set("0123456789 ()-.+"):
            raise ValueError("punctuations not permitted")

        return "".join(ch for ch in raw_number if ch.isdigit())


    def _normalize_country_code(self, digits: str) -> str:
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11 and digits[0] != '1':
            raise ValueError("11 digits must start with 1")

        return digits[1:] if len(digits) == 11 else digits

    
    def _validate_nanp_rules(self, digits: str) -> None:
        if digits[0] == '0':
            raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
            raise ValueError("area code cannot start with one")
        if digits[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
            raise ValueError("exchange code cannot start with one")


    def pretty(self) -> str:
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
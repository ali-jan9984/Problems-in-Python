class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = self.card_num.replace(' ','')
        if len(num) <= 1 or not all(x.isnumeric() for x in num):
            return False
        
        result = []
        for i, d in enumerate(reversed(num)):
            digit = int(d)
            if i % 2 == 0:
                result.append(digit)
            else:
                double = digit * 2
                result.append(double - 9) if double > 9 else result.append(double)
        return sum(result) % 10 == 0
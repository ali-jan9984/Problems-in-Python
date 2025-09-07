class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')

    def valid(self):
        card_num = self.card_num
        if len(card_num) <= 1 or not all(x.isnumeric() for x in card_num):
            return False

        result = [int(d) for d in card_num]
        result[-2::-2] = [2 * d - 9 * (d >= 5) for d in result[-2::-2]]
        return sum(result) % 10 == 0
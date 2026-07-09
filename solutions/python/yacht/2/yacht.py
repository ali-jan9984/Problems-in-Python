from collections import Counter
# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"
def score(dice: list[int], category) -> int:
    c = Counter(dice)
    
    if category == "ones":
        return c[1] * 1
    if category == "twos":
        return c[2] * 2
    if category == "threes":
        return c[3] * 3
    if category == "fours":
        return c[4] * 4
    if category == "fives":
        return c[5] * 5
    if category == "sixes":
        return c[6] * 6
        
    if category == "full house":
        if sorted(c.values()) == [2, 3]:
            return sum(dice)
        return 0
    if category == "four of a kind":
        for face, cnt in c.items():
            if cnt >= 4:
                return face * 4
        return 0
    if category == 'little straight':
        return 30 if set(dice) == {1,2,3,4,5} else 0
    if category == 'big straight':
        return 30 if set(dice) == {2,3,4,5,6} else 0
    if category == 'choice':
        return sum(dice)
    if category == 'yacht':
        return 50 if len(c) == 1 else 0
    raise ValueError("unknown category")
SCORE = {}
for k, v in {
    "AEIOULNRST":1,
    "DG":2,
    "BCMP":3,
    "FHVWY":4,
    "K":5,
    "JX":8,
    "QZ":10
}.items():
    SCORE.update({x: v for x in k})


def score(word):
    return sum([SCORE[ch] for ch in word.upper()])
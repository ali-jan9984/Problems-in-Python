def score(x, y):
    distance_from_center = (x**2 + y**2) ** 0.5
    score = 0
    if distance_from_center <= 1:
        score = 10
    elif distance_from_center <= 5:
        score = 5
    elif distance_from_center <= 10:
        score = 1
    else:
        score = 0
    return score

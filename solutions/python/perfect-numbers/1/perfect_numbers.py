def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = 0
    for factor in range(1,number):
        if number % factor == 0:
            aliquot += factor
    if number == aliquot:
        return "perfect"
    elif number < aliquot:
        return "abundant"
    else:
        return "deficient"
print(classify(6))

    
def sum_of_multiples(limit, multiples):
    list_of_multiples = []
    for magical_value in multiples:
        if magical_value == 0:
            continue 
        multiple_of_mag_val = []
        for multiple in range(limit):
            if multiple % magical_value == 0:
                multiple_of_mag_val.append(multiple)
        list_of_multiples.extend(multiple_of_mag_val)
    unique_munltiples = set(list_of_multiples)
    return sum(unique_munltiples)
                
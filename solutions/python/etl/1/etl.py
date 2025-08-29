def transform(legacy_data):
    new_dict = {}
    for score,letters in legacy_data.items():
        for letter in letters:
            new_dict[letter.lower()] = score
    return new_dict
        
